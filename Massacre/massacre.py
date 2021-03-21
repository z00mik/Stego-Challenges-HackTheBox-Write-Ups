#!/usr/bin/env python3

from PIL import Image
import re

R = 0; G = 1; B = 2

img_name = 'massacre.png'

try:
    img = Image.open(img_name)   # Return an Image object
except:
    print ('Put massacre.png file on this directory')
    exit(1)

pixels = list(img.getdata())    # Gets the image's data
nozero = []

print("Extracting non zero pixels...")
for rgb in pixels:  # Skipping zero rgb's
        if rgb != (0, 0, 0):
                nozero.append(rgb)
message = ""

print("Getting the message...")
# Getting the last digit from the RBG tuples
for i in nozero:
        if i[0] % 10 != 0 or i[1] % 10 != 0 or i[2] % 10 != 0:  # Some numbers don't end with 0, so we'll want it

            r = '{:08b}'.format(i[R] % 10)[6:8] # Get the last 2 bits of the octal obtained by doing module 10, and convert them to binary
            g = '{:08b}'.format(i[G] % 10)[5:8] # Get the last 3 bits ----
            b = '{:08b}'.format(i[B] % 10)[5:8] # Get the last 3 bits ----
            str = r + g + b # All the bits represents a binary number
            i = chr(int(str[:8], 2))  # ASCII char from each 8 bits number converted to decimal
            message = message + i   # Joins each char to a message

print("Looking for the flag...")
regex = re.compile("(HTB{.*})") # Creating the pattern to find the flag inside the message
found = regex.search(message)   # Searching that regex in the message

if found:
    print(found.group(1))   # Shows the match
    exit(0)
else:
    print ("Nothing works")
    exit(1)