import os

def create_dict(folder_name):
    a = os.path.join(os.getcwd(), folder_name)
    dict = {}
    for i in os.listdir(a):
        with open(os.path.join(os.getcwd(), folder_name, i), encoding='utf-8') as read_list:
            dict[i] = read_list.readlines()
    return dict

def get_key(value, folder_name):
    dict_ = create_dict(folder_name)
    for k, v in dict_.items():
        if v == value:
            return k



def w_fin_file(fin_file_name, folder_name):
    with open(fin_file_name, 'w', encoding='utf-8') as new_file:
        dict_ = create_dict(folder_name)
        sorted_list = sorted(dict_.values(), key=len)
        for line in sorted_list:
            new_file.write(get_key(line, folder_name))
            new_file.write('\n')
            new_file.write(str(len(line)))
            new_file.write('\n')
            new_file.write(str(''.join(line)))
            new_file.write('\n')
            new_file.write('\n')

w_fin_file('fin_file.txt', 'folder_1')