class Solution:
    def fib(self, n: int) -> int:
        sum = 0 
        if (n == 0 or n == 1):
            return n
        else:
            sum = 1
            aux = 2
            array = [0, 1]
            while (n >= aux):
                sum = array[aux-2] + array[aux-1]
                array = array + [sum]
                aux = aux + 1
        return sum  