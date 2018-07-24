library(streamR)
library(ROAuth)

requestURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "https://api.twitter.com/oauth/access_token"
authURL <- "https://api.twitter.com/oauth/authorize"
# The string within the quotation marks has to be replaced with the actual
# consumerKey and consumerSecret.
consumerKey <- "W1hrepnFRz4STYJqZagxxk5yE"
consumerSecret <- "ql5sxM7g275q1k1X1T4eiGKHMLZsvLV27ip3RydrcfyKG1qSch"
# The next two lines establish a connection to the Twitter API.
# The system will print a URL which should be copied in a browser to receive a PIN number.
# This PIN has to be entered in the R-console.
my_oauth <- OAuthFactory$new(consumerKey = consumerKey, 
                             consumerSecret = consumerSecret, 
                             requestURL = requestURL, 
                             accessURL = accessURL, 
                             authURL = authURL)
my_oauth$handshake(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl"))
# Once the connection is established we can save it so that we do not have
# repeat this process.
save(my_oauth, file = "my_oauth.Rdata")
