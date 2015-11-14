for i in range(1,5+1):
	print sum([((idx+1) * 10**(x-1))*10**i for idx,x in enumerate(range(i-1,0,-1))]) + sum([10**(x-1)*x for x in range(1,i+1)])