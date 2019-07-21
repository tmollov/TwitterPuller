import tkinter as tk
from tkinter import font as f
import Data
import Const
from Const import Background

api = Data.TweepyApi()

mainWindow = tk.Tk()
mainWindow.title(Const.AppTitle)
mainWindow.configure(bg="white")
width = int(mainWindow.winfo_screenwidth() / 3)
height = int(mainWindow.winfo_screenheight() / 2)
mainWindow.geometry(f"{width}x{height}")
mainWindow.resizable(0, 0)

frame = tk.Frame(mainWindow,bg=Background.White)
infoFrame = tk.Frame(mainWindow,bg=Background.White)  

var = tk.StringVar()
var.set("")
emptyLable= tk.Label(frame,
    bg=Background.White,textvariable=var)

inputInfo = tk.Label(frame,
    text=Const.InputHeader,
    bg=Background.White)

searchBar = tk.Entry(frame, 
    justify="center",
    bg="white")

heading1 = f.Font(family='Arial', size=24)
heading2 = f.Font(family='Arial', size=20)
heading3 = f.Font(family='Arial', size=16)
def showInfo(event):
    username = searchBar.get()
    user = None
    profilePic = None
    try:
        user = Data.GetUserInfo(api,username)
        profilePic = Data.GetProfileImage(user.imageUrl)
    except Exception:
        var.set(f"User *{username}* not found!")
        return


    img = tk.Label(infoFrame,image=profilePic,
        bg=Background.White)
    img.image = profilePic
    user.followers
    nameLabel = tk.Label(infoFrame, text=user.name,
        bg=Background.White)
    descriptionLabel = tk.Label(infoFrame, text=user.description,
        bg=Background.White)
    locationLabel = tk.Label(infoFrame, text=user.location,
        bg=Background.White,wraplength=500,justify="center")
    followersLabel = tk.Label(infoFrame, text=f"Followers: {user.followers}",
        bg=Background.White)
    followingLabel = tk.Label(infoFrame, text=f"Following: {user.following}",
        bg=Background.White)
    
    def showSearch(self):
        infoFrame.pack_forget()
        img.pack_forget()
        nameLabel.pack_forget()
        descriptionLabel.pack_forget()
        locationLabel.pack_forget()
        followersLabel.pack_forget()
        followingLabel.pack_forget()
        backBtn.pack_forget()
        infoFrame.pack_forget()
        inputInfo.pack()
        searchBar.pack()
        emptyLable.pack()
        frame.pack()
        frame.tkraise()
    
    backBtn = tk.Button(infoFrame,text="< Back to Search",bg=Background.White)
    
    backBtn.bind("<Button-1>",showSearch)
    
    nameLabel["font"] = heading1
    locationLabel["font"] = heading2
    descriptionLabel["font"] = heading2
    followersLabel["font"] = heading3 
    followingLabel["font"] = heading3
    frame.pack_forget()
    infoFrame.pack()
    img.pack()
    nameLabel.pack()
    descriptionLabel.pack()
    locationLabel.pack()
    followersLabel.pack()
    followingLabel.pack()
    backBtn.pack()


def clearLabel(event):
    var.set("")

searchBar.bind("<Return>",showInfo)
emptyLable.bind("<Button-1>",clearLabel)


emptyLable["font"] = heading1
searchBar["font"] = heading1
inputInfo["font"] = heading1

inputInfo.pack()
searchBar.pack()
emptyLable.pack()

if __name__ == '__main__':
    frame.pack()
    frame.tkraise()
    mainWindow.mainloop()  