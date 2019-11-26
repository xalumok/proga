from linkedList import *
from generator import *
from iterator import *

def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

print("Input begin, end, step and EPS")
begin, end, step, EPS = input().split()

for x in begin, end, step, EPS:
	if (RepresentsFloat(x) == False):
		raise ValueError("Input values must be float")

begin = float(begin)
end = float(end)
step = float(step)
EPS = float(EPS)

iterList = LinkedList()
for x in Iterator(begin, end, step, EPS):
    iterList.push_back(x)
    
iterList.print()

genList = LinkedList()
for x in generator(begin, end, step, EPS):
    genList.push_back(x)
print()
genList.print()
