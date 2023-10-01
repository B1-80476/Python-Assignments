# Q-2) Computation class:
# 1 - Create a Coputation class with a default constructor (without parameters)
# allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial
# of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n
# integers 1 + 2 +3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in the Calculation class to test the
# primality of a given integer. Test this method.
# 4 - Create a method called testPrims() allowing to test if two numbers are prime
# Between them.
# 5 - Create a tableMult() method which creates and displays the multiplication
# table of a given integer. Then create an allTablesMult() method to display all
# the integer multiplication tables 1, 2, 3, ..., 9.

class Computation:

    def __init__(self):
        pass

    def factorial(self, num):
        self.num = num
        print(f"Factorial of {num} is :")
        fact = 1
        for index in range(1,num+1):
            fact = fact * index
        print(f"Factorial of {num} = {fact} ")
        print("*"*80)


    def sum(self,num):
        print("Sum function")
        self.num = num
        s = 0
        for index in range(1,num+1):
            s = index + s
        print(s)
        print("*" * 80)


    def testprim(self,num):
        self.num = num
        print(f"checking {num} prime or not")
        for index in range(2,num):
            if num % index == 0:
                print(f"{num} is Not prime")
                break
            else:
                print(f"{num} is Prime")
                break
        print("*" * 80)

    def testprims(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Range of prime numbers between {num1} & {num2}")
        l = []
        for index in range(num1, num2+1):
            for i in range(2,index):
             if index == 2:
                l.append(index)
                break
             elif index % i == 0:
                 print(f"{index} is Not Prime")
                 break
            else:
                l.append(index)
        print(f"Prime number {l}")
        print("*" * 80)


    def tablemult(self, mul):
        self.mul = mul
        print(f"Table of {mul}")
        for index in range(1,11):
            print(f"{self.mul} X {index} = {self.mul * index}\n")
        print("-"*80)
        print("*" * 80)

    def alltablesmult(self):
        print("Table 1 To nine")
        for index in range(1,10):
            for index1 in range(1,11):
                print(f"{index} X {index1} = {index1 * index}\n")
            print("-" * 80)
        print("*" * 80)







c = Computation()
c.tablemult(5)
c.alltablesmult()
c.sum(5)
c.factorial(5)
c.testprim(10)
c.testprims(10,100)