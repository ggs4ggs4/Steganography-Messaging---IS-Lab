from __future__ import print_function
import firebase_admin
from firebase_admin import credentials,firestore
from msvcrt import kbhit, getwch
import time
import sys,os

def createUser():
    pass
    #create pq set and images
    #store in user_data/keys

def display(allUsers,User):
    pass
    #display the message history with the selected user
    #let user enter a message or return to the chat list screen
    os.system('cls')
    print("Message (Enter to return): ",end='')
    message = input()
    if message=="":
        return ""
    else:
        EncodeAndSend(message)#add key and name etc if needed to the arguments
        return "ReDisplay"

def EncodeAndSend(message):
    #encode
    #send
    #update receivers newmessage entry in db
    return

def newMessages():
    pass
    #checkin dbif new
    #return list of new

def chatList(new):
    pass
    os.system('cls')
    #import all text files names
    #print indexed names
    #retrn chatlist with new at start new 

def print_flush(*args):
    print(*args, end='')
    sys.stdout.flush()

def timed_input(prompt='', timeout=None):
    if timeout is None:
        return input(prompt)
    print_flush(prompt)
    start = time.time()
    response = ''
    while time.time() - start < timeout:
        if kbhit():
            char = getwch()
            if char == '\r':
                break
            elif char == '\x08': # backspace
                if response:
                    print_flush(char, char)
                    response = response[:-1]
            else:
                print_flush(char)
                response += char
        time.sleep(0.01)
    else:
        response = None
    print()
    return response
