"""
Scraping Numbers from HTML using BeautifulSoup 
In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_283287.html (Sum ends with 97)
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

counter = 0
total = list()
url = input('Enter URL: ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
tags = soup('span')

for tag in tags:
    total.append(int(tag.string))
    counter = counter + 1
    
print("Counter:", counter)
print("Sum:", sum(total

"""
Output:
Counter: 50
Sum: 2197
"""
