from common_import import *

def init(**kwargs):
  data = kwargs["data"]

  if "count" not in data:
    data["count"] = 0
  return data

def do_check(**kwargs):
  data = kwargs["data"]

  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

  page = urllib_get_page("http://www.fimfiction.net/story/290208/utaan", hdr)

  new_count = page.count("class=\'chapter_link\'")

  if data["count"] != new_count:
    response = notify("Utaan update", str(new_count-data["count"]) + " chapter update/s, most recent is " + str(new_count) + ". Would you like to read? Press Cancel to be reminded again later", MB_YESNOCANCEL|ICON_INFO)

    if response == SELECTED_YES:

      data["count"] = new_count

      # get first unread chapter url
      segment = page.split("chapter_link", data["count"] + 1)[-1][8:]
      url = "http://www.fimfiction.net" + segment[:segment.find("\"")]
      
      # update batch file with url
      chr_run_file = open("new_chapter_chromerun.bat", "r")
      string = chr_run_file.read().split("http://www.fimfiction.net")[0]
      chr_run_file.close()

      chr_run_file = open("new_chapter_chromerun.bat", "w")
      chr_run_file.write(string + url + "\"")
      chr_run_file.close()

      # run batch file
      Popen("new_chapter_chromerun.bat")

    elif response == SELECTED_NO:

      data["count"] = new_count

  return data