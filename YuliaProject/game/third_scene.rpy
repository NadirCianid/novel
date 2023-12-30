define k = Character("Кей", what_size=20, who_color="#070b9c")
define n = Character("Таинственный голос", what_size=20, who_color="#F0ed2c")
define gg = Character("Юля", what_size = 20, who_color="#0b86f6")

image main_hall = "main hall.png"
image key normal = "keya normal.jpeg"
image black_screen = "black_screen.png"

label third_scene:
    scene main_hall
    with dissolve

    n "Спустя некоторое время наши герои оказались в замке."

    "На этом демо-версия заканчивается. Спасибо, что были с нами, увидимся в будущем на релизе."

    jump game_over