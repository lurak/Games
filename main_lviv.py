import game

Struyska = game.Room("Struyska")
Struyska.set_description("Вулиця Стрийська: Довга і протяжна вулиця, яка є в'їздом у Львів і у нашу подорож")

Koz = game.Room("Koz")
Koz.set_description("Вулиця Козильеицького: Місце, де розміщенний найкращий університет у світі - УКУ!")

Franka = game.Room("Franka")
Franka.set_description("Вулиця Франка: Вулиця названа на честь видатного українського поета")

Sahar = game.Room("Sahar")
Sahar.set_description("Вулиця Академіка Сахарова: місце, де ти зустрінеш багато студентів, адже тут є 'Фуршет'")

Zel = game.Room("Zel")
Zel.set_description("Вулиця Зелена: Вулиця біля якої є стадіон 'Україна'")

Krak = game.Room("Krak")
Krak.set_description("Вулиця Краківська: вулиця, яка знаходиться в центрі міста Лева")

Struyska.link_room(Koz, "схід")
Koz.link_room(Sahar, "схід")
Koz.link_room(Franka, "північ")
Koz.link_room(Struyska, 'захід')
Sahar.link_room(Koz, 'захід')
Franka.link_room(Zel, 'схід')
Franka.link_room(Koz, "південь")
Franka.link_room(Krak, 'північ')
Krak.link_room(Franka, 'південь')

Kav = game.Enemy("Кавалер", "Кавалер: Чоловік, який розважає жінку в товаристві, супроводить її під час прогулянки.")
Kav.set_conversation("Гей, не дивись на мою дівчину!")
Kav.set_weakness("каблук")
Franka.set_character(Kav)

Lotr = game.Enemy("Лотр", "Лотр: Негідник, розбійник, грабіжник.Фацет")
Lotr.set_conversation("Гє-гє, хто тут на районі!")
Lotr.set_weakness("пляшка")
Zel.set_character(Lotr)

Zbrui = game.Enemy("Збруй", 'Збруй: Розбійник, грабіжник.')
Zbrui.set_conversation("Шо дивишся, гроші давай")
Zbrui.set_weakness("порох")
Sahar.set_character(Zbrui)

Bat = game.Enemy("Батяр", "Батяр: Гульвіса, п'яничка, популярний у жінок брутальний чоловік кінця 19-початку 20 "
                          "століття")
Bat.set_conversation("Кх-кх")
Bat.set_weakness("алкодез")
Krak.set_character(Bat)

kab = game.Item("каблук")
kab.set_description("Певно, якась дівчина загубила цю туфельку")
Koz.set_item(kab)

bottle = game.Item("пляшка")
bottle.set_description("Хтось напевно забув цю пляшку біля 'Фуршету'")
Sahar.set_item(bottle)

por = game.Item("порох")
por.set_description("Ух, а на Краківській багато пороху...")
Krak.set_item(por)

al = game.Item("алкодез")
al.set_description("Чудовий препарат від похмілля")
Franka.set_item(al)

current_room = Struyska
backpack = []

dead = False
print("В цій грі є такі команди взяти, битися, говорити(для взаємодії) and схід,захід,північ,підвень для руху")
while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["північ", "південь", "схід", "захід"]:
        # Move in the given direction
        try:
            current_room = current_room.move(command)
        except KeyError:
            print("Ви не можете туди піти, бо там ремонтують дорогу!\n"
                  "Вибори ж на носі!")
    elif command == "говорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "битися":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("Чим будете битися?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Урааа, ви перемогли!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 4:
                        print("Вітання ви перемогли всіх ворогів!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Ох, як так? Ви програли")
                    print("Це кінець гри(")
                    dead = True
            else:
                print("Ви не маєте " + fight_with)
        else:
            print("Нема з ким битися, забіяко")
    elif command == "взяти":
        if item is not None:
            print("Ви поклали " + item.get_name() + " у ваш рюкзак")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Тут нема нічого! Все зубожіло!")
    else:
        print("я не знаю що це " + command)