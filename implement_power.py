class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x==0:
            return 0
        res=1    
        while(n>0):
            if(n%2!=0):
                n-=1
                res=(res*x)%d
            n=n/2
            x=(x*x)%d
        return res    
            
