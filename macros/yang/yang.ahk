SetKeyDelay, -1
anthonies := ["our lord and saviour ", "the great Anthony ", "supreme leader Tony ", "our glorious leader ", "the one true Yang "]

count := -1
for index, value in anthonies
  count++

::tony::
::yang::
::anthony::

rand := 0
for index, value in anthonies
{
  Random, rand, 0, count

  if (rand = 0)
  {
  Send, %value%
  Return
  }
}
