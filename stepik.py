
# # Бесконечный ввод
# import sys

# for line in sys.stdin:
#     print(line.strip()[::-1])

# with open('products.csv', encoding='utf-8') as file:
#     data = file.read()
#     for line in data.splitlines():
#         print(line.split(','))

# with open('products.csv', encoding='utf-8') as file:
#     data = file.read()
#     table = [r.split(',') for r in data.splitlines()]
#     del table[0]                                        # удаляем заголовок
#     table.sort(key=lambda item: int(item[1]))
#     for line in table[:5]:
#         print(line)
    
# with open('products.tsv', encoding='utf-8') as file:
#     data = file.read()
#     table = [r.split('\t') for r in data.splitlines()]
#     del table[0]
#     table.sort(key=lambda item: int(item[1]))
#     for line in table[:5]:
#         print(line)

# table = [['keywords', 'price', 'product_name'],
# ['Садовый стул', '1699', 'ВЭДДО'],
# ['Садовый стул', '2999', 'ЭПЛАРО'],
# ['Садовый табурет', '1699', 'ЭПЛАРО'],
# ['Садовый стол', '1999', 'ТЭРНО'],
# ['Складной стол', '7499', 'ЭПЛАРО'],
# ['Настил', '1299', 'РУННЕН'],
# ['Стеллаж', '1299', 'ХИЛЛИС'],
# ['Кружка', '39', 'СТЕЛЬНА'],
# ['Молочник', '299', 'ВАРДАГЕН'],
# ['Термос для еды', '699', 'ЭФТЕРФРОГАД'],
# ['Ситечко', '59', 'ИДЕАЛИСК'],
# ['Чайник заварочный', '499', 'РИКЛИГ'],
# ['Кофе-пресс', '699', 'УПХЕТТА'],
# ['Чашка с блюдцем', '249', 'ИКЕА'],
# ['Кружка', '249', 'ЭМНТ']]


# from collections import namedtuple

# Game = namedtuple('Game', 'name developer publisher')

# ExtendedGame = namedtuple('ExtendedGame', Game._fields + ('release_date', 'price'))

# print(ExtendedGame._fields)

#json

# import json

# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

# countries_json = json.dumps(countries, indent='   ', separators=(',', ' - '), sort_keys = True)
# print(countries_json)



# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }

# data_json = dumps(words, skipkeys = True)
# print(data_json)


# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "gaolkeeper": "M. Neuer", "league_position": 1}

# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "gaolkeeper": "M. Ter Stegen", "league_position": 7}

# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "gaolkeeper": "D. De Gea", "league_position": 8}
# all_football_comand = club1, club2, club3
# with open('data_json', "w") as file:
#         json.dump(all_football_comand, file, indent = "   ")


# specs = {
#          ['Модель']: 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }

# specs_json = json.dumps(specs, ensure_ascii=False, indent = "   ")
# print(type(specs_json))


# def is_correct_json(data_for_json):
#         try:
#                 json.loads(data_for_json)
#         except Exception:
#                 return False
#         else:
#                 return True


# data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

# print(is_correct_json(data))


# values_json = {"size": 36, "style": "bold", "name": "text1", "alignment": "center"} 
# json_dict = json.dumps(values_json, ensure_ascii=False, indent=0)
# for i in json_dict:
#         print(i)


# values_json = ",".join(values_json.replace('"#$%&\()*+-./;<=>?@[\\]^_`{|}~\'').rstrip())
# json_dict = json.dumps(values_json, ensure_ascii=False)
# print(json_dict)

# for line in sys.stdin:
#     print(line.strip('\n').replace('"#$%&\()*+-./;<=>?@[\\]^_`{|}~\'').split(","))

# data = [line.strip() for line in sys.stdin]

# json_data = []

# with open('list.json', encoding='utf8') as file:
#         data = json.load(file)
#         for i in data:
#                 if type(i) == str:

#                         json_data.append(i + "!")

#                 elif type(i) == list:
#                         json_data.append(i * 2)

#                 elif type(i) == bool:
#                         if i is True:
#                                 json_data.append(False)
#                         else:
#                                 json_data.append(True)
#                 elif type(i) == int:
#                         json_data.append(i + 1)
#                 elif type(i) == dict:
#                         i.update({"newkey": None})
#                         json_data.append(i)
#                 elif i is None: 1+1

# with open('updated_data.json', 'w', encoding='utf8') as file:
#     json.dump(json_data, file)


# with open ('data1.json', encoding = 'utf8') as file1:
#     dict1 = json.load(file1)

# with open('data2.json', encoding = 'utf8') as file2:
#     dict2 = json.load(file2)


# dict = dict1 | dict2


# with open('data_merge.json', 'w', encoding='utf8') as file:
#     json.dump(dict , file)

# my_set = dict()
# with open('people.json', encoding = 'utf-8') as file:
#     peoples = json.load(file)

# my = {k:None for i in peoples for k in i.keys()}

# for i in peoples:
#         for k in i.keys():
#                 my_set [k]="None"
# for i in peoples:
#         my_set.append(my | i)

# with open('updated_people.json', 'w', encoding='utf8') as file:
#      json.dump(peoples , file)


# with open ('students.json', encoding = 'utf-8') as file:
#     students = json.load(file)
    
# data = []
# for i in students:
#         if i['age'] > 17 and i ['progress'] > 74:
#                 data.append([i['name'], i['phone']])

# data.sort()            
# columns = ['name', 'phone']


# with open('data.csv', 'w', encoding='utf-8', newline='') as file1:
#     writer = csv.writer(file1)
#     writer.writerow(c['name', 'phone'])
#     for row in data:
#         writer.writerow(row)




# with open('students.json') as file:
#     students = json.load(file)
#     result = []
#     for student in data:
#         if student['age'] >= 18 and student['progress'] >= 75:
#             result.append([student['name'], student['phone']])
#     result.sort()
        
# with open('data.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'phone'])
#     writer.writerows(result)


# with open( 'food_services.json', encoding = 'utf-8') as file:
#     food_services = json.load(file)
# district = {}
# operatingCompany = {}
# for i in food_services:
#     district[i['District']] = district.get(i['District'],0) + 1
#     if i['IsNetObject'] == 'да':
#         operatingCompany[i['OperatingCompany']] = operatingCompany.get(i['OperatingCompany'],0) + 1
        
# print(*sorted(district.items(), key = lambda x: x[1], reverse = True)[0], sep = ': ')
# print(*sorted(operatingCompany.items(), key = lambda x: x[1], reverse = True)[0], sep = ': ')

# with open('countries.json', encoding='utf-8') as f, open('religion.json', 'w') as f2:
#     base = json.load(f)
#     res = {}
#     for i in base:
#         res.setdefault(i['religion'], []).append(i['country'])
#     json.dump(res, f2, indent='   ')



# with open('playgrounds.csv', encoding='utf-8') as csv_file:
#     playgrounds = csv_file.read()
#     read_playgrounds = [i. split(';') for i in playgrounds.splitlines()]
#     del read_playgrounds[0]
#     dict = {}
#     for ObjectName, AdmArea, District, Address in read_playgrounds:
#         dict.setdefault(AdmArea, {}).setdefault(District,[]).append(Address)

# with open('addresses.json', 'w', encoding='utf-8') as file:
#     json.dump(dict, file, ensure_ascii=False, indent = "   ")

# data = defaultdict()

# print(data['phone'])





# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
# data.sort(key = lambda x: x[0])
# final = {}
# for i in data:
#     key = i[0]
#     value = i[1]
#     final[key] = final.get(key, 0) + value
# for i in final:
#     key = i[0]
#     value = i[1]
#     print(f'{key}: ${value}')


# from collections import defaultdict

# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]

# result = defaultdict(int)

# for key, value in data:
#     result[key] += value

# for key, value in sorted(result.items()):
#     print(f'{key}: ${value}')

# from collections import Counter

# most_no_popular_word = Counter(input().lower().split()).most_common()[::-1]
# final=[]
# for i in most_no_popular_word:
#     if i[1] == most_no_popular_word[0][1]:
#         final.append(i[0])

#     else:
#         break

# print(*sorted(final), sep = ",")

# st=input().lower().split()
# count = Counter(st).most_common()
# count_min = [i[0] for i in count if count[-1][-1] == i[-1]]
# print(*sorted(count_min),sep=", ")

from collections import Counter

most_popular_word = Counter(input().lower().split()).most_common()
final =[]
for i in most_popular_word:
    if i[1] == most_popular_word[0][1]:
        final.append(i[0])
    else:
        break
        
final.sort(key=len)
                       
print(final)