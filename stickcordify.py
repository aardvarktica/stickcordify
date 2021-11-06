import argparse
from os import listdir
from os.path import getsize
from apng import APNG
from PIL import Image

def parseargs(version):
    '''Create parser object and populate with arguments'''
    parser = argparse.ArgumentParser(description='Image to Discord Sticker conversion Utility '+version)
    parser.add_argument("-f", "--file", help="File to convert", type=str)
    parser.add_argument("-a", "--autoclean", help="Automatically clean up tmp staging directory", type=bool)
    parser.add_argument("-c", "--compress", help="Attempt to compress files below Discord sticker filesize limit", type=bool)
    args = parser.parse_args()
    return args

def compress(img,filename, sizelim):
    outname = filename.split(".")[0]+"_compress.png"
    img.save(outname,optimize=True,quality=95)
    if sizelim < getsize(outname):
        print(f"**Warning:** File {outname} larger than Discord Sticker limit!")

def resize(img,dimlim):
    return imgcompress = img.resize(dimlim, Image.ANTIALIAS)

if __name__ == "__main__":
    version = "0.0.0"
    dimlim = (320,320) # 320x320 pixels max
    sizelim = 500000 # 500kb
    args = parseargs(version)
    filename = args.file
    img = Image.open(filename)
    fname, extension = filename.split(".")
    if extension == ".gif":
        flg = 0
        try:
            while 1:
                img.seek(flg)
                img = resize(img,dimlim)
                compress(img,f"{flg}.png",sizelim)
                flg+=1
        except EOFError:
            pass
    else:
        img = resize(img,dimlim)
        compress(img,f"{fname}_compress.png",sizelim)

