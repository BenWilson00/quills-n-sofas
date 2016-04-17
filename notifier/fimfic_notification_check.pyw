from common_import import *

def get_notifications(cookie_data):
  fimfic_cookie = get_cookie("fimfiction_login", cookie_data)

  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Cookie' : fimfic_cookie}

  page = urllib_get_page("http://www.fimfiction.net", hdr)

  notifications = {}

  # private messages are handled differently to others
  startsearch = 20000
  pm_index = find_element("mail-link new", page[startsearch:], False)

  if pm_index == -1:
    pms = 0
  else:
    pms = get_full_int(pm_index + 49 + startsearch, page)
    
  notifications["private messages"] = pms

  startsearch = 15700
  index2 = find_element("var logged_in_user", page[startsearch:], False) + startsearch

  notifications["content"] = get_full_int(index2 + 71, page)
  notifications["meta"] = get_full_int(index2 + 103, page)
  notifications["social"] = get_full_int(index2 + 137, page)
  
  return notifications

def get_notification_str(notifications):
  text = ""
  for key in notifications:
    text += key + ": " + str(notifications[key]) + "\n"

  return text + "Do you want to view these notifications? Press no to mark notifications as read, but not on the website. Press cancel to be reminded again later."

def init(**kwargs):
  data = kwargs["data"]

  if "notifications" not in data:
    data["notifications"] = {"private messages" : 0} 

  return data
 
def do_check(**kwargs):
  data = kwargs["data"]
  cookie_data = kwargs["cookies"]

  notifications = get_notifications(cookie_data)

  if True in (notifications[key] > data["notifications"][key] for key in notifications):

    response = notify("Ff notifications", get_notification_str(notifications), MB_YESNOCANCEL|ICON_INFO)
    
    if response == SELECTED_YES:

      data["notifications"] = {key : 0 for key in notifications}

      Popen("fimfic_chromerun.bat")

    elif response == SELECTED_NO:

      data["notifications"] = notifications

  return data