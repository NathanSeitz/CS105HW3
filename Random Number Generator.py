import random

def generationCreator(parents,offspring,counter):

    while counter <= 10:
        while parents > 0:
            theCoin = RandomGenerator()
            if theCoin <= 2:
                parents = parents - 1
                offspring = offspring + 2
            elif theCoin == 3:
                parents = parents - 1
        print('offspring gen',counter,':',offspring)
        #print('parents gen',counter,':',parents)
        counter = counter + 1
        parents = offspring
        offspring = 0
        

def RandomGenerator():
    theRandomBoi = random.randint(1,4)
    return theRandomBoi
def main():
    parents = 10
    offspring = 0
    generationCreator(parents,offspring,1)
    
main()
