import random
    
def RandomGenerator(low, high):
    theRandomBoi = random.randint(low, high)
    return theRandomBoi

def main():
    number1 = int(input("What should the minimum possible value be? "))
    number2 = int(input("What should the maximum possible value be? "))
    RandomGenerator(number1, number2)
    
main()
