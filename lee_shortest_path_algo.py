dr = [-1,1,0,0]
dc = [0,0,-1,1]
def findShortestPathLength(mat, src, dest):

    N,M = len(mat) , len(mat[0])
    visit = set()

    q = [(src[0],src[1],0)]


    def isValid(x,y):
        return 0<=x<N and 0<=y<M and (x,y) not in visit

    def getPath(parent):
        path = []
        step = dest 
        while step!=src:
            path.append(step)
            step = parent[step]
        path.append(src)
        path.reverse()
        return path


    parent ={}
    while q:

        x,y,dist = q.pop(0)

        if x==dest[0] and y == dest[1]:
            return getPath(parent)
        val = mat[x][y]
        if (x,y) not in visit:
            visit.add((x,y))
            for i in range(4):
                xx = x + dr[i]*val
                yy = y + dc[i]*val
                if isValid(xx,yy):
                    q.append( (xx,yy,dist+1) )
                    parent[(xx,yy)] = (x,y)
    return -1


if __name__ == '__main__':
    
    mat = [
        [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
        [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
        [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
        [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
        [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
        [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
        [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
        [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
        [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
        [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
    ]
    N,M = len(mat),len(mat[0])
    src = (0, 0)
    dest = (N-1,M-1)
 
    path = findShortestPathLength(mat, src, dest)
    print(path)