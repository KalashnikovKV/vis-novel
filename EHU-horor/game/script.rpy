# Игра начинается здесь:
define e = Character("Bus")
define nothing = Character("...")
define zhenya = Character("Женя")
image model_bus = "33 location busstop model bus"
image model_monk = "/images/1_act/hero/AI PNG/ai figure 02 basement 1.png"

label start:

####################### 1 ACT ######################

    # $ renpy.movie_cutscene('videos/Bubble.ogv')
    # nothing "asdfasdas"
    with fade
    scene 11 telephone alarm
    nothing "Ранние подъёмы мне всегда давались с трудом. Сегодняшнее утро не стало исключением. Однако, именно этот день считается особенным в жизни каждого студента. Особенный, потому что первый."
    zhenya "нужно вставать, собираться"

    scene 11 location room morning with fade
    nothing "Всего пару песен в наушниках из любимого плейлиста и вот я уже стою готовая перед зеркалом, морально настраиваю себя  на предстоящую учёбу."
    
    scene 12 mirror with fade
    zhenya "Всё будет хорошо, всё будет хорошо."
    nothing "В последний раз взглянув на себя, я отошла от зеркала, готовая к выходу."

    scene 13 location room v2 with fade
    # show valiaetca
    nothing "Закинув рюкзак на плечо, покинула комнату взглядом. Комната выглядела аккуратной и по-общажному уютной. Соседка Варя сменила позу, негромко что-то пробормотав во сне."
    zhenya "Интересно, сны у неё такие же странные, как и она сама? И почему она до сих пор спит.., у второго курса другое расписание?"
    nothing "Вздохнув, я вышла из комнаты, почти бесшумно закрыв за собой дверь."

    # scene 13 location room v1 with fade
    # e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 2_location_dormitory with fade
    show hero walk_location dormitory_01 with dissolve
    pause 0.5
    nothing "Асфальт на улице был по-прежнему мокрым, после ночного дождя. Осень давала о себе знать. Листва, опавшая с деревьев, прилипала к обуви, пока я шла к остановке до университета." with dissolve
    hide hero with dissolve
    pause 0.5
    show hero walk_location dormitory_02 with dissolve
    pause 0.5
    zhenya "Погода такая же паршивая, как и настроение... С другой стороны, сегодня должно быть интересно, первый же день." with dissolve
    hide hero with dissolve

    scene 31 location busstop dorm with fade
    nothing "Серые улицы и недовольные лица людей - очень похоже на утро понедельника."
    zhenya "Главное сесть на нужный автобус и выйти на нужной остановке. Не хотелось бы потеряться в незнакомом городе и, тем более, опоздать на первую пару в году"

    scene 33 location bus with fade
    nothing "Незнакомые пейзажи сменяли друг друга, а непонятное волнение в груди наростало"
    zhenya "Ого, уже студентка. Ещё и в другой стране. А ведь, кажется, вчера только в школу пошла. Сколько сил потрачено для этого переезда. Годы в художке не прошли зря"
    nothing "Казалось, в автобусе время тянется бесконечно долго. Интересно, это из-за утренних пробок или внутреннего волнения."

    scene 33 location busstop uni with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"
    show model_bus:
        xalign -4.0 yalign 1.1
        linear 4.0 xalign 0.0
        pause 2.0
        linear 10.0 xalign 10.0
    e "bla1 bla1 bla1 bla bla bla bla bla bla bla bla bla"
    pause 2.0

    scene 33 location busstop uni 1 with fade
    e "bla12 bla12bla bla bla bla bla bla bla bla bla bla" with dissolve

    scene 41 location university with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 42 location universitys enter with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 51 location hallway with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 61 location auditory with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 63 location auditory table with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 71 location basement with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

    scene 73 location basement aud with fade
    e "bla bla bla bla bla bla bla bla bla bla bla bla"

####################### 1 ACT ######################

return
