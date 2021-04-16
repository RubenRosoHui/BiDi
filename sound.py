#!/usr/bin/python

import re
import cgi, cgitb

cgitb.enable( )  # enabled for CGI script troubleshooting
                 # script langauge/runtime errors are displayed and sent back to
                 # the browser
# set variable to check the sound is loud
warningdB = False
# open file
file = open("soundDB.txt", "r")
# check if the file is in open mode
if file.mode == 'r' :
    # read the file as a list of lines
    dBList = file.readlines()
    # close the file
    file.close

# get the last line of the file
currentdB = dBList[-1]
# search '*' if the temperature is higher than normal
match = re.search(r'[*]$', currentdB)
if match :
    warningdB = True
    # delete '*' mark before displaying value
    currentdB = currentdB.rstrip('*')

# web content
print("Content-type: text/html\n\n")
print("<html><head><meta http-equiv=\"refresh\" content=\"3\" /> \n")
print("</head><body align=\"center\">\n")

print("<p>\n")
print("<h2>Sound sensor</h2>\n")
print("<a href=\"../sound.html\" >\n")
print("<input type=\"submit\" value=\"Turn OFF\" style=\"width: 90%;")
print("font-size:20px;")
print("height: 100px; background: rgb(255, 137, 137);\"/>\n")
print("</a><br \>\n")
print("<h2>Current Sound: %s dB</h2>" %currentdB)
if warningdB == True :
    print("<h1 style=\"color:red;\">Sound is LOUD!!</h1>\n")
print("</p>\n")
print("</body></html>\n")