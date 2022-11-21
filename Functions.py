from __future__ import print_function
import firebase_admin
from firebase_admin import credentials,firestore
from msvcrt import kbhit, getwch
import time
import sys,os
from PIL import Image
from rsa import*
def genData(data):
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def stegEncode(img, data):
    newimg=img.copy()
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
    return newimg  

def stegDecode(img):
    data = ''
    imgdata = iter(img.getdata())
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data
            
def stego_example():
    img='stego img.jpg';        
    img = Image.open(img, 'r')
    text="this needs to be decoded"
    newimage=encode(img,text)
    newimage.save("Encoded_image.jpg")
    textd=decode(newimage)
    print(textd)
  

def createUser():
    pub,pvt=generate_key()
    with open("./user_data/keys/rsa.txt","w") as file:
        file.write(str(pub[0])+','+str(pub[1])+'\n')
        file.write(str(pvt[0])+','+str(pvt[1])+'\n')
    
    #create random image
    #upload to db

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
