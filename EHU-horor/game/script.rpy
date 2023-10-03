# Игра начинается здесь:
define e = Character("Bus")
define nothing = Character("...")
define zhenya = Character("Женя")

label start:
    $ default_mouse = "default"

####################### 1 ACT ######################

    # $ renpy.movie_cutscene('videos/Bubble.ogv')
    # nothing "asdfasdas"
    # with fade

    stop music fadeout 1.5

    scene 11 telephone alarm
    nothing "Ранние подъёмы мне всегда давались с трудом. Сегодняшнее утро не стало исключением. Однако, именно этот день считается особенным в жизни каждого студента. Особенный, потому что первый."
    zhenya "нужно вставать, собираться"

    scene 11 location room morning with fade
    show screen buttons_11 
    show model_dust:
        xalign 0.0 yalign 0.9
        linear 30.0 xalign -0.3
        linear 30.0 xalign 0.0
        repeat
    nothing "Всего пару песен в наушниках из любимого плейлиста и вот я уже стою готовая перед зеркалом, морально настраиваю себя  на предстоящую учёбу."
    hide screen buttons_11

    scene 12 mirror with fade
    zhenya "Всё будет хорошо, всё будет хорошо."
    nothing "В последний раз взглянув на себя, я отошла от зеркала, готовая к выходу."

    scene 13 location room v2 with fade
    show screen buttons_13
    nothing "Закинув рюкзак на плечо, покинула комнату взглядом. Комната выглядела аккуратной и по-общажному уютной. Соседка Варя сменила позу, негромко что-то пробормотав во сне."
    zhenya "Интересно, сны у неё такие же странные, как и она сама? И почему она до сих пор спит.., у второго курса другое расписание?"
    nothing "Вздохнув, я вышла из комнаты, почти бесшумно закрыв за собой дверь."
    hide screen buttons_13

    # scene 13 location room v1 with fade
    # e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 2_location_dormitory with fade
    show 02_hero_01 with dissolve
    pause 0.5
    nothing "Асфальт на улице был по-прежнему мокрым, после ночного дождя. Осень давала о себе знать. Листва, опавшая с деревьев, прилипала к обуви, пока я шла к остановке до университета." with dissolve
    pause 0.5
    hide 02_hero_01
    show 02_hero_02 with dissolve
    pause 0.5
    zhenya "Погода такая же паршивая, как и настроение... С другой стороны, сегодня должно быть интересно, первый же день." with dissolve
    hide 02_hero_02


    scene 31 location busstop dorm with fade
    show 31_nps
    show 31_hero_01
    show 31_nps_01
    nothing "Серые улицы и недовольные лица людей - очень похоже на утро понедельника."
    hide 31_hero_01
    hide 31_nps_01
    show 31_hero_02
    show 31_nps_02
    zhenya "Главное сесть на нужный автобус и выйти на нужной остановке. Не хотелось бы потеряться в незнакомом городе и, тем более, опоздать на первую пару в году"
    hide 31_hero_02
    hide 31_nps_02

    scene 33 location bus with fade
    nothing "Незнакомые пейзажи сменяли друг друга, а непонятное волнение в груди наростало"
    zhenya "Ого, уже студентка. Ещё и в другой стране. А ведь, кажется, вчера только в школу пошла. Сколько сил потрачено для этого переезда. Годы в художке не прошли зря"
    nothing "Казалось, в автобусе время тянется бесконечно долго. Интересно, это из-за утренних пробок или внутреннего волнения."

    scene 33 location busstop uni with fade
    show model_bus:
        xalign -4.0 yalign 1.1
        linear 4.0 xalign 0.0
    zhenya "Завидев знакомые пейзажи за окном, я быстро поднялась и направилась к выходу."
    zhenya "Спасибо Варе, которая съездила со мной день назад сюда и показала дорогу до университета."

    scene 33 location busstop uni with fade
    show model_bus:
        pause 1.0
        xalign 0.0 yalign 1.1
        linear 3.0 xalign 4.0
        linear 5.0 xalign 10.0
    zhenya "Покинув автобус на нужной остановке, я направилась по заученному маршруту." with dissolve

    scene 41 location university with fade
    zhenya "По дороге я рассматривала местные дома и вывески магазинов и ресторанов. Не смотря на то, что была здесь ещё вчера, удавалось замечать много новых деталей. Архитектура в Старом городе заставляла невольно улыбаться."
    zhenya "Дорога до университета заняла меньше времени, чем я думала."

    scene 42 location universitys enter with fade
    show screen buttons_42 
    zhenya "Пришла, вроде, заранее, а людей всё равно немало уже"
    nothing "Решив не терять больше времени я вошла в здание."
    hide screen buttons_42


    scene 51 location hallway with fade
    show screen buttons_51 
    nothing "Войдя внутрь я принялась рассматривать всё, что меня окружало. Не смотря на то. что вчера я ездила с Варей сюда - внутрь мы не заходили. И теперь каждая деталь интерьера вызывала у меня любопытство."
    zhenya "А здесь довольно комфортно и отдохнуть есть где. Осталось найти аудиторию.."
    nothing "Пройдясь по коридору первого этажа я быстро отыскала нужную дверь. Она, как и остальные на этаже, была открыта."
    hide screen buttons_51

    scene 61 location auditory with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 63 location auditory table with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 71 location basement with fade
    show model_dust:
        xalign 0.0 yalign 0.0
        linear 10.0 xalign 0.1
        linear 10.0 xalign -0.1
        linear 10.0 xalign 0.1
        linear 10.0 xalign 0.0
        repeat
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 73 location basement aud with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

####################### 1 ACT ######################

return
