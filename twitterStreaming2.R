setwd("C:/Users/skcary/Dropbox/Programming/Personal R Projects/twitterStreaming")
library(streamR)
library(ROAuth)

load("my_oauth.Rdata")

file = "tweets.json"
track = "testfilterstream"
follow = NULL
loc = NULL
lang = NULL
minutes = 2
time = 60*minutes
tweets = NULL
filterStream(file.name = file, 
             track = track,
             follow = follow, 
             locations = loc, 
             language = lang,
             timeout = time, 
             tweets = tweets, 
             oauth = my_oauth,
             verbose = TRUE)

tweets.df <- parseTweets(file)

#testing writing to console
filterStream( file.name="", track=track, timeout=30, oauth=my_oauth )


