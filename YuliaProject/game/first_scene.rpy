define k = Character("Кей", what_size=20, who_color="#070b9c")
define n = Character("Таинственный голос", what_size=20, who_color="#F0ed2c")
define gg = Character("Юля", what_size = 20, who_color="#0b86f6")

image working_table_usual = "monitor_off.png"
image working_table_strange = "monitor_strange.png"
image white_screen = "white_screen.png"

image key = "keya happy.png"

label intro:
    scene working_table_usual
    play music "bg_music.mp3"

    gg "Охххх"

    gg "Как же я устала готовиться к этому экзамену!"

    gg "А, к какому экзамену я вообще готовлюсь? Голова уже совсем не варит."

    "..."

    gg "zzz (звуки сна)"

    "\" Происходит резкая вспышка света\""
    scene white_screen

    "..."

    scene working_table_strange
    with dissolve

    gg "Что происходит? Я уснула?"

    menu:
        "Не думаю. Все выглядит довольно естественно" :
            jump into_the_magic

        "Похоже, что да." :
            jump back_to_reality
    return

label back_to_reality:
    scene working_table_usual
    with dissolve

    play music "bg_music.mp3"

    gg "Я действительно заснула!"

    "Это не удивительно при такой нагрузке."

    gg "Пора ложиться спать. Но на этот раз в кровать."

    gg "Ну и ну! В следующий раз не буду засиживаться допоздна."

    return

label into_the_magic:
    scene working_table_strange
    play music "magic_begins.mp3"

    show key at left

    gg "ЭТО ТЫ????"


    k "Пока мы не знакомы, но скоро все изменится."

    gg "О чем ты?"

    k "Скоро увидимся)"

    "\" Происходит резкая вспышка света\""
    scene white_screen

    "..."

    gg "Чтоооооо? Подожди!"

    
    jump back_to_reality
    return
