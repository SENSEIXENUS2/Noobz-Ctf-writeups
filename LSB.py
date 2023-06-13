#! /usr/bin/env python
import subprocess
#Using Stegolsb to perform lsb on the wav file
wav_contents = subprocess.Popen("stegolsb wavsteg -r -i chall.wav -o output.txt -n 2 -b 23375;strings output.txt",stdout=subprocess.PIPE,shell=True)
#Grepping the flag from output.txt
grep_contents = subprocess.Popen("grep 'n00bz{'",stdin = wav_contents.stdout,stdout=subprocess.PIPE,shell=True)
output = grep_contents.communicate()
print(f"The flag is {output[0].decode()}")
