from __future__ import print_function
import firebase_admin
from firebase_admin import credentials,firestore
from msvcrt import kbhit, getwch
import time
import sys
from Functions import*
from rsa import*
from steg import*



e= encrypt("heloo how arar 8",(1979,3233))

encodeLSB(e, "./user_data/keys/stegimg.jpg", "Encoded_image2")
res = decodeLSB("Encoded_image2.png")
d=decrypt(res,(659,3233))
print(d)