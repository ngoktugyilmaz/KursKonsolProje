import ProgramOyunlar,ProgramCizim,ProgramHesapMakinesi
def anamenu():
    print("╔════════════════════════════════╗")
    print("║             ANA MENU           ║")
    print("╠════════════════════════════════╣")
    print("║   1-Oyunlar                    ║")
    print("║   2-Çizimler                   ║")
    print("║   3-Hesaplamalar               ║")
    print("║   4-Çıkış                      ║")
    print("║   Seçimiz nedir?               ║")
    print("╚════════════════════════════════╝")
    secim = input()
    if secim == "1" :
        print("Oyunları seçtin")
        ProgramOyunlar.oyunMenu()
    if secim == "2" :
        print("Çizimleri seçtin")
        ProgramCizim.CizimMenu()
    if secim == "3" :
        print("Hesaplamalar seçtin")
        ProgramHesapMakinesi.HesapMakinesiMenu()
    if secim == "4" :
        exit()
    anamenu()

anamenu()


