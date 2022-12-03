#Input

molW = float(input('Molecular weight of the compound: '))
nElm = int(input('Number of elements in the compound: '))

elmPercList = dict()
elmMassList = dict()

for i in range(1,nElm+1):
    elem = str(input(f'Element {i}: '))
    elmPercList[elem] = None
    elmMassList[elem] = None



for i in elmPercList:

    perc = float(input(f'Percentage of {i}: '))
    elmPercList[i] = perc
    atms = float(input(f'Atomic mass of {i}: '))
    elmMassList[i] = atms

#END input section

#Calc Ratio Percentages over Masses
rtElm = dict()

for i in elmPercList:
    rt = elmPercList[i]/elmMassList[i]
    rtElm[i] = rt

#Set minimum ratio

minRatio = min(rtElm, key=rtElm.get)

#calculate element coefficients
cElm = dict()
for i in rtElm:
    coefElm = int(rtElm[i]/rtElm[minRatio])
    cElm[i] = coefElm

#EMPIRICAL FORMULA

for i in cElm:
    if cElm[i] != 1:
        print(f'{i}{cElm[i]}', end='')
    else:
        print(f'{i}', end='')

print('')

#CALC MOLECULAR FORMULA
#calc weight of the empirical formula

wEmp = 0

for i in cElm:
    wEmp += cElm[i] * elmMassList[i]

#Molecular ratio

molRatio = int(molW/wEmp)

#Molecular coefficient

cMol = dict()

for i in cElm:
    molCoeff = molRatio*cElm[i]
    cMol[i] = molCoeff

#Print Molecular Formula

for i in cMol:
    if cMol[i] != 1:
        print(f'{i}{cMol[i]}', end='')
    else:
        print(f'{i}', end='')

print('')

