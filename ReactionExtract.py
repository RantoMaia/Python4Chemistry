#Input

reaction = list(input('Write a reaction in the form A + B --> C + D: '))
length = len(reaction)
structure = set()
structure = {' ','-','>','+'}


coefficient = list()
elem = set()
print(reaction)

for i in range(0,length):
    if reaction[i].isnumeric():
        coefficient.append(reaction[i])
        #Implement recognition of stoichiometrics
    elif reaction[i + 1].islower():
        elem.add(str(reaction[i] + reaction[i + 1]))
    elif reaction[i].islower():
        structure.add(reaction[i])
    else:
        elem.add(reaction[i])
        

result = elem.difference(structure)



print(elem)
print(result)