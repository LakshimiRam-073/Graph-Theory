dr = [2,2,-2,-2,1,1,-1,-1]
dc = [-1,1,-1,1,2,-2,-2,2]
def shortest(N,src,des):
	board = N*N 
	visit = set()
	i,j = src
	
	path = {}
	desx,desy = des

	if i>=N or j>=N or desx >= N or desy >= N :
		return None

	q = [(i,j,0)]


	def isValid(x,y):
		if 0<=x<N and 0<=y<N and (x,y) not in visit:
			return True


	def pathReconstruct(path, src, des):
		pathList =[]
		step = des
		while step!=src:	
			pathList.append(step)
			step = path[step]
		pathList.append(src)
		for p in reversed(pathList):
			print(p,end=" ")
		print()


	while q:
		x,y,dist = q.pop(0)
		if desx == x and desy == y:
			pathReconstruct(path,src,des)
			return dist
		visit.add((x,y))
		for i in range(8):
			xx = x+dr[i]
			yy = y+dc[i]
			if isValid(xx,yy):
				q.append((xx,yy,dist+1))
				path[(xx,yy)] =(x,y)

	return -1



def main():
	N =6

	src = (5,0)
	des = (0,5)
	print(f"Shortest path from {src} to {des} is {shortest(N,src,des)}")



if __name__ == '__main__':
	main()