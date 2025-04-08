## Imports
from io import StringIO 
import sys

### Constants

### Functions & Classes
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

def ValaMath(a, b, c):
    x = range(a, b, c)
    for n in x:
        print(n, end=' ')

## List of Arguments (NOTE: Add arguments verification missing)
input = sys.argv[1]
output = sys.argv[2]
#print ('argument list', sys.argv)

## Enable first argument to reading values for function 'ValaMath' usage
f = open(input)
lines = f.read().split()
f.close()

## Output printing of the input file (NOTE: inputfile verification missing)
#print ('Content', lines)

## Enable second argument for saving output
s = open(output, "w")

## Collect objects from input file
Row1Nr1 = int(lines[0])
Row1Nr2 = int(lines[1])
LimitRow1 = int(lines[2])
Row2NR1 = int(lines[3])
Row2Nr2 = int(lines[4])
LimitRow2 = int(lines[5])

## Do print capturing from stdout for quick print capture
with Capturing() as output1:
    ValaMath(Row1Nr1, LimitRow1, Row1Nr1)

with Capturing() as output2:
    ValaMath(Row1Nr2, LimitRow1, Row1Nr2)

with Capturing() as output3:
    ValaMath(Row2NR1, LimitRow2, Row1Nr1)

with Capturing() as output4:
    ValaMath(Row2Nr2, LimitRow2, Row2Nr2)

## Do the magic for the ouput file and screen print with structure of function data and parameters
FirstRowMerge = ((str(output1).strip("[']")) + (str(output2).strip("[']")))
SecondRowMerge = ((str(output3).strip("[']")) + (str(output4).strip("[']")))
FirstRowNumbers = list(map(int, FirstRowMerge.split()))
SecondRowNumbers = list(map(int, SecondRowMerge.split()))
print(LimitRow1,":", sorted(FirstRowNumbers))
print(LimitRow2,":", sorted(SecondRowNumbers))
print(LimitRow1,":", sorted(FirstRowNumbers), file=s)
print(LimitRow2,":", sorted(SecondRowNumbers), file=s)

## Close ouptut file
s.close()
