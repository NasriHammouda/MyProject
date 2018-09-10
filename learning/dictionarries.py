super_villains = {'Fiddler': 'Isaac Bowin', 'Pied Piper': 'Thomas Peterson'}
print(super_villains['Fiddler'])
del super_villains['Fiddler']

super_villains['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villains))

print(super_villains.get('Pied Piper'))

print(super_villains.keys())

print(super_villains.values())