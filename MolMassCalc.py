#Input 

#How many molecules?
molList = list()
masList = list()
lenList = list()
nMol = int(input('How many molecules?: '))

#Input molecules as SMILES
count = 1
while count<=nMol:
    mol = str(input(f'Type the molecule {count} as SMILES: '))
    leng = len(mol)
    molList.append(mol)
    lenList.append(leng)
    mas = 0
    masList.append(mas)
    count += 1

print(molList)

#Molar masses

masDic = {'C': 12, 'O': 16, 'H': 1}

for i in range(0,len(molList)):
    masList[i] = 0
    length = lenList[i]
    #Considering the molecule
    for j in range(0,lenList[i]):
    #Calculate the mass
        if molList[i][j] == 'C':
            if j == 0 or j == (length-1):
                masList[i] += masDic['C'] + 3
                #can be put condition to check d.bounds
            elif molList[i][j+1] == '(':
                masList[i] += masDic['C'] + 1
            else:
                masList[i] += masDic['C'] + 2
        #put condition to calc number of hydrogens
        elif molList[i][j] == 'O':
            if molList[i][j-1] == '(' and molList[i][j+1] == ')':
                masList[i] += masDic['O'] + 1
            else:
                masList[i] += masDic['O']
        #put condition to calc number of hydrogens
        elif molList[i][j] == 'H':
            masList[i] += masDic['H']
        else: 
            continue
print(masList)


