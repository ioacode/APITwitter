#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:15:27 2019

@author: ahmadshiddiq
"""

#!/usr/bin/python
import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('********', '*******')
auth.set_access_token('*******', '********')

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "google",
                           since = "2014-02-14",
                           until = "2019-02-15",
                           lang = "en").items():
    print("Lagi proses ----------------------------")
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
