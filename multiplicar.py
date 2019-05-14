class multiplicar(object):
    def __init__(self):
        pass
    def mult_aux(self,a,b):
        if isinstance (a,list)and (b,list):
            return self.mult(a,b,0,0,0,m,0)
        


    def mult(self,a,b,i,j,k,m,r):
        if i == len(a):
            return m
        elif j == len(a[0]):
            return self.mult(a,b,i+1,0,0,m,0)
        
        elif k == len(a[0]):
            m[i][j] = r
            return self.mult(a, b, i, j+1, 0, m, 0)
        else:
            r += a[i][k]*b[k][j]
            k+=1
            return self.mult(a, b, i, j, k, m, r)


a = [[1,2],[1,3]]
b = [[1,2],[3,1]]
m = [[0, 0], [0, 0]]
o = multiplicar()
print (o.mult_aux(a,b))
