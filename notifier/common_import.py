import urllib2
import ctypes
import os
import time
import shelve

def listdir(directory=None):
  files = []
  for file_ in (os.listdir(directory) if directory else os.listdir(os.getcwd())):
    files.append(file_)
  return files

def notify(title, text, style):
  ctypes.windll.user32.MessageBoxA(0, text, title, style)

def get_page(hdr):
  req = urllib2.Request("http://www.fimfiction.net/story/290208/utaan", headers=hdr)
  response = urllib2.urlopen(req)
  return response.read()

def find_element(text, page, abort_on_fail = True):
  index = page.find(text)

  if index == -1:
    if abort_on_fail:
      print "search failed - login issue or unexpected script"
      exit(1)

  return index

def get_full_int(index, parsed):
  int_string = ""

  while parsed[index].isdigit():
    int_string += parsed[index]
    index += 1

  return int(int_string)

def get_cookie(name, cookie_data):
  if name not in cookie_data:
    print "cookie " + name + " not found"
    print "cookies:", cookie_data
    print "terminating"
    exit(1)

  return cookie_data[name]["name"] + "=" + cookie_data[name]["value"]
