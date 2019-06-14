def insertionSort(ls):
	for n in range(1,len(ls)):
		item = ls[n]
		while(item<ls[n-1]):
			ls[n] = ls[n-1] #if item is less than previous items, shift them right by i unit
			if n==0:
				break
			n -= 1
		ls[n] = item
	return ls
			
if __name__=="__main__":
	ls = [2,7,4,1,1,5,3,10,0,23,9] 
	print(insertionSort(ls))