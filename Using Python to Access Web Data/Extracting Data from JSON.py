"""
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_283290.json (Sum ends with 44)
"""

import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter :")
uh = urllib.request.urlopen(url).read()

print("Retrieving:", url)
print('Retrieved', len(uh), 'characters')

info=json.loads(uh)

rs=0
count=0
for item in info['comments']:
    rs= rs + item['count']
    count = count + 1
print("Sum:",  rs)
print("Count:", count)

"""
Output:
Retrieving: http://py4e-data.dr-chuck.net/comments_283290.json
Retrieved 2733 characters
Sum: 2844
Count: 50
"""
