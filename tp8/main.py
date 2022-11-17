from displayCpu import *
import sort
from umons_cpu import cpu_time
from random import *


#For sorted list
def calculatesorted(fct, maxiter):
	result = []	
	count = 10
	while (count <= maxiter):
		t1 = []
		for i in range(count):
			t1.append(randint(0,count))
		count += 200
		result.append(cpu_time(fct, t1))
	return result

inserttime = calculatesorted(sort.insertion_sort, 1000)
selectiontime = calculatesorted(sort.selection_sort, 1000)
mergetime = calculatesorted(sort.merge_sort, 1000)

display = CpuPlot([200, 400, 600, 800, 1000])

display.prepare(inserttime, 'Tri par insertion')
display.prepare(selectiontime, 'Tri par selection')
display.prepare(mergetime, 'Tri par fusion')
display.draw()

input()
