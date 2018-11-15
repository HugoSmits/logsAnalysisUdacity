#!/usr/bin/env python3
# Since python is an interpreter and can be installed in different places the
# env ensure it runs without problems !
# "Database code" for the DB Forum.
#####################################################
# vagrant up -> vagrant ssh -> psql -d news
#####################################################

import datetime
import psycopg2
import json

DBNAME = "news"

def get_month(month):
    if month == '1':
        monthString = "January"
    elif month == '2':
        monthString = "February"
    elif month == '3':
        monthString = "March"
    elif month == '4':
        monthString = "April"
    elif month == '5':
        monthString = "May"
    elif month == '6':
        monthString = "June"
    elif month == '7':
        monthString = "July"
    elif month == '8':
        monthString = "August"
    elif month == '9':
        monthString = "September"
    elif month == '10':
        monthString = "October"
    elif month == '11':
        monthString = "November"
    elif month == '12':
        monthString = "December"
    else:
        monthString = "Invalid Month"
    return monthString

def get_posts_ex1():
    db = psycopg2.connect(database=DBNAME)
    f = open('Output.txt', 'w')
    f.write("Solution to ex 1: " + "\r\n")
    c = db.cursor()
    c.execute("select articles.title , count(articles.author)"
              "as subtotal from articles , log where log.path LIKE"
              " concat('%' , articles.slug) group by articles.author , "
              "articles.title , articles.slug order by 2 DESC;")

    posts = c.fetchall()
    posts_new = [tuple(map(str, i)) for i in posts]

    for x in posts_new:
        string_json_first = (json.dumps(x[0]).rpartition('"')[0])[1:]
        string_json_second = (json.dumps(x[1]).rpartition('"')[0])[1:]

        concatenation_elements = string_json_first + \
            ' -- ' + string_json_second + " views"

        f.write(concatenation_elements + "\r\n")
        print(
            "The output has been written to Output.txt "
            "with the following info: " +
            concatenation_elements)

    f.write("\r\n")
    f.close()
    db.close()


def get_posts_ex2():
    db = psycopg2.connect(database=DBNAME)
    f = open('Output.txt', 'a')
    f.write("Solution to ex 2: " + "\r\n")
    c = db.cursor()
    # Can not have nested aggregate functions
    c.execute("select authors.name , count(author) as subTotal from authors"
              " , articles , log where (log.path LIKE "
              "concat('%' , articles.slug)) "
              "and (articles.author = authors.id) group by 1 order by 2 DESC;")

    posts = c.fetchall()
    posts_new = [tuple(map(str, i)) for i in posts]

    for x in posts_new:
        string_json_first = (json.dumps(x[0]).rpartition('"')[0])[1:]
        string_json_second = (json.dumps(x[1]).rpartition('"')[0])[1:]

        concatenation_elements = string_json_first + \
            ' -- ' + string_json_second + " views"

        f.write(concatenation_elements + "\r\n")
        print(
            "The output has been written to Output.txt "
            "with the following info: " +
            concatenation_elements)

    f.write("\r\n")
    f.close()
    db.close()


def get_posts_ex3():
    db = psycopg2.connect(database=DBNAME)
    f = open('Output.txt', 'a')
    f.write("Solution to ex 3: " + "\r\n")
    c = db.cursor()

    c.execute("select date_trunc('day', time) as day , "
              "((count(*) filter (where status != '200 OK') / "
              "cast(count(*) as float)) *100 ) "
              "as errorpercentage from log group by 1 "
              "having ((count(*) filter (where status != '200 OK') "
              "/ cast(count(*) as float)) *100 ) > 1;")

    posts = c.fetchall()
    posts_new = [tuple(map(str, i)) for i in posts]

    for x in posts_new:
        str_json_1 = (json.dumps(x[0]).rpartition('"')[0])[1:]
        string_json_2 = (json.dumps(x[1]).rpartition('"')[0])[1:]

        str_json_1_split, str_json_2_split = str_json_1.split()
        stringa, stringb, stringc = str_json_1_split.split('-')

        string_month = get_month(stringb[1])

        string_json_1_rounded = str(round(float(string_json_2), 2))

        concatenation_elements = string_month + ' ' + stringc + ', ' + \
            stringa + ' -- ' + string_json_1_rounded + "%" + " errors"

        f.write(concatenation_elements + "\r\n")
        print(
            "The output has been written to Output.txt "
            "with the following info: " +
            concatenation_elements)

    f.close()
    db.close()


if __name__ == '__main__':
    get_posts_ex1()
    get_posts_ex2()
    get_posts_ex3()
