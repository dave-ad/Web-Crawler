#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thur April 6 2023

@author: A.D
Web Crawler
"""

from urllib.request import urlopen

html = urlopen("https://www.wikipedia.org")
print(html.read())
# (urlopen(input()))