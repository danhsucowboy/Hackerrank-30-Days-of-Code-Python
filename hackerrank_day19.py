class AdvancedArithmetic(object):
    def divisorSum(self,n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor = []
        for i in range(1,n+1):
            if n//i == 0:
                divisor.append(i)
                
        return sum(divisor)
        pass


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)