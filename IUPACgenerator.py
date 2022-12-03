#INPUT

mol = str(input('Type the molecule as SMILES: ')).upper()

# Prefix ---> Number of carbons

pre = mol.count('C')

print(pre)

if pre == 1:
  prefix = str('met')
elif pre == 2:
  prefix = str('et')
elif pre == 3:
  prefix = str('prop')
elif pre == 4:
  prefix = str('but')
elif pre == 5:
  prefix = str('pent')
elif pre == 6:
  prefix = str('hex')
elif pre == 7:
  prefix = str('ept')
elif pre == 8:
  prefix = str('oct')
elif pre == 9:
  prefix = str('non')
elif pre == 10:
  prefix = str('dec')
else:
  print('Too many carbons')

print(prefix)

#Infix ---> number of d bonds

if 'C=C' in mol:
  dBonds = mol.count('C=C')
  if dBonds == 1:
    infix = str('en')
  elif dBonds == 2:
    infix = str('adien')
  else:
    print('Too many double bonds.')
else:
  infix = str('an')

print(infix)


#Suffix --> functional group

if '(C=O)OH' in mol:
  suffix = str('oic acid')
elif '(C=O)H' in mol:
  suffix = str('al')
elif 'OH' in mol:
  suffix = str('ol')
else:
  suffix = str('e')

print(suffix)

#output

print(prefix+infix+suffix)