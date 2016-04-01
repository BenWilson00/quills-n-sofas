ASCII_FIRST = 33
ASCII_FINAL = 126

opened = open("hotkey_list.txt", "w")
write_str = ""
for i in range(ASCII_FIRST, ASCII_FINAL+1):
  char = str(unichr(i))

  write_str += "~"
  if char == char.upper() and char != char.lower():
    write_str += "+"

  write_str += char

  write_str += "::\n  output .= \"" 

  if char == "!":
    write_str += "{!}"
  elif char == "\"":
    write_str += "\"\""
  else:
    write_str += char

  write_str += "\"\nReturn\n\n"

opened.write(write_str)

opened.close()