#! /usr/bin/env python3
import pytesseract
import subprocess
#Extracting video frames withh ffmpeg
subprocess.call("ffmpeg -i flag.avi -vf 'select=eq(pict_type\,I)' -vsync vfr output_%d.png",shell=True)
preflag =[]
#Extracting Text from Images with Tessaract
for i in range(1,114):
    no = str(pytesseract.image_to_string(r'output_{}.png'.format(i)))
    print(f"Extracting from {i}:{no}")
    preflag.append(no)
print(len(preflag))
flag = ""
#Converting Binary to text
for i in preflag:
    i = str(i)
    i = int(i,2)
    i = chr(i)
    flag += i
print(flag)
    
