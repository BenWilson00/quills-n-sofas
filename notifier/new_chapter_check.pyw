from common_import import *

def get_chapter_count():
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

  return get_page(hdr).count("class=\'chapter_link\'")

def init(**kwargs):
  data = kwargs["data"]

  if "count" not in data:
    data["count"] = 0
  return data

def do_check(**kwargs):
  data = kwargs["data"]
  
  new_count = get_chapter_count()

  if data["count"] != new_count:
    notify("Utaan update", str(new_count-data["count"]) + " chapter update/s, most recent is " + str(new_count), 0)

  data["count"] = new_count

  return data