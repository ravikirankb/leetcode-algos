class Solution(object):
    def multiply(self, num1, num2):
        numdict = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }

        stringdict = {v:k for k,v in numdict.items()}
        
        def getFactor(_range):
           fact = 1
           for i in range(1,_range):
              fact = fact * 10
           return fact

        val1,val2 = 0, 0 
        
        for i, n1 in enumerate(num1):
            _factor = getFactor(len(num1) -  i)
            val1 += numdict[n1] * _factor
            

        for i, n2 in enumerate(num2):
            _factor = getFactor(len(num2) -  i)
            val2 += numdict[n2] * _factor

        result,s = val1 * val2,''
        
        while result:
            s = stringdict[result%10] + s
            result = result//10
        return s if s else '0'
        
        
