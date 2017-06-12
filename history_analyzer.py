#! /usr/bin/python3

import sqlite3
from collections import defaultdict
import matplotlib.pyplot as plt

username = 'abhipanda'
path_firefox = '/home/' + username + '/.mozilla/firefox/44gladgd.default/places.sqlite'
path_chromium = '/home/' + username + '/.config/google-chrome/Default/History'

conn = sqlite3.connect(path_firefox)
c = conn.cursor()
table_name = 'moz_places'
c.execute('SELECT * FROM ' + table_name)

# a list to hold the results
final_list = []

# for firefox browser
for item in c:
    # the https address is obtained in the form of https://www.domain/<info>
    # isolate the domain name by splitting on basis of /
    try:
        domain = str(item[1]).split('/')[2].replace('www.', '')
    except IndexError:
        domain = 'null'

    final_list.append(domain)
conn.close()


# for chromium browser
conn = sqlite3.connect(path_chromium)
c = conn.cursor()
c.execute('SELECT * FROM urls')
for item in c:
    # the https address is obtained in the form of https://www.domain/<info>
    # isolate the domain name by splitting on basis of /
    try:
        domain = str(item[1]).split('/')[2].replace('www.', '')
    except IndexError:
        domain = 'null'

    final_list.append(domain)
conn.close()

# a frequency dictionary for knowing the visit counts for each website
fq = defaultdict(int)
for site in final_list:
    fq[site] += 1

# sort according to counts in increasing order of frequency
sorted_list = sorted(fq, key = fq.get)
# filter out the last 14 elements
most_visited = sorted_list[-14:]

most_visited = most_visited[::-1]
left = [i for i in range(14)]

# plot a graph
plt.bar(left, [fq[i] for i in most_visited], tick_label = most_visited, width = 0.8, color = ['red', 'blue'])
plt.show()
