//USING RECURSION 
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        d=[]
        digits.sort()
      
        for ind,val in enumerate(digits):
            d.append([val,digits[0:ind]+digits[ind+1:]])
        res=[]
      
        def f1(l1):
            f1l1=[]
            ele=l1[0]
            it=l1[1]
            sum=ele*100
            for i in range(len(it)):
                t1=sum+(it[i]*10)
                for j in range(len(it)): 
                    if(i==j):
                        continue 
                    t2=t1+it[j]
                    if(t2%2==0):
                       f1l1.append(t2)
            return f1l1
        
        for i in range(len(d)):
            if(d[i][0]==0):
                continue
            res.extend(f1(d[i]))
          
        return sorted(list(set(res)))


//NORMAL APPROACH
class solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if i == j:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    num = digits[i]*100 + digits[j]*10 + digits[k]

                    if num % 2 == 0:
                        res.add(num)

        return sorted(res)



