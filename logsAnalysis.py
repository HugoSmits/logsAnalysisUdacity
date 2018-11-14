# "Database code" for the DB Forum.
#####################################################
# Author: Hugo Smits
# Date of creation : 12/11/2018
# Last modified : 12/11/2018
#####################################################
# Views must be created in vagrant/psql environment before the c.executes can run the selects !
#####################################################
# vagrant up -> vagrant ssh -> psql -d news
#####################################################
#WebBio:
#https://www.postgresql.org/docs/9.6/app-psql.html
#http://www.postgresqltutorial.com/postgresql-python/
#https://www.tutorialspoint.com/postgresql
#https://www.hacksparrow.com/python-split-string-method-and-examples.html
#https://stackoverflow.com/questions/22412258/get-the-first-element-of-each-tuple-in-a-list-in-python
#https://www.postgresql.org/message-id/271d057bf6acfee775e7c47fe899cc9e%40biglumber.com
#https://www.w3schools.com/sql/sql_like.asp
#https://popsql.io/learn-sql/postgresql/how-to-group-by-time-in-postgresql/
#https://stackoverflow.com/questions/1400078/is-it-possible-to-specify-condition-in-count/1400115
#https://dba.stackexchange.com/questions/112796/postgres-count-with-different-condition-on-the-same-query
#https://stackoverflow.com/questions/1780242/postgres-math-expression-calculcated-for-each-row-in-table
#####################################################

import datetime
import psycopg2
import json

DBNAME = "news"

def get_month( month ):
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
  c.execute("select articles.author , articles.title, articles.slug , log.path from articles , log where log.path LIKE concat('%' , articles.slug);")
  c.execute("select author , title, slug , count(author) as subTotal from SortedArticlesTitleForViews group by author , title , slug;")
  c.execute("select title , subtotal from SubTotalTitleView order by subtotal DESC;")
  posts = c.fetchall()
  posts_new = [tuple(map(str, i)) for i in posts]

  #print(posts_new)
  string_json = json.dumps(posts_new)
  for x in posts_new:
    string_json_first = (json.dumps(x[0]).rpartition('"')[0])[1:]
    string_json_second = (json.dumps(x[1]).rpartition('"')[0])[1:]

    concatenation_elements = string_json_first + ' -- ' + string_json_second +  " views"
    f.write(concatenation_elements + "\r\n")
    print("The output has been written to Output.txt with the following info: " + concatenation_elements)

  #print(string_json_first)
  #print(string_json_second)
  #print(string1)
  #print(string2) string_json_first_element = string_json_first.rpartition('"')[0]
    #string_json_second_element = string_json_second.rpartition('"')[0]
  f.write("\r\n")
  f.close()
  db.close()

def get_posts_ex2():
  db = psycopg2.connect(database=DBNAME)
  f = open('Output.txt', 'a')
  f.write("Solution to ex 2: " + "\r\n")
  c = db.cursor()
  c.execute("select articles.author , articles.slug , log.path from articles , log where log.path LIKE concat('%' , articles.slug);")
  c.execute("select author , slug , count(author) as subTotal from SortedArticlesForViews group by author , slug;")
  c.execute("select authors.name , SubTotalViews.slug , SubTotalViews.subtotal from SubTotalViews , authors where SubTotalViews.author = authors.id order by SubTotalViews.author;")
  c.execute("select name , sum(subtotal) as Total from AuthorViews group by 1 order by 2 DESC;")
  posts = c.fetchall()
  posts_new = [tuple(map(str, i)) for i in posts]

  #print(posts_new)
  string_json = json.dumps(posts_new)
  for x in posts_new:
    string_json_first = (json.dumps(x[0]).rpartition('"')[0])[1:]
    string_json_second = (json.dumps(x[1]).rpartition('"')[0])[1:]

    concatenation_elements = string_json_first + ' -- ' + string_json_second +  " views"
    f.write(concatenation_elements + "\r\n")
    print("The output has been written to Output.txt with the following info: " + concatenation_elements)

  #print(string_json_first)
  #print(string_json_second)
  #print(string1)
  #print(string2) string_json_first_element = string_json_first.rpartition('"')[0]
    #string_json_second_element = string_json_second.rpartition('"')[0]
  f.write("\r\n")
  f.close()
  db.close()


def get_posts_ex3():
  db = psycopg2.connect(database=DBNAME)
  f = open('Output.txt', 'a')
  f.write("Solution to ex 3: " + "\r\n")
  c = db.cursor()
  c.execute("select date_trunc('day', time) as day, count(*) as Total , count(case status when '200 OK' then 1 end) as noErrorStatusTotal, count(*) filter (where status != '200 OK') as ErrorStatusTotal from log group by day;")
  c.execute("select * , ( (errorstatustotal / cast(total as float) ) * 100) as errorpercentage from Statistics;")
  c.execute("select day , errorpercentage from StatisticsPercentage where errorpercentage > 1")
  posts = c.fetchall()
  posts_new = [tuple(map(str, i)) for i in posts]

  #print(posts_new)
  string_json = json.dumps(posts_new)
  for x in posts_new:
    string_json_first = (json.dumps(x[0]).rpartition('"')[0])[1:]
    string_json_second = (json.dumps(x[1]).rpartition('"')[0])[1:]

    string_json_first_split , string_json_second_split = string_json_first.split()
    stringa , stringb , stringc= string_json_first_split.split('-')
    #string_json_first_split_second = stringc + '-' + stringb + '-' + stringa
    
    string_month = get_month(stringb[1])

    string_json_first_rounded = str(round(float(string_json_second), 2))

    concatenation_elements = string_month + ' ' + stringc + ', ' + stringa + ' -- ' + string_json_first_rounded + "%" +  " errors"
    #concatenation_elements = string_json_first_split_second + ' -- ' + string_json_first_rounded + "%" +  " errors"
    f.write(concatenation_elements + "\r\n")
    print("The output has been written to Output.txt with the following info: " + concatenation_elements)

  #print(string_json_first_element1)
  #print(string_json_second_element1)
  #print(string1)
  #print(string2) string_json_first_element = string_json_first.rpartition('"')[0]
    #string_json_second_element = string_json_second.rpartition('"')[0]
  f.close()
  db.close()



if __name__ == '__main__':
  get_posts_ex1()
  get_posts_ex2()
  get_posts_ex3()