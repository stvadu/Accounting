def get_employees(file_name):
    print('getting employees...')
    with open(file_name, 'r') as f:
        list = []
        for line in f:
            list.append(line.strip())
    print('getting employees done')
    return list
