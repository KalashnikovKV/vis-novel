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
    scene location room
    e "TEXT"

    scene location dorm
    with fade
    e "TEXT"

    scene location busstop dorm
    with fade
    e "TEXT"

    scene location bus
    with fade
    e "TEXT"

    scene location busstop uni
    with fade
    e "TEXT"

    scene location university
    with fade
    e "TEXT"

    scene location hall
    with fade
    e "TEXT"

    scene location aud
    with fade
    e "TEXT"

    scene location basement
    with fade
    e "TEXT"

#    show eileen happy

    return
