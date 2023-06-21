import json
from datetime import datetime


def load_operation(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def mask_card(str_):
    str_list = str_.split(' ')
    numb = str_list[-1]
    if not str_list[0] == 'Счет':
        return "Счёт " + numb[:4] + ' ' + numb[4:6] + '** **** ' + numb[-4:]
    else:
        return " ".join(str_list[:-1]) + ' **' + numb[-4:]


def filter_sort(data):
    items = []
    for item in data:
        if item.get('state') == "EXECUTED":
            items.append(item)
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items[:5]

def print_operation(operation):
    from_ = mask_card(operation.get('from', ""))
    to_ = mask_card(operation.get('to'))
    print(f'{operation["date"]} {operation["description"]}')
    print(f'{from_} -> {to_}')
    print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')


def form_date(data):
    new_date = datetime.fromisoformat(data)
    formated_date = new_date.strftime('%d.%m.%Y')
    return formated_date




