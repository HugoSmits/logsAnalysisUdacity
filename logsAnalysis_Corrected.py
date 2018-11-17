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


def get_posts_ex1():
    db = psycopg2.connect(database=DBNAME)
    f = open('Output.txt', 'w')
    f.write("Solution to ex 1: " + "\r\n")
    c = db.cursor()
    query = """
    SELECT articles.title,
           count(articles.author) AS subtotal
    FROM articles, log
    WHERE log.path LIKE concat('%' , articles.slug)
    GROUP BY articles.author,
             articles.title,
             articles.slug
    ORDER BY 2 DESC;
    """

    c.execute(query)

    posts = c.fetchall()
    posts_new = [tuple(map(str, i)) for i in posts]

    for x in posts_new:
        str_json_1 = (json.dumps(x[0]).rpartition('"')[0])[1:]
        str_json_2 = (json.dumps(x[1]).rpartition('"')[0])[1:]

        concatenation_elements = str_json_1 + \
            ' -- ' + str_json_2 + " views"

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
    query = """
    SELECT authors.name,
           count(author) as subTotal
    FROM authors, articles, log
    WHERE (log.path LIKE concat('%' , articles.slug))
    AND (articles.author = authors.id)
    GROUP BY 1
    ORDER BY 2 DESC;
    """
    c.execute(query)

    posts = c.fetchall()
    posts_new = [tuple(map(str, i)) for i in posts]

    for x in posts_new:
        str_json_1 = (json.dumps(x[0]).rpartition('"')[0])[1:]
        str_json_2 = (json.dumps(x[1]).rpartition('"')[0])[1:]

        concatenation_elements = str_json_1 + \
            ' -- ' + str_json_2 + " views"

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
    query = """
    SELECT to_char(TIME::date,'FMMonth FMDD, YYYY') AS day,
           round( ((count(*) filter (WHERE status != '200 OK') /
            cast(count(*) AS numeric) ) *100), 2 ) AS errorpercentage
    FROM log
    GROUP BY 1
    HAVING ((count(*) filter (WHERE status != '200 OK') /
    cast(count(*) AS float)) *100 ) > 1;
    """
    c.execute(query)

    posts = c.fetchall()
    posts_new = [tuple(map(str, i)) for i in posts]

    for x in posts_new:
        str_json_1 = (json.dumps(x[0]).rpartition('"')[0])[1:]
        str_json_2 = (json.dumps(x[1]).rpartition('"')[0])[1:]

        concatenation_elements = str_json_1 + ' -- ' \
            + str_json_2 + "%" + " errors"

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
