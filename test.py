from __future__ import print_function
import firebase_admin
from firebase_admin import credentials,firestore
from msvcrt import kbhit, getwch
import time
import sys
from Functions import*
from rsa import*
cred = credentials.Certificate('firebase.json') # Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred) # As an admin, the app has access to read and write all data, regradless of Security Rules
db=firestore.client()
result=db.collection("to,from").document("Ibrahim-ganesh").get()
#result=db.collection("user_public").document("Ibrahim").get()
print(result.to_dict())