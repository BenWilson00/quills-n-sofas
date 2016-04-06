SetKeyDelay, -1
nBackspaces = 26
SendTable := {"0": "dammit fourths", "1": "foooouuuurrrrtths", "2": "I blame fourths", "3": "It's fourths' fault"}

count = 0
for key, value in SendTable
  count++
highestIndex := count - 1

!^f::

  Send, [Enter a number from 0-%highestIndex%]

  while true
  {
    For key, value in SendTable
    {
      if (GetKeyState(key))
      {
      Send, {backspace %nBackspaces%}%value%{Enter}
      Return
      }
    }
    if (GetKeyState("Escape"))
    {
    Return
    }
  }