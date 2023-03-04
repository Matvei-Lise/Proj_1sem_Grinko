# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
# фразу «Министерства образования Ростовской области», посчитать количество
# произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
# «50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re

def func_open(text):
    telephone = re.findall(r"8\d\d\d\d\d\d\d\d03", text)
    telephone += re.findall(r"8\d\d\d\d\d\d\d\d50", text)

    tel_g = re.split(r"\n", text)
    lst = []
    count_change = re.findall("«Горячая линия»", text)
    for k in tel_g:
        if re.findall("ЕГЭ|ГИА", k):
            lst += re.findall(r"\d\d\d\d\d\d\d\d\d\d\d", k)
        elif re.findall("«Горячая линия»", k):
            pass

    return len(telephone), lst, len(count_change)


with open("hotline.txt", encoding="UTF-8") as f1:
    f2 = f1.read()
    lst = "".join(f2)
    telephones, tel_gg, count_changes = func_open(f2)
    print(f"Количество номеров телефонов - (03, 50): {telephones}\nНомера тел. горячих линий: {tel_gg}")
    print(f"Количество изменений: {count_changes}")

with open("hotline.txt", "w", encoding="UTF-8") as f2:
    f3 = f2.write(re.sub("«Горячая линия»", "Горячая линия Министерства образования Ростовской области", lst))