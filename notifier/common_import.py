import urllib2, ctypes, os, time, shelve, webbrowser
from subprocess import Popen

MB_YESNOCANCEL = 0x03
MB_YESNO = 0x04
ICON_INFO = 0x40

SELECTED_YES = 0x06
SELECTED_NO = 0x07
SELECTED_CANCEL = 0x02

def pause(reason=''):
  if reason != '': raw_input('Paused with message : \n'+reason + '\nPress enter to resume.')
  else: raw_input('Paused. Press enter to resume.')

def listdir(directory=None):
  files = []
  for file_ in (os.listdir(directory) if directory else os.listdir(os.getcwd())):
    files.append(file_)
  return files

def notify(title, text, flags):
  return ctypes.windll.user32.MessageBoxA(0, text, title, flags)

def urllib_get_page(page, hdr):
  req = urllib2.Request(page, headers=hdr)
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
