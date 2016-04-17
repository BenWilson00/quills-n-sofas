from common_import import *

def get_notification_count(cookie_data):
  fimfic_cookie = get_cookie("fimfiction_login", cookie_data)

  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Cookie' : fimfic_cookie}

  page = get_page(hdr)

  notifications = {}

  pm_index = find_element("mail-link new", page, False)

  if pm_index == -1:
    pms = 0
  else:
    pms = get_full_int(pm_index + 49, page)
    

  notifications["private messages"] = pms
 
  return notifications

def get_notification_str(notifications):
  text = ""
  for key in notifications:
    text += key + ": " + str(notifications[key]) + "\n"
  return text

def init(**kwargs):
  data = kwargs["data"]

  if "notifications" not in data:
    data["notifications"] = {"private messages" : 0} 

  return data
 
def do_check(**kwargs):
  data = kwargs["data"]
  cookie_data = kwargs["cookies"]

  notifications = get_notification_count(cookie_data)

  if reduce(lambda x, y: x and y, (notifications[key] for key in notifications)):

    notify("Ff notifications", get_notification_str(notifications), 0)
