from __future__ import print_function
import firebase_admin
from firebase_admin import credentials,firestore
from msvcrt import kbhit, getwch
import time
import sys
from Functions import*
from rsa import*

#============firebase================
cred = credentials.Certificate('firebase.json') # Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred) # As an admin, the app has access to read and write all data, regradless of Security Rules
db=firestore.client()
for i in db.collection("user_public").get():
    print(i.id, i.to_dict())

#============load user================
try:
    #open users stored private key file/img
    with open("./user_data/keys/rsa.txt","r") as file:
        publicKey=tuple(map(int,file.readline().split(',')))
        privateKey=tuple(map(int,file.readline().split(',')))       
        stegImg=Image.open("./user_data/keys/stegimg.jpg", 'r') 
except:
    #create users stored private key file/img
    createUser()
    #open users stored private key file/img
    with open("./user_data/keys/rsa.txt","r") as file:
        publicKey=tuple(map(int,file.readline().split(',')))
        privateKey=tuple(map(int,file.readline().split(',')))       
        stegImg=Image.open("./user_data/keys/stegimg.jpg", 'r') 

#============display/functioning================
while True:
    new=newMessages()
    allUsers=chatList(new)
    inp = timed_input("You have ten seconds to answer!",10)
    if inp != None and inp!="":
        print(inp)
        while True:
            returned= display(allUsers,int(inp))
            if returned=="":
                break