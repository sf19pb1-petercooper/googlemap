"""
BrooklynPublicLibraries.py

Map of every Brooklyn Library. No need to parse the data with conditionals.

Google Map
https://drive.google.com/open?id=19KXHctMdKnZXYDzemfLf4FEaAOznHP33&usp=sharing

"""

import sys
import csv   #Comma-Separated Values
import urllib.request

#Database is at
#https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/pi5s-9p35
url = "https://data.cityofnewyork.us/api/views/xmzf-uf2w/files/20a12ae9-bf36-4125-a38d-2287e8e9ec5d?download=true&filename=BPL_Locations.csv"

try:
    infile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error, file = sys.stderr)
    sys.exit(1)

#lines is a list of sequences of bytes.
lines = infile.readlines()
infile.close()

try:
    #Change lines into a list of strings of characters.
    lines = [line.decode("utf-8") for line in lines]
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

#print(lines[0], end = "") #1st line in the CSV file is a line of column headers.

for line in lines:          #Each time around the loop, line is a string.
    reader = csv.reader([line]) #[line] is a list containing one string
    fields = next(reader)       #fields is a list of strings.
    print(fields[0:4])
    # if (fields[26] == "10003"
    #     and fields[7] == "Alive"
    #     and fields[25].endswith("EAST 5 STREET")
    #     and int(fields[25].split(maxsplit = 1)[0]) >= 300):
    #     print(line, end = "")
