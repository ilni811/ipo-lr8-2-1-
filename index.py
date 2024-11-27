import json

sum = 0
close = True

with open("dump1.json", "r", encoding="utf-8") as file:
    file_json = json.load(file)

def error(er):
    print("Возникла ошибка. " + er)

def choise():
    print('Выберите следующие пункты:')
    print(' 1. Вывести все записи\n', 
          '2. Вывести запись по полю.\n',
          '3. Добавить запись\n',
          '4. Удалить запись по полю\n', 
          '5. Выйти из программы\n')

def choice1():
    global sum
    for brand in file_json:
        print(f"""
             Код: {brand['id']} 
             Название бренда: {brand['brand_name']}
             Имя создателя: {brand['creator_name']}
             Продается ли в Беларуси: {brand["sold_in_Belarus"]}
             Стиль: {brand["Fashion"]}
             Где можно купить: {brand["Where_can_buy_it_cheap?"]}
             Страна: {brand["country"]}""")
    sum += 1

def choice2():
    global sum
    num = int(input("Введите id: "))
    found = False
    for brand in file_json:
        if num == brand['id']:
            found = True
            print(f"""
                 Код: {brand['id']} 
                 Название бренда: {brand['brand_name']}
                 Имя создателя: {brand['creator_name']}
                 Продается ли в Беларуси: {brand["sold_in_Belarus"]}
                 Стиль: {brand["Fashion"]}
                 Где можно купить: {brand["Where_can_buy_it_cheap?"]}
                 Страна: {brand["country"]}""")
            break
    if not found:
        print("Запись не найдена.")
    sum += 1

def choice3():
    global sum 
    number_brend = int(input("Введите id: "))
    counter = False
    for brand in file_json:
        if number_brend == brand['id']:
            counter = True
            break
    if counter:
        print("Введен существующий id")
    else: 
        name1_brand = input("Введите название бренда: ")
        name = input("Введите ФИО создателя бренда: ")
        sold = input("Продается ли в Беларуси?(да/нет) ")
        fashion = str(input("Какой стиль? "))
        where_buy = str(input("Где можно купить? "))
        where_country = str(input("В какой стране производится? "))
        new_brand = {
            "id": number_brend,
            "brand_name": name1_brand,
            "creator_name": name,
            "sold_in_Belarus": True if sold.lower() == "да" else False,
            "Fashion": fashion,
            "Where_can_buy_it_cheap?": where_buy,
            "country": where_country
        }
        file_json.append(new_brand)
        with open("dump1.json", "w", encoding="utf-8") as file:
            json.dump(file_json, file, ensure_ascii=False, indent=2)
        print("Запись успешно добавлена.")
    sum += 1

def choice4():
    global sum 
    id_choice = int(input("Введите номер поля(id): "))
    counter2 = False  

    for brand in file_json:
        if id_choice == brand['id']:
            file_json.remove(brand)  
            counter2 = True 
            break 

    if not counter2:
        print("Запись не найдена.")
    else:    
        with open("dump1.json", 'w', encoding='utf-8') as file:
            json.dump(file_json, file, ensure_ascii=False, indent=2)
            print("Бренд успешно удален.")
    sum += 1

def closes():
    global close
    print(f"Программа завершена. Количество выполненных операций с записями равно: {sum}" )
    close = False

def main():
    global close  
    while close:
        choise()
        choice = int(input("Выберите пункт меню (1-5): ")) 
        if choice == 1:
            choice1()
        elif choice == 2:
            choice2()
        elif choice == 3:
            choice3()
        elif choice == 4:
            choice4()
        elif choice == 5:
            closes()
        else:
            error("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")

main()
