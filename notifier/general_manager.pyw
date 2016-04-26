from common_import import *

files = {name : 0 for name in map(lambda y: y.split(".")[0], filter(lambda x: x.rfind(".pyw") != -1, listdir()))}

del files["general_manager"]

for file in files:
  files[file] = __import__(file)

shelf = shelve.open("C:\Users\Ben Wilson\Desktop\python_scripts\\notifier\common_data")

for filename in files:
  if not shelf.has_key(filename):
    shelf[filename] = {}

  shelf[filename] = files[filename].init(data=shelf[filename])

shelf.close()

while True:
  time.sleep(60)
  shelf = shelve.open("C:\Users\Ben Wilson\Desktop\python_scripts\\notifier\common_data")
  for filename in files:
    shelf[filename] = files[filename].do_check(data=shelf[filename], cookies=shelf["cookies"])
  shelf.close()