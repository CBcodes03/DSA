class Solution(object):
        def isValid(self, s):
            d={'(':')','{':'}','[':']'}
            sta=[]
            for i in s:
                if i in d.keys():
                    sta.append(d[i])
                else:
                    if len(sta):
                        if sta[len(sta)-1] != i:
                            break
                        else:
                            sta.pop()
                    else:
                        return False
            if len(sta):
                return False
            else:
                return True
