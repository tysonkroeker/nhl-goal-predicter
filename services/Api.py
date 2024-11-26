import sys
import numpy
import pandas
import urllib.request
import json
import pprint
import PySimpleGUI as sg


def makeRequest(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    f = urllib.request.urlopen(req)
    data = f.read()
    jsonData = json.loads(data)
    return jsonData