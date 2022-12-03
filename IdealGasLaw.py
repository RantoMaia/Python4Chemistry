#Menu and input 

print('What variable do you want to calculate?')
print('[1] Pressure')
print('[2] Volume')
print('[3] Temperature')
print('[4] Number of moles')

rCost = 0.082

listOpt = ['Pressure', 'Volume', 'Temperature', 'Number of moles']

while True:
    opt = int(input('Select: '))
    if opt >= 1 and opt <=4:
        print(f'Selected: {listOpt[opt]}')
        break
    else:
        print('Invalid option')

if opt == 1:
    vol = float(input('Insert the volume: '))
    nMol = float(input('Insert the number of moles: '))
    temp = float(input('Insert the temperature: '))
    pres = (nMol*rCost*temp)/vol
    print(f'Pressure: {pres}')
elif opt == 2:
    pres = float(input('Insert the pressure: '))
    nMol = float(input('Insert the number of moles: '))
    temp = float(input('Insert the temperature: '))
    vol = (nMol*rCost*temp)/pres
    print(f'Volume: {vol}')
elif opt == 3:
    vol = float(input('Insert the volume: '))
    nMol = float(input('Insert the number of moles: '))
    pres = float(input('Insert the pressure: '))
    temp = (pres*vol)/(nMol*rCost)
    print(f'Temperature: {temp}')
elif opt == 4:
    vol = float(input('Insert the volume: '))
    temp = float(input('Insert the temperature: '))
    pres = float(input('Insert the pressure: '))
    nMol = (pres*vol)/(temp*rCost)
    print(f'Number of moles: {nMol}')