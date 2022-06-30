def create_cook_book(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]
        dict_ = {}
        while len(lines) > 0:
            x = lines.pop(0)
            y = lines.pop(0)
            p = int(y)
            spisok = []
            lines_ = []
            for i in range(p):
                lines_.append(lines[i])
            for k in lines_:
                two = k.split(' | ')
                one = ['ingr', 'quant', 'measure']
                g = dict(zip(one, two))
                spisok.append(g)
            dict_[x] = spisok
            h = int(y) + 1
            del lines[0:h]
    return(dict_)

def shopping_list(dishes, person_count):
    j = create_cook_book('file.txt')
    ingridient_dict = {}
    for key in dishes:
        if key in j.keys():
            for m in j.get(key):
                x = m.pop('ingr')
                m['quant'] = int(m['quant'])
                ingridient_dict[x] = m
        else:
            print('this key is not in dishes')
    for s in ingridient_dict.values():
        s['quant'] *= person_count
    return(ingridient_dict)


print(create_cook_book('file_1.txt'))
print(shopping_list(['Запеченный картофель', 'Запеченный картофель'], 2))