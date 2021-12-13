class Solution(object):
    def fizzBuzz(self, n):
        
        str = []
        
        for i in range(1 , n+1 , 1):
            if(i % 3 == 0):
                if(i % 5 == 0):
                    str.append("FizzBuzz")
                else:
                    str.append("Fizz")
            elif(i % 5 == 0):
                str.append("Buzz")
            else:
                str.append("{}".format(i))
        return str