def introspection_info(obj):
# Тип объекта
    obj_type = type(obj).__name__

# Атрибут объекта
    attributes = dir(obj)

# Методы объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]

# Модуль, к которому объект принадлежит
    module = obj.__class__.__module__

# Словарь с информацией об объекте
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
    return info

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция строки
string_info = introspection_info('Класс')
print(string_info)

# Интроспекция списка
list_info = introspection_info([3, 10, 2.0, 0.5, 'Pyhton'])
print(list_info)