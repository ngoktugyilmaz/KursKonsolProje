import turtle
def KareCizimi():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)

def UcgenCizimi():
    for a in range(3):
        turtle.forward(100)
        turtle.left(120)  

def DaireCizimi():
    for a in range(360):
        turtle.speed(10000)
        turtle.forward(1)
        turtle.right(1)

def AtaturkCizimi():   

   
    turtle.speed(0)
    turtle.hideturtle()


    def leke_ciz(koordinatlar, renk="black", y_kaydir=55):
        turtle.color(renk, renk)
        turtle.penup()
        turtle.goto(koordinatlar[0][0], koordinatlar[0][1] + y_kaydir)
        turtle.pendown()
        turtle.begin_fill()
        for x, y in koordinatlar[1:]:
            turtle.goto(x, y + y_kaydir)
        turtle.goto(koordinatlar[0][0], koordinatlar[0][1] + y_kaydir)
        turtle.end_fill()


    def imza_cizgi(koordinatlar, kalinlik=4):
        turtle.pensize(kalinlik)
        turtle.color("black")
        turtle.penup()
        turtle.goto(koordinatlar[0])
        turtle.pendown()
        for x, y in koordinatlar[1:]:
            turtle.goto(x, y)


    # 1. SOL SAÇ VE KULAK ÇEVRESİ ANA BLOĞU
    sac_ana_blok = [
        (-195, -135), (-225, -75), (-255, -5), (-265, 65), (-248, 130),
        (-205, 195), (-150, 245), (-105, 265), (-90, 260), (-112, 240),
        (-92, 232), (-115, 210), (-108, 185), (-132, 165), (-110, 155),
        (-135, 125), (-115, 118), (-130, 85), (-155, 78), (-190, 88),
        (-225, 82), (-242, 50), (-235, 0), (-205, -45), (-165, -72),
        (-135, -75), (-148, -105), (-195, -135)
    ]
    leke_ciz(sac_ana_blok, "black")

    # Kulak içi kıvrım lekeleri
    kulak_ic_1 = [
        (-185, 68), (-212, 62), (-224, 35), (-218, -5),
        (-195, -35), (-182, -25), (-202, 2), (-205, 32),
        (-182, 48), (-185, 68)
    ]
    leke_ciz(kulak_ic_1, "black")

    kulak_ic_2 = [
        (-165, 35), (-182, 25), (-184, 5), (-170, -10),
        (-158, 0), (-162, 22), (-165, 35)
    ]
    leke_ciz(kulak_ic_2, "black")

    # 2. KAŞLAR VE GÖZ ÇUKURU GÖLGESİ
    kas_goz_golge = [
        (-62, 132), (-45, 145), (-22, 135), (15, 132), (45, 122),
        (65, 130), (82, 122), (115, 115), (132, 128), (145, 118),
        (140, 92), (122, 78), (102, 82), (85, 92), (68, 95),
        (52, 112), (38, 108), (32, 85), (5, 82), (-25, 84),
        (-45, 90), (-62, 105), (-52, 120), (-62, 132)
    ]
    leke_ciz(kas_goz_golge, "black")

    sol_goz_isik = [
        (-32, 102), (-12, 112), (12, 110), (18, 102),
        (-5, 100), (-28, 95), (-32, 102)
    ]
    leke_ciz(sol_goz_isik, "white")

    # 3. ELMACIK KEMİĞİ GÖLGE ÜÇGENİ
    elmacik_ucgen = [
        (-92, 22), (-25, 22), (15, 12), (-8, -12),
        (-32, -55), (-62, -15), (-92, 22)
    ]
    leke_ciz(elmacik_ucgen, "black")

    # 4. BURUN ALTI GÖLGESİ VE KÜÇÜK NOKTALAR
    burun_alti = [
        (35, 10), (52, 12), (85, 22), (128, 26), (136, 15),
        (122, -8), (95, -10), (65, -16), (42, -8), (35, 10)
    ]
    leke_ciz(burun_alti, "black")

    leke_ciz([(22, -2), (30, -2), (30, -5), (22, -5)], "black")
    leke_ciz([(88, -18), (105, -16), (105, -20), (88, -20)], "black")

    # 5. DUDAK VE BIYIK GÖLGESİ
    dudak_golge = [
        (12, -62), (32, -52), (75, -48), (102, -52), (126, -68),
        (118, -74), (92, -62), (55, -64), (22, -72), (12, -62)
    ]
    leke_ciz(dudak_golge, "black")

    # 6. ÇENE ALTI VE BOYUN GÖLGE BLOĞU
    boyun_golge = [
        (5, -78), (15, -105), (55, -122), (105, -122), (122, -135),
        (102, -165), (68, -205), (35, -242), (-15, -195), (-62, -155),
        (-35, -118), (-10, -82), (5, -78)
    ]
    leke_ciz(boyun_golge, "black")

    # 7. K. ATATÜRK İMZASI VE PARAF
    # "K." Harfi ve Noktası
    imza_cizgi([(-185, -255), (-195, -310)], kalinlik=5)
    imza_cizgi([(-155, -252), (-190, -285), (-152, -312)], kalinlik=5)
    imza_cizgi([(-138, -308), (-135, -308)], kalinlik=6)

    # "Atatürk" El Yazısı Gövdesi
    imza_govde = [
        (-112, -312), (-95, -260), (-82, -248), (-78, -262), (-72, -312),  # A
        (-102, -286), (-52, -284),                                        # A yatay çizgisi ve turtle geçişi
        (-48, -256), (-54, -310), (-42, -312), (-28, -304),               # turtle
        (-18, -290), (-26, -306), (-18, -310), (-12, -292), (-8, -310),   # a
        (6, -254), (0, -310), (14, -306),                                 # turtle
        (24, -290), (22, -308), (32, -310), (40, -290), (38, -310),       # ü
        (52, -290), (50, -310), (56, -294), (66, -292),                   # r
        (82, -250), (74, -312),                                           # k dikey çizgi
        (102, -282), (77, -296), (108, -312),                             # k kolları
        (165, -308), (185, -312), (110, -326), (-15, -334), (-145, -336)  # Alt imza parafı
    ]
    imza_cizgi(imza_govde, kalinlik=4)

    # "ü" Harfinin Noktaları
    imza_cizgi([(26, -276), (28, -276)], kalinlik=5)
    imza_cizgi([(38, -276), (40, -276)], kalinlik=5)

    turtle.done()


def PikachuCizimi():
    turtle.speed(0)
    turtle.pensize(3)


    def git(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()


    def daire_ciz(x, y, yaricap, renk):
        git(x, y)
        turtle.fillcolor(renk)
        turtle.begin_fill()
        turtle.circle(yaricap)
        turtle.end_fill()


    # 1. Yüz (Ana Sarı Kısım)
    daire_ciz(0, -120, 120, "#FFD700")

    # 2. Sol Kulak ve Siyah Ucu
    git(-75, 70)
    turtle.fillcolor("#FFD700")
    turtle.begin_fill()
    turtle.setheading(115)
    turtle.forward(110)
    turtle.right(135)
    turtle.forward(110)
    turtle.goto(-75, 70)
    turtle.end_fill()

    git(-106, 136)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.setheading(115)
    turtle.forward(38)
    turtle.right(135)
    turtle.forward(38)
    turtle.goto(-106, 136)
    turtle.end_fill()

    # 3. Sağ Kulak ve Siyah Ucu
    git(75, 70)
    turtle.fillcolor("#FFD700")
    turtle.begin_fill()
    turtle.setheading(65)
    turtle.forward(110)
    turtle.left(135)
    turtle.forward(110)
    turtle.goto(75, 70)
    turtle.end_fill()

    git(106, 136)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.setheading(65)
    turtle.forward(38)
    turtle.right(-135)
    turtle.forward(38)
    turtle.goto(106, 136)
    turtle.end_fill()

    # 4. Gözler ve Göz Bebekleri
    daire_ciz(-45, 10, 18, "black")
    daire_ciz(-40, 22, 6, "white")

    daire_ciz(45, 10, 18, "black")
    daire_ciz(40, 22, 6, "white")

    # 5. Kırmızı Yanaklar
    daire_ciz(-75, -45, 22, "#FF2400")
    daire_ciz(75, -45, 22, "#FF2400")

    # 6. Burun
    git(0, -10)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(8)
    turtle.left(120)
    turtle.forward(16)
    turtle.left(120)
    turtle.forward(16)
    turtle.left(120)
    turtle.forward(8)
    turtle.end_fill()

    # 7. Ağız
    git(-28, -35)
    turtle.setheading(-60)
    turtle.circle(16, 120)
    turtle.setheading(-60)
    turtle.circle(16, 120)

    turtle.hideturtle()
    turtle.done()
def CizimMenu():
    print("╔════════════════════════════════╗")
    print("║      ÇİZİMLER MENUSU           ║")
    print("╠════════════════════════════════╣")
    print("║   1-Kare                       ║")
    print("║   2-Desen                      ║")
    print("║   3-Pikachu                    ║")
    print("║   4-Üçgen                      ║")
    print("║   5-Daire                      ║")
    print("║   6-Atatürk                    ║")
    print("║   7-Çıkış                      ║")
    print("║   Seçimiz nedir?               ║")
    print("╚════════════════════════════════╝")
    secim = input()

    if secim == "1" :
        print("Kare seçtin")
        KareCizimi()
        input()

    if secim == "2" :
        print("Desen seçtin") 

    if secim == "3" :
        print("Pikachu seçtin")     
        PikachuCizimi()
        input()


    if secim == "4" :
        print("Üçgen seçtin")
        UcgenCizimi()
        input()

    if secim == "5" :
        print("Daire seçtin")
        DaireCizimi()
        input()

    if secim == "6" :
        print("Atatürk seçtin")
        AtaturkCizimi()
        input()

