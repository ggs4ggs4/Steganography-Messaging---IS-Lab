from __future__ import print_function
import firebase_admin
from firebase_admin import credentials,firestore
from msvcrt import kbhit, getwch
import time
import sys
from Functions import*
#============firebase================
cred = credentials.Certificate('firebase.json') # Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred) # As an admin, the app has access to read and write all data, regradless of Security Rules
db=firestore.client()
for i in db.collection("user_public").get():
    print(i.id, i.to_dict())

#============load user================
try:
    pass
    #open users stored private key file/img
    #open('abc.txt')
except:
    pass
    createUser()
    #open users stored private key file/img
    #open('abc.txt')

#============display/functioning================


while True:
    new=newMessages()
    others=chatList(new)
    print_chatlist(new, others)
    inp = timed_input("You have ten seconds to answer!",10)
    if inp != None:
        print(inp)
        cl=new+others
        display(cl,inp)
    