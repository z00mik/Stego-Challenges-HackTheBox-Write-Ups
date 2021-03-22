# !/usr/bin/env python3

from PIL import Image
import brainfuck

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


def get_replace(binary_values,bs,next=False):
    index = int.from_bytes(bs, "little") - 128
    if(next):
        _bs = bitstring_to_bytes(binary_values[index + 1])
    else:
        _bs = bitstring_to_bytes(binary_values[index])
    return _bs


def generate_binary_string():
    try:
        img = Image.open("Unprintable.png") # Open the img
    except:
        print('Put Unprintable.png file on this directory')
        exit(1)

    pixels = img.convert('RGB') #Convert it in RGB

    width, height = img.size    #Getting the img's dimension

    binary_string = ""

    # Loop every 10 pixels
    for y in range(0, height, 10):
        for x in range(0, width, 10):

            r, g, b = pixels.getpixel((x, y))

            if r == g == b == 0:    #If the pixel is 0 = black = 0
                binary_string += "0"
            elif r == g == b == 255:    #If the pixel is 255 = white = 1
                binary_string += "1"

    return binary_string


def decode_binary(binary_string):

    binary_values = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    decoded_str = ""
    raw_str=""
    for i in range(len(binary_values)):
        bs = bitstring_to_bytes(binary_values[i])
        raw_str += str(bs).replace("b'","").replace("'","")
        try:
            decoded_str += bs.decode()
        except:
            _bs = get_replace(binary_values,bs)
            try:
                decoded_str += _bs.decode()
            except:
                __bs = get_replace(binary_values, _bs)
                decoded_str += __bs.decode()
                __bs = get_replace(binary_values, _bs, True)
                decoded_str += __bs.decode()
                continue
            _bs = get_replace(binary_values, bs, True)
            try:
                decoded_str += _bs.decode()
            except:
                __bs = get_replace(binary_values, _bs)
                decoded_str += __bs.decode()
                __bs = get_replace(binary_values, _bs, True)
                decoded_str += __bs.decode()
    print("\033[94m" + "The raw decoded string is:\n" + '\033[1;37;0m' + raw_str )
    return decoded_str


def rle_decode(decoded_str):
    final_decoded_string = ""
    i = 0
    while i < len(decoded_str):
        if decoded_str[i].isdigit():
            if decoded_str[i + 1].isdigit():
                final_decoded_string += int(decoded_str[i] + decoded_str[i + 1]) * decoded_str[i + 2]
                i += 3
            else:
                final_decoded_string += int(decoded_str[i]) * decoded_str[i + 1]
                i += 2
        else:
            final_decoded_string += decoded_str[i]
            i += 1
    return final_decoded_string



if __name__ == "__main__":

    binary_string = generate_binary_string()
    print("\033[94m" + "The binary string is:\n" + '\033[1;37;0m' + binary_string)
    decode_binary = decode_binary(binary_string)
    print("\033[94m" + "The binary string properly decoded is: \n" + '\033[1;37;0m' + decode_binary)
    final_decoded_string = rle_decode(decode_binary)
    print("\033[94m" + "The brainfuck string is: \n" + '\033[1;37;0m' + final_decoded_string)
    flag = brainfuck.evaluate(final_decoded_string)
    print("\033[94m" + "The flag is:\n" + '\033[1;37;0m' + flag)