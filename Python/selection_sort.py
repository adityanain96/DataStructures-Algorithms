import math

def selectionSort(ls):	
	for n in range(0,len(ls)):		
		min = math.inf
		min_index = 0
		for i in range(n,len(ls)):	#this runs from index "n" to the end of the list		
			if ls[i] < min:				
				min = ls[i]				
				min_index = i		
		temp = ls[n]
		ls[n] = ls[min_index]
		ls[min_index] = temp
	return ls
	
	
if __name__=="__main__":
	ls = [2,7,4,1,5,3,10,0,23,9]
	print(selectionSort(ls))