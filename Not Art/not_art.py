from PIL import Image

img_name = 'not_art.png'

try:
    img = Image.open(img_name)   # Return an Image object
except:
    print ('Put not_art.png file on this directory')
    exit(1)

"""
def number(value):
    result = 0
    for key in dic:
        if str(value) == key:
            result = dic[key]

    return result

pixelsels = img.convert('RGB') #Convert it in RGB
width, height = img.size    #Getting the img's dimension

dic = {'0':0, '192':1, '255':2}

ans = []

for y in range(0, height,10):
    for x in range(0, width,10):
        r, g, b = pixelsels.getpixelsel((x, y))
        if r or g or b != 0:
            x = number(r)
            y = number(g)
            z = number(b)
            xyz = str(x)+str(y)+str(z)
            xyz_10 = int(xyz, 3)    # From base 3 to base 10
            ans.append(chr(97+((xyz_10+12)%26)))
"""
#-----------#
pixels = img.load()

arr = []
ans = []

first = 0
last = 29

while first*10+5 < 135:
    for i in range(first, last+1):
        arr.append(pixels[i*10+5,first*10+5])
    for i in range(first+1, last+1):
        arr.append(pixels[last*10+5,i*10+5])
    for i in reversed(range(first, last)):
        arr.append(pixels[i*10+5,last*10+5])
    for i in reversed(range(first+2, last)):
        arr.append(pixels[first*10+5,i*10+5])
    arr.append(pixels[(first+1)*10+5,(first+2)*10+5])
    first += 2
    last -= 2
arr.append(pixels[145,145])
arr.append(pixels[155,145])
arr.append(pixels[155,155])

for i in range(len(arr)):
    temp = 0
    for j in range(3):
        if arr[i][j] == 192:
            temp += 1*(3**(2-j))
        if arr[i][j] == 255:
            temp += 2*(3**(2-j))
    ans.append(chr(97+((temp+12)%26))) #Base3 + ROT+13

#-----------#

message = "".join(ans)

message = message.replace("underscore", "_")
message = message.replace("leftcurlybracket", "{")
message = message.replace("rightcurlybracket", "}")
message = message.replace("exclamationmark", "!")
message = message.replace("lowercase", "")

while message.find("uppercase") != -1:
    array = list(message)
    array[message.find("uppercase") + 9] = array[message.find("uppercase") + 9].upper()
    message = "".join(array)
    message = message.replace("uppercase", "", 1)

message = message.replace("htb", "HTB").replace("eof", "")
print(message)
