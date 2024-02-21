my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': ''}
my_dict.update({'tuple': ('Cat', 'Dog', 'Turtle', 'Parrot', 'Ferret')})
my_dict.update({'list': [_ for _ in range(5)]})
my_dict.update({
    'dict': {'name': 'Alice Cooper', 'Born': '4.02.1948', 'Origin': 'Arizona',
             'Genre': 'Rock/Metal', 'Band': 'Alice Cooper'
             }})
my_dict.update({'set': {'black', 'white', 'blue', 'yellow', 'purple'}})
print(my_dict['tuple'][-1])
my_dict['list'].append(5)
my_dict['dict'].update({'i am a tuple': False})
my_dict['dict'].pop('Band')
my_dict['set'].add('crimson')
my_dict['set'].remove('yellow')
print(my_dict)
