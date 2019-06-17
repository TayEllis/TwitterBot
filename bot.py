import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ui6oXLxrJI7Q2cCdfDuBPrJaF",
    "0JumGqqKb4kCHl705omTv94QNGDJutL1IYbJXdpCWYJHRljlOn")
auth.set_access_token("1140645371237916672-c3oOQsomNrNWFxEbOBYaMz3SOBwMXB",
    "LQK48aIU0lbGog4wtscOVacJkUJ1GjTcCzSR8sqKxxvw4")

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

try:
    api.update_status("Test Tweet From Bot")
    print("Tweet Tweet")
except:
    print("Tweet Failed")

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
