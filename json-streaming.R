#https://docs.microsoft.com/en-us/power-bi/service-real-time-streaming 
#https://www.r-bloggers.com/real-time-data-visualization-using-r-and-data-extracting-from-sql-server/ 
#http://jeroen.github.io/mongo-slides 
library(jsonlite)
library(curl)
library(MASS)
#simple stream test
stream_out(cats, stdout())

#example 2
# con <- curl("https://jeroenooms.github.io/data/diamonds.json")
# mydata <- stream_in(con, pagesize = 1000)


