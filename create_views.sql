#Ex 1 
CREATE VIEW SortedArticlesTitleForViews AS select articles.author ,
articles.title, articles.slug , log.path from articles , log where log.path
LIKE concat('%' , articles.slug); 
CREATE VIEW SubTotalTitleView AS select
author , title , slug , count(author) as subTotal from
SortedArticlesTitleForViews group by author ,title, slug;

#Ex2 
CREATE VIEW SortedArticlesForViews AS select articles.author ,
articles.slug , log.path from articles , log where log.path LIKE concat('%' ,
articles.slug); CREATE VIEW SubTotalViews AS select author , slug ,
count(author) as subTotal from SortedArticlesForViews group by author , slug;
CREATE VIEW  AuthorViews AS select authors.name , SubTotalViews.slug ,
SubTotalViews.subtotal from SubTotalViews , authors where SubTotalViews.author
= authors.id order by SubTotalViews.author;

#Ex3 
CREATE VIEW Statistics AS select date_trunc('day', time) as day, count(*)
as Total , count(case status when '200 OK' then 1 end) as noErrorStatusTotal,
count(*) filter (where status != '200 OK') as ErrorStatusTotal from log group
by day; 
CREATE VIEW StatisticsPercentage AS select * , ( (errorstatustotal /
cast(total as float) ) * 100) as errorpercentage from Statistics;
