# Домашнее задание "Секретарь".

# Необходимо реализовать следующие функции.
# get_name — функция. Принимает номер документа и выводит имя человека, которому он принадлежит.
# Если такого документа не существует, вывести “Документ не найден”.
# get_directory — функция. Принимает номер документа и выводит номер полки, на которой он находится.
# Если такой документ не найден, на полках вывести “Полки с таким документом не найдено”.
# add — функция, которая добавит новый документ в каталог и перечень полок.


documents = []
directories = {}

def get_name(doc_number):
    for numbers in documents:
        if doc_number in numbers["number"]:
            return numbers["name"]
    return None

def get_directory(doc_number):
    for shelf_numbers in directories.keys():
        num = directories[shelf_numbers]
        if doc_number in num:
            return shelf_numbers
    return None

def add(document_type, number, name, shelf_number):
    new_dict={"type": document_type, "number": number, "name": name}
    documents.append(new_dict)
    if shelf_number in directories.keys():
        directories[shelf_number].append(number)
    else:
        directories[shelf_number] = [number]
    return

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))