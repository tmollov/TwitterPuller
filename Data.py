import json, os
from PIL import Image,ImageTk
import requests
from io import BytesIO
import tweepy
import Const

class UserInfo:
    def __init__(self,name=None,description=None,location=None,joined=None,imageUrl=None,followers=None,following=None):
        self.name = name
        self.location = location
        self.joined = joined
        self.imageUrl = imageUrl
        self.followers = followers
        self.following = following
        self.description = description

class Joined:
    def __init__(self,year,month):
        self.year = year
        self.month = self._setMonth(month)

    def _setMonth(self,month):
        return Const.months[month-1]

    def Show(self):
        return f"{self.month} {self.year}"

def TweepyApi():       
    keys = GetKeys()
    auth = tweepy.OAuthHandler(keys['ApiKey'], keys['ApiSecretKey'])
    auth.set_access_token(keys['AccessToken'], keys['AccessTokenSecret'])
    api = tweepy.API(auth)
    return api

def GetUserInfo(api,name):
    u = api.get_user(name)
    
    user = UserInfo(u.name,u.location,u.description,
        Joined(u.created_at.year,u.created_at.month),u.profile_image_url
            ,u.followers_count,u.friends_count)
    return user

def GetKeys(filename=None):
    default = 'keys.json' if filename==None else filename
    if os.path.isfile(default):
        return json.load(open(default, "r" ))
    else:
        return Exception

def GetProfileImage(url):
    response = requests.get(url.replace("_normal",""))
    img = Image.open(BytesIO(response.content))
    img = img.resize((200, 200))
    render = ImageTk.PhotoImage(img)
    return render