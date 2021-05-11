class Solution:
    def maximumTime(self, time: str) -> str:
        
        def handleHour(hour):
            res = ''
            if hour[0] == '?':
               v = hour[1]
               if v == '?':
                    res += '23'
               else:
                    if int(v) <= 3:
                       res += '2'
                    else:
                        res += '1'
                    res += v
                    
            else:
                res += hour[0]
                if hour[1]=='?':
                    if int(res) == 2:
                        res += '3'
                    else:
                        res += '9'
                else:
                    res += hour[1]
                
            return res
        
        def handleMin(min):
            res = ''
            if min[0] == '?':
                res += '5'
                if min[1] == '?':
                    res += '9'
                else:                
                    res += min[1]
            else:
                res += min[0]
                if min[1] == '?':
                    res += '9'
                else:
                    res += min[1]
                
            return res
        
        timeparts = time.split(':')
        
        res = ''
        res += handleHour(timeparts[0])
        res += ":"
        res += handleMin(timeparts[1])
        
        return res
            
        
