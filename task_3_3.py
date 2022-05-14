

def thesaurus(*args):
    new = {}
    for el in args:
        first_letter = el[0]
        new[first_letter] = new.get(first_letter, []) + [el]
    return new


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
