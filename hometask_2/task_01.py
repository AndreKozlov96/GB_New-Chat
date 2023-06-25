import csv
import re

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]


def get_data():
    for i in range(1, 4):
        filename = f'info_{i}.txt'
        with open(filename) as f:
            data = f.read()
            search_prod = re.compile('Изготовитель системы:\s*\S*')
            search_name = re.compile('Название ОС:\s*\S*\s\S*\s\S*')
            search_code = re.compile('Код продукта:\s*\S*')
            search_type = re.compile('Тип системы:\s*\S*')
            os_prod_list.append(search_prod.findall(data)[0].split()[2])
            os_name_list.append(f'{search_name.findall(data)[0].split()[3]} '
                                f'{search_name.findall(data)[0].split()[4]}')
            os_code_list.append(search_code.findall(data)[0].split()[2])
            os_type_list.append(search_type.findall(data)[0].split()[2])
            main_data.append(
                [str(i), os_prod_list[i - 1], os_name_list[i - 1], os_code_list[i - 1], os_type_list[i - 1]])
    return main_data


def write_to_csv(file_csv):
    get_data()
    with open(file_csv, 'w', encoding='utf-8') as f:
        data_write = csv.writer(f)
        data_write.writerows(main_data)


file_csv = '01_comp_data.csv'
write_to_csv(file_csv)
