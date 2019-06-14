def bubbleSort(ls):	
	for n in range(0,len(ls)):
		pdb.set_trace()
		sorted = True #consider that list is already sorted
		for i in range(0,len(ls)-(n+1)):
			if ls[i] > ls[i+1]:
				sorted = False #list is not sorted
				#swap items
				temp = ls[i+1]
				ls[i+1] = ls[i]
				ls[i] = temp
		if sorted==True: #list is already sorted, exit the loop
			return ls
	return ls
	
if __name__=="__main__":
	ls = [2,7,4,1,5,3,10,0,23,9] 
	print(bubbleSort(ls))