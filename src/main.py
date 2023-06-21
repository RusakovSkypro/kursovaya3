
from src.utils import load_operation, filter_sort, mask_card, print_operation, form_date

file_path = 'operations.json'

def main():
    data = load_operation(file_path)
    sorted_operations = filter_sort(data)
    for operation in sorted_operations:
        operation['date'] = form_date(operation['date'])
        print_operation(operation)


if __name__ == '__main__':
    main()
