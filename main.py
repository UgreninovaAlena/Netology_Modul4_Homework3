from logger import get_log_to, get_log_to_file
import os

@get_log_to
def refactor_list(my_list):
    print('Задание 5. Приобразование списка')
    steps = len(my_list)
    vlog = {my_list[steps-2] : my_list[steps-1]}
    set_result={}
    steps = steps - 2
    while steps > 0:
        set_result[my_list[steps-1]] = vlog
        vlog = set_result
        set_result={}
        steps = steps-1
    set_result = vlog
    print(set_result)
    return set_result

@get_log_to_file('log.txt')
def refactor_list_logs_into_log_txt(my_list):
    print('Задание 5. Приобразование списка')
    steps = len(my_list)
    vlog = {my_list[steps-2] : my_list[steps-1]}
    set_result={}
    steps = steps - 2
    while steps > 0:
        set_result[my_list[steps-1]] = vlog
        vlog = set_result
        set_result={}
        steps = steps-1
    set_result = vlog
    print(set_result)
    return set_result


print('Введите список: ')
my_list = list(map(str, input().split()))
print(my_list)
refactor_list(my_list)
refactor_list_logs_into_log_txt(my_list)