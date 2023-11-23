#!/usr/bin/env python3

import sys

url = sys.argv[1]

scheme = ""
host = ""
port = ""
path = ""
query = ""
fragment = ""

token = url.split("://")
scheme = token[0]
url = token[1]

token = url.split("#")

if len(token) > 1:
  fragment = token[1]

url = token[0]
token = url.split("?")

if len(token) > 1:
  query = token[1]

url = token[0]

token = url.split("/")
path = token[0]
url = token[1]

print(path, url)

"""print("scheme:", scheme)
print("host:", host)

if len(port) > 0:
  print("port:", port)

print("path:", "/" + path)

if len(query) > 0:
  print("query-string:", query)

if len(fragment) > 0:
  print("fragment:", fragment)"""
