#!/usr/bin/env python
from tweepy import (Stream, OAuthHandler)
from tweepy.streaming import StreamListener
import time
from os import environ
import tweepy
import random

#tes
#sekarang lagi make piku
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)
user = api.me()
# the profile name to be updated
name = "piku tag on!"

#ava buka
avabuka = "./assets/images/open.png"
avatutup = "./assets/images/closed.png"

# updating the background picture
api.update_profile(name)
print (user.name)

class Listener(StreamListener):

    tweet_counter = 0 # Static variable
    total = 0
    print("jasa tag is starting")

    def login(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth

    def on_status(self, status):

        
        # Upload images and get media_ids
        filenames = ['./assets/images/1.png', 
                     './assets/images/2.png', 
                    './assets/images/3.png',
                    './assets/images/4.png']
        media_ids = []
        
        for filename in filenames:
             res = api.media_upload(filename)
             media_ids.append(res.media_id)
        
        #deklarasi variabel
        tweetId = status.id
        nama = status.user.name
        username = status.user.screen_name
        link = ''
        #" " + '\n\n' + emolink + ":https://twitter.com/pikuupa/status/1373587658748870658?s=19"
        
        kata2 = ["haloo kak pas banget nih kak, di @pikupaw ada yang gemes-gemes sampai yang dark! yuk cek duluu",
                "haai kak , kakak lagi nyari layout ya? @pikupaw lagi open layout nih, pengerjaannya 1-3 hari ajaa, bisa dicariin juga fotonya, yuk kak cek duluu di @pikupaw",
                "kalo cari layout kesini aja kaak, ada layout gemes sampai yang dark! yuk ditunggu ya kaak dmnya di @pikupaw",
                "eh kaak, cek dulu yuuk siapa tau jodooh hehee! @pikupaw",
                "halooo kaaak @pikupaw lagi open loh! tanpa batasan slot, yuk kajja order? bisa diliat dulu nih kaak",
                "di @pikupaw semua ada kaak, dari yang lucu, sampai yang classy atau dark, yuk diorderr <3",
                "kak, cari layout? ke @pikupaw aja yuuk, lagi opeeen, diliat dulu aja kak siapa tau sukaa",
                "haai kak, jajan di @pikupaw yuk! dari yang gemes sampai yang dark ada semua, lengkapnya cek link di bio @pikupaw yaaa",
                "halo kaak, beli layout di @pikupaw yuk! lagi open nih hehe! cek dulu katalognya siapa tau sukaa, lengkapnya ada di pinned @pikupaw yaa",
                "misiii kak, yuk jajan di @pikupaw, mau layout gemes/handraw/classy/dark ada semua kok, diliat dulu aja kaak, lengkapnya ada di link bio @pikupaw yaa, ditunggu hehee"]
        
        #cek pikupa buka apa engga
        
        # the ID of @pikuupa
        idpiku = '1385032698993905664'
        # fetching the user
        user = api.get_user(idpiku)
        # fetching the screen name
        dnpiku = user.name
        
        
        
        if 'open' in dnpiku.lower():
            print ("pikupa open")
            #ketika status tuh dalam bentuk quote, di skip
            if status.is_quote_status is True:
                print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")
                
                
            elif 'anime' in (status.text).lower():
                print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")
                
    
            elif 'scenery' in (status.text).lower():
                print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")
                
            #ketika status tuh bukan dalam bentuk quote jalanin ini
            
            elif 'anitwt' in (status.text).lower():
                print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")

            elif 'jadi hari ini' in (status.text).lower():
                print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")

            elif 'couple' in (status.text).lower():
                print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")
            
            elif 'cp' in (status.text).lower():
                print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")
                
            #ketika status tuh bukan dalam bentuk quote jalanin ini
            else:
                Listener.tweet_counter += 1
                
                api.update_status("@" + username + " " + kata2[random.randint(0, 9)] , media_ids=media_ids, in_reply_to_status_id = tweetId)
                print( str(Listener.tweet_counter) +".  " + status.user.screen_name + ": " + status.text + " ( replied )")
                
                if Listener.tweet_counter < Listener.stopAt:
                    return True
                else:
                    print('Max num reached = ' + str(Listener.tweet_counter))
                    Listener.tweet_counter = 0
                    print('istirahat dulu 1 jaaam')
                    name = "Istirahat"
                    api.update_profile(name)
                    time.sleep(3600)
                    listener.getTweetsByHashtag(6, ['layout drop katalog', 'leyot drop katalog', 'tawarin layout', 'leot drop katalog','tawarin leyot', 'tawarin leot', 'wtb leot', 'wtb layout', 'wtb leyot'])
                    # the profile name to be updated
                    name = "Arkean."
                    print('mulai lagii :3')
                    # updating the background picture
                    api.update_profile(name)
                    print("> " + status.user.screen_name + ": " + status.text + " ( skipped )")
                
        else:
            print ("PIKU is CLOSED")                
            # the profile name to be updated
            name = "Arkean."  
            # updating the background picture
            api.update_profile(name)
        


    


    def getTweetsByHashtag(self, stop_at_number, hashtag):
        try:
            Listener.stopAt = stop_at_number
            auth = self.login()
            streaming_api = Stream(auth, Listener(), timeout=60)
            # Atlanta area.
            streaming_api.filter(track=hashtag, is_async=True, stall_warnings=True)
        except KeyboardInterrupt:
            print('Got keyboard interrupt')

listener = Listener()
listener.getTweetsByHashtag(6, ['layout drop katalog', 'leyot drop katalog', 'tawarin layout', 'leot drop katalog','tawarin leyot', 'tawarin leot', 'wtb leot', 'wtb layout', 'wtb leyot'])
