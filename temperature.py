#!/usr/bin/python

import re
import cgi, cgitb

cgitb.enable( )  # enabled for CGI script troubleshooting
                 # script langauge/runtime errors are displayed and sent back to
                 # the browser
# set variable to check the temperature is high
warningTemp = False
# open file
file = open("temperatureDB.txt", "r")
# check if the file is in open mode
if file.mode == 'r' :
    # read the file as a list of lines
    tempList = file.readlines()
    # close the file
    file.close

# get the last line of the file
currentTemp = tempList[len(tempList)-1]
# search '*' if the temperature is higher than normal
match = re.search(r'[*]$', currentTemp)
if match :
    warningTemp = True
    # delete '*' mark before displaying value
    currentTemp = currentTemp.rstrip('*')

# web content
print("Content-type: text/html\n\n")
print("<html><head><meta http-equiv=\"refresh\" content=\"3\" /> \n")
print("</head><body align=\"center\">\n")

print("<p>\n")
print("<h2>Temperature sensor</h2>\n")
print("<a href=\"../temperature.html\" >\n")
print("<input type=\"submit\" value=\"Turn OFF\" style=\"width: 90%;")
print("font-size:20px;")
print("height: 100px; background: rgb(255, 137, 137);\"/>\n")
print("</a><br \>\n")
print("<h2>Current Temperature: %s &deg;C</h2>" %currentTemp)
if warningTemp == True :
    print("<h1 style=\"color:red;\">Temperature is HIGH!!</h1>\n")
print("</p>\n")
print("</body></html>\n")