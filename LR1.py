# Датасет книг взят из открытых источников: https://data.mos.ru/opendata/7702155262-knigi-nominanty-i-pobediteli-literaturnyh-premiy-po-godam-nahodyashchiesya-v-kajdoy-gosudarstvennoy-publichnoy-biblioteke-goroda-moskvy

import pandas as pd
from tkinter import *

# "ID";"NominationYear";"Name";"Author";"PubYear";"AgeLimit";"Genre";"PublishingHouse";"LitPrizeName";"Nomination";"signature_date";"global_id";
raw = pd.read_csv('data1.csv', delimiter=';')

# Критерии книг по порядку выбора
criteries = ['AgeLimit', 'PubYear',   'Genre', 'Nomination', 'Name', 'Author']

print(raw[criteries])
age_limits = raw["AgeLimit"].unique()

root = Tk()
root.title('Выбор книги')

label = Label(text='Выбирайте книгу',
              font='Arial 14', padx=20)
label.grid(row=0, sticky='', column=0, columnspan=2)

field = Text(root, height=5, width=50, font='Arial 14', wrap=WORD)
field.grid(row=1, column=0, columnspan=2, padx=20, pady=6)

yes = Button(root, text='Нравится', height=1,
             font='arial 14', command=lambda: choice(True))
yes.grid(row=2, column=0, columnspan=1)

no = Button(root, text='Не нравится', height=1,
            font='arial 14', command=lambda: choice(False))
no.grid(row=2, column=1, columnspan=1)

ru_criteries = ['Возрастное ограничение', 'Год публикации',
                'Жанр', 'Номинация', 'Название книги', 'Имя автора']

stage = 0
step = 0

result = ru_criteries[stage] + ": " + raw[criteries[stage]].unique()[step]
field.insert(1.0, result)

preference = 'Вам подходит книга: '

preference = {

}


def choice(answer):
    global stage
    global step
    global preference
    global raw
    print(preference)

    try:
        if answer:
            if stage == len(criteries) - 1:
                preference[criteries[stage]] = str(
                    raw[criteries[stage]].unique()[step])
                show_result()
                return

            preference[criteries[stage]] = str(
                raw[criteries[stage]].unique()[step])

            raw = raw[raw[criteries[stage]] == raw[criteries[stage]].unique()[
                step]]

            print(raw)
            stage += 1
            step = 0
        else:
            step += 1

        result = ru_criteries[stage] + ": " + \
            str(raw[criteries[stage]].unique()[step])
    except:
        raw = pd.read_csv('data1.csv', delimiter=';')
        stage = 0
        step = 0
        result = "Мы не смогли подобрать для вас книгу. Пожалуйста, попробуйте снова\n" + \
            ru_criteries[0] + ": " + raw[criteries[0]].unique()[0]

    field.delete('1.0', END)
    field.insert(1.0, result)


def show_result():
    field.delete('1.0', END)
    result = 'Вам подходит:\nАвтор: ' + preference["Author"] + "\nКнига: " + \
        preference["Name"] + "\nГод: " + preference["PubYear"] + \
        "\nЖанр: " + preference["Genre"]
    field.insert(1.0, result)


root.mainloop()
