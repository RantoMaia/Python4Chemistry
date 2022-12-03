import random

#SOME ISSUES with Al + HCl --> AlCl3 + H2 
#Functions

def validInt(question):
    while True:
        try:
            n = int(input(question))
        except:
            print('Invalid Input!')
        else:
            return n
            break

def molDef(mol, molList, reagorprod):
    if reagorprod:
        for i in range(0,len(mol)-1):
            if mol[i].isupper():
                if mol[i+1].isnumeric():
                    if mol[i+2].isnumeric():
                        molList[mol[i]] = int(mol[i+1:i+3])
                        continue
                    else:
                        molList[mol[i]] = int(mol[i+1])
                    continue
                elif mol[i+1].islower():
                    if mol[i+2].isnumeric():
                        if mol[i+3].isnumeric():
                            molList[mol[i:i+2]] = int(mol[i+2:i+4])
                            continue
                        else:
                            molList[mol[i:i+2]] = int(mol[i+2])
                        continue
                    else:
                        molList[mol[i:i+2]] = 1
                        continue
                else:
                    molList[mol[i]] = 1
                    continue
            elif mol[i].isnumeric():
                continue
            elif mol[i].islower():
                continue  
    else:
        for i in range(0,len(mol)-1):
            if mol[i].isupper():
                if mol[i+1].isnumeric():
                    if mol[i+2].isnumeric():
                        molList[mol[i]] = 0-int(mol[i+1:i+3])
                        continue
                    else:
                        molList[mol[i]] = 0-int(mol[i+1])
                    continue
                elif mol[i+1].islower():
                    if mol[i+2].isnumeric():
                        if mol[i+3].isnumeric():
                            molList[mol[i:i+2]] = 0-int(mol[i+2:i+4])
                            continue
                        else:
                            molList[mol[i:i+2]] = 0-int(mol[i+2])
                        continue
                    else:
                        molList[mol[i:i+2]] = -1
                        continue
                else:
                    molList[mol[i]] = -1
                    continue
            elif mol[i].isnumeric():
                continue
            elif mol[i].islower():
                continue  
    
    return molList

def elementset(mol, elemSet = set()):
    for i in range(0,len(mol)-1):
        if mol[i].isupper():
            if mol[i+1].islower():
                elemSet.add(str(mol[i]+mol[i+1]))
            else:
                elemSet.add(str(mol[i]))
        else:
            continue

    return elemSet                

def coefficientList(ctrlSet, reagentDic, productDic):
    elDic = dict()
    ctrList = list(ctrlSet)
    k=0
    while k<len(ctrList):
        b = str(ctrList[k])
        elDic[b] = list()
        k += 1

    i = 0
    while i < len(ctrList):
        a = str(ctrList[i])
        for j in reagentDic:
            if ctrList[i] in reagentDic[j]:
                
                elDic[a].append(reagentDic[j][a])
            else:
                
                elDic[a].append(0)
        i += 1
    l = 0     
    while l < len(ctrList):
        a = str(ctrList[l])
        for j in productDic:
            if ctrList[l] in productDic[j]:  
                
                elDic[a].append(productDic[j][a])
            else:
                
                elDic[a].append(0)
        l += 1

    return elDic  
        
def rngList(a, b):

#Generate many numbers as the sum of reagents (a) and products (b)
    length = a + b
    tripl = list()
    count = 0
    while count < length :
        tripl.append(random.randint(1,20))
        count += 1

    return tripl

def sumLists(coeffList):
    summes = dict()
    
    for i in coeffList:
        summes[i] = sum(coeffList[i])
    
    listValues = list(summes.values())
    sumZero = all(item == 0 for item in listValues)
        
    
    return sumZero

def mltpLists(rndCoeff, coeffList, a, b):
    multipliedList = dict()
    length = a + b
    for i in coeffList:
        multipliedList[i] = list()
        count = 0

        while count < length:
            multipliedList[i].append(coeffList[i][count] * rndCoeff[count])
            count += 1
    return multipliedList

def minrndNum(randlist):

  minimum = min(randlist)
  divisions = list()
  found = True
  while found:
    for i in range(len(randlist)-1):
      divisions.append(randlist[i]%minimum)
    if (all(item == 0 for item in divisions)):
      found = False
      break
    elif minimum == 1:
      break
    else:
      minimum -= 1

  newRnd = list()
  count = 0

  while count < len(randlist):

    newRnd.append(int(randlist[count]/minimum))
    count +=1
  
  return newRnd      

#INPUT

nReag = validInt('Number of reagents: ')
nProd = validInt('Number of products: ')

reag = dict()
prod = dict()         
reagSet = set()
prodSet = set()
reagMol = list()
prodMol = list()

#Input all the reagents and products, functions will extract the information from the input string (element and stoichiometric coefficient)

for i in range(1,nReag+1):
    
    elem = str(input(f'Reagent {i}: ')+' ')
    reagList = dict()
    
    reagMol.append(elem)
    reag[i] = molDef(elem, reagList, True)
    elementset(elem, reagSet)


for i in range(1,nProd+1):

    elem = str(input(f'Product {i}: ')+' ')
    prodList = dict()
    prodMol.append(elem)
    prod[i] = molDef(elem, prodList, False)
    elementset(elem, prodSet)


#END INPUT SECTION


#Creation of list of coefficient

elemSet = reagSet.union(prodSet)

cfList = coefficientList(elemSet, reag, prod)

sumCtrl = sumLists(cfList)
rndNums = list()

# find the set of stoichiometric coefficient that balance the reaction

while sumCtrl != True:
    rndNums = rngList(nReag, nProd)
    cfmultiList = mltpLists(rndNums, cfList, nReag, nProd)
    sumCtrl = sumLists(cfmultiList)
    


# find if there is a set of smaller number that can balance the reaction

newRand = minrndNum(rndNums)

#OUTPUT

print('Equation balanced.')

countReag = 0
while countReag < len(reagMol):
    if countReag < ((len(reagMol)) - 1):
        print(f'{newRand[countReag]} {reagMol[countReag]}', end= '+ ')
    else:
        print(f'{newRand[countReag]} {reagMol[countReag]}', end= ' --> ')
    countReag +=1

countProd = 0
while countProd < len(prodMol):
    if countProd < (len(prodMol)-1):
        print(f'{newRand[(countProd + (len(reagMol)))]} {prodMol[countProd]}', end= '+ ')
    else:
        print(f'{newRand[(countProd + (len(reagMol)))]} {prodMol[countProd]}')
    countProd += 1