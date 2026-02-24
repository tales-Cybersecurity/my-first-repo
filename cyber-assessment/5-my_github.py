#!/usr/bin/python3
import requests
import sys

r = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
print(r.json().get("id"))
