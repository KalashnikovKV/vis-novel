# Вы можете расположить сценарий своей игры в этом файле.


# Определение персонажей игры.
define e = Character('Somebody', color="#000000")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    with fade
    scene 11 telephone alarm
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 11 location room morning 
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 13 location room v2
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 13 location room v1
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 33 location dorm
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 31 location busstop dorm
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 33 location bus
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 33 location busstop uni
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 41 location university
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 51 location hallway 
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 61 location auditory
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 71 location basement
    with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

return


