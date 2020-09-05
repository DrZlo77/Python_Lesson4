
#==================================================================================
'''
1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины
N случайных имен из первого списка (могут повторяться, можно взять значения: количество
 имен 20, N = 100, рекомендуется использовать функцию random);
'''

list_name_param = ["Семен","Петр","Александр","Николай","Василий","Сергей","Епифаний","Абрам","Фёдор"]
n = 100
random_name_list_param = []
import random

def random_name_list (name_list,n):
    """
    :param name_list: Список имен
    :param n: количество имен в новом списке
    :return: возвращаемы произвольный список
    """
    random_list_name = []
    for a in range (n):
        random_list_name.append(random.choice(name_list))
    global random_name_list_param
    random_name_list_param = random_list_name
    return random_list_name

print("Рандомный список имен: ", random_name_list(list_name_param,n))

#==================================================================================
'''
#2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
'''

def most_popular_name (random_list_name):
    """
    :param random_list_name: : радномный список имен
    :return: самое популярное имя
    """
    dict_name = {}
    print(random_list_name)
    for name in random_list_name:
        values_dict = dict_name.get(name,0)
        dict_name[name] = values_dict +1
    max = 0
    first_popular_name = ''

    print(dict_name)

    for elem_dict in dict_name.items():
        if elem_dict[1] > max:
           max = elem_dict[1]
           first_popular_name = elem_dict
    return first_popular_name

print("Самое популярное имя: ",most_popular_name(random_name_list_param))


#==================================================================================
'''
#3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F
'''

def rarity_letter (random_list_name):

    """
    :param random_list_name: радномный список имен
    :return: самая редкая буква в начеле имение
    """

    first_letters_list = []

    for name in random_list_name:
        first_letters_list.append(name[0])


    dict_latters = {}
    for latters in first_letters_list:
        latters_values = dict_latters.get(latters,0)
        dict_latters[latters] = latters_values + 1
    print(dict_latters)

    list_values = []

    for values in dict_latters.values():
        list_values.append(values)
    min_values = min(list_values)

    raruty_latterts_list = []


    for key,values in dict_latters.items():
        if values == min_values:
            raruty_latterts_list.append(key)
    return raruty_latterts_list


print("Самая редкая буква в начале имени: ",rarity_letter(random_name_list_param))

#==================================================================================
'''
PRO:
LIGHT + 
4.  В файле с логами найти дату самого позднего лога (по метке времени)
'''
def return_max_log ():
    '''
    :return: возвращаем последни лог
    '''
    file = open('log','r')
    text_log = file.read()
    text_log_splite = text_log.split('\n')
    time_list = []
    for elem in text_log_splite:
        if len(elem)>10:
            time_list.append(elem[:19]) # Если необходимо вернуть то метке времени именно в часах меняем на elem[10:19]
    max_time = max(time_list)
    print(max_time)

    for elem in text_log_splite:
        if len(elem)>10:
           if elem[:19] == max_time:
               max_time_log = elem
               return max_time_log
# Не элегантно, но работает ))
print("Последний лог в файле: ",return_max_log ())

