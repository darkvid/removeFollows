import tweepy
import sys
import time

print ()
print ("**************************")
print ("**************************")
print ("**************************")
print ("**************************")
print ("*******UnFollow v0.1*******")
print ("**************************")
print ("**************************")
print ("**************************")
print ("**************************")
print ()
nick = input("Introduce tu nick de Twitter --> ")

print ("El nick es " + nick)
print()

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
followers = api.followers_ids(nick)
friends = api.get_user(nick).friends()

print ("Numero de tweets " + str(len(public_tweets)))
print ("Numero de personas que te siguen " + str(len(followers)))
print ("Numero de personas a las que sigues " + str(len(friends)))

print ()
print ("Vamos a ver qué amigos no twittean desde el año pasado")
#print (friends[0])

file = open ("eliminar.txt", "w")

try:
    for f in tweepy.Cursor(api.friends).items():
        friendTweets = api.user_timeline(id=f.id)
        #print ("numero tweets " + str(len(friendTweets)))
        if friendTweets[0].created_at.year == 2019:
            print ("ultimo tweet del usuario " + str(f.screen_name) + " en " + str(friendTweets[0].created_at.year))
            file.write(f.screen_name + "\n")

except tweepy.RateLimitError:
    for i in range(2 * 60, 0, -1):
        time.sleep(1)
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} tiempo de descanso .".format(i))
        sys.stdout.flush()
    
except tweepy.TweepError:
    print('no se puede buscar más gente en este momento')
    exit() 

file.close()


print ()
print ("Thanks")
print ()