children = {'name': ['Nikita', 'Peter', 'Ivan', 'Danil'],
            'female': ['Malihin', 'Ivenko', 'Petrenko', 'Teslenko'],
            'age': [20, 23, 15, 10]}
while True:
    army_list = []
    free_list = []
    add = input('do u want to add someone?')
    if add == 'yes':
        children['name'].append(input('name: '))
        children['female'].append(input('female: '))
        children['age'].append(int(input('age: ')))
    for i in range(len(children['age'])):
        name = children['name'][i]
        female = children['female'][i]
        age = children['age'][i]
        if age >= 18:
            army_list.append({'name': name, 'female': female, 'age': age})
        else:
            free_list.append({'name': name, 'female': female,'age': age})
    else:
        print('army' + '->', army_list)
        print('free' + '->', free_list)

    next =(input('do u want to continue?'))
    if next.lower() != 'yes':
        print('army' + '->', army_list)
        print('free' + '->', free_list)
        break



