import json
import csv
from datetime import datetime
import os

def get_name():
    return input("Введите Ваше имя: ")

def convertor(objects, objects_name):
    jsonDict = dict()
    for id, object in enumerate(objects):
        jsonDict[f"{objects_name[id]}"] = object
    if not os.path.exists("soxhran.json"):
        with open("soxhran.json", 'w') as file:
            allJson = list()
            allJson.append(jsonDict)
            json.dump(allJson, file, indent=4)
    else:
        allJson = list()
        with open("soxhran.json", 'r') as file:
            allJson = json.load(file)
        allJson.append(jsonDict)
        with open("soxhran.json", 'w') as file:
            json.dump(allJson, file, indent=4)
    if not os.path.exists("soxhran.csv"):
        with open("soxhran.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(objects)
    else:
        rows = list()
        with open("soxhran.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        rows.append(objects)
        with open("soxhran.csv", 'w') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)




def spisok_first(steps):
    print("Добро пожаловать в игру!")
    print("Выберите действие:")
    print("1. Начать игру")
    print("2. Выйти из игры")
    print("3. Справка об игре")
    first = input()
    all_steps = steps
    if first == "1":
        all_steps.append(first)
        spisok2_one()
        oneIn = input()
        if oneIn == "1":
            all_steps.append(oneIn)
            spisok3_one()
            secondIn = input()
            if secondIn == "1":
                spisok4_one_one()
            elif secondIn == "2":
                spisok4_one_two()
            all_steps.append(secondIn)
        elif oneIn == "2":
            spisok3_two()
            first_In = input()
            all_steps.append(oneIn)
            if first_In == "1":
                spisok4_two_one()
            elif first_In == "2":
                spisok4_two_two()
            all_steps.append(first_In)
        elif oneIn == "3":
            spisok3_three()
            second_In = input()
            all_steps.append(oneIn)
            if second_In == "1":
                spisok4_three_one()
                all_steps.append(second_In)
            elif second_In == "2":
                all_steps.append(second_In)
                spisok4_three_two()
                three_In = input()
                if three_In == "1":
                    all_steps.append(three_In)
                    three_two_one()
                    four_In = input()
                    if four_In == "1":
                        all_steps.append(four_In)
                        three_two_one_one()
                    elif four_In == "2":
                        all_steps.append(four_In)
                        three_two_one_two()
                elif three_In == "2":
                    all_steps.append(three_In)
                    three_two_two()
    elif first == "2":
        print("Вы вышли из игры, до свидания")
        all_steps.append("ВЫХОД")
    elif first == "3":
        print(
            "Игра была выполнена студентом группы П50-3-22. По содержанию не обесуть, кал получился АХХА \n ______________________________")
        all_steps.append('справка')
        spisok_first(all_steps)
    return all_steps

def spisok2_one():
    print(
        "Ты находишься в загадочном замке и тебе нужно выбрать\nправильные действия, чтобы выбраться оттуда живым. Вот твои варианты:")
    print("1. Войти в темную комнату")
    print("2. Открыть старую дверь или идти вниз по крутой лестнице?")
    print("3. Пойти через запертую железную дверь или пролезть через узкую трубу?")

def spisok3_one():
    print(
        "Ты вошел в темную комнату. Перед тобой несколько дверей.\n На одной из них написано «Рай» на другой «Ад». Что выберешь?")
    print("1. Дверь Рай")
    print("2. Дверь Ад")

def spisok3_two():
    print(
        "Открыв старую деревянную дверь и спустившись вниз\nпо крутой лестнице, перед тобой предстает выбор в виду двух дверей:")
    print("1. Спутиться в подземный мир")
    print("2. Новый китайский автомобиль OMODA C5 в нищенской комплектации")

def spisok3_three():
    print("После того, как ты прошел через железную дверь и пролез через узкую трубу, перед тобой:")
    print("1. Инновационный костюм железного человека")
    print("2. Стать Стивом Джобсом")
    print("Что выберешь?")

def spisok4_one_one():
    print(
        "Открыв дверь, перед тобой оказалась большая лестница, \nведущая к большому величественному трону, на которой восседало что-то похожее на человека,\nно более больших размеров. «Оно» говорит тебе, ты обрел вечный покой")

def spisok4_one_two():
    print("Открыв дверь в \"АД\" из нее выливается раскаленная лава и ты сгораешь заживо..")

def spisok4_two_one():
    print(
        "Ты выбрал спуститься в подземный мир. При входе в мир, стоит раскидистый дуб,\nа на нем написанно, что ты лягушка. шикарный конец АХХА")

def spisok4_two_two():
    print(
        "Ты выбрал новое чудо китайского автомобилестроения,\nдо встречи в автосервисе через 5.000км со сгоревшей проводкой)")

def spisok4_three_one():
    what = "инновационный"
    who = "человека"
    message = f"Ты выбрал {what} костюм железного {who}. Теперь тебе не страшны *кхм* от твоей мамы, за то, что ты забыл купить гречку"
    print(message.upper())

def spisok4_three_two():
    print("Ты выбрал стать Стивом Джобсом. Какой жизненный путь ты выберешь")
    vibor = {"1. Создать компанию Apple", "2. Устроиться работать в мак"}
    print(vibor)

def one_one_two():
    print("Ты выбрал Вернуться в самое начало")

def three_two_one():
    print("Ты выбрал создать компанию Apple. Что ты хочешь выпускать под этим брендом?")
    stive = {"1": "1. Выпускать технику", "2": "2. Выпускать автомобили"}
    print(stive["1"])
    print(stive["2"])

def three_two_two():
    print(
        "Ты выбрал устроиться Макдоналдс. Теперь ты сдохнешь в одиночестве,\nпотому что второй половинки, работая в маке ты не найдешь лол")

def three_two_one_one():
    print(
        "Ты выбрал выпускать технику. В будущем твоя компания перерастет в\nцелую корпорацию, а ты станешь мультимиллиардером. У тебя будут:")
    chtobudet = ["деньги", "тачки", "админки"]
    print(chtobudet[1])

def three_two_one_two():
    print(
        "Ты выбрал выпускать автомобили. А как мы все знаем,\nотчественный автопром - это кринж, поэтому твоя компания будет приносить\nтебе копейки и ты сдохнешь от бедности")


if __name__ == "__main__":
    start = datetime.now()
    name = get_name()
    all_steps = spisok_first(list())
    end = datetime.now()
    dur = (end - start)
    objects = [str(start), name, all_steps, str(end), str(dur)]
    objects_name = ['start', 'name', 'steps', 'end', 'dur']
    convertor(objects, objects_name)

