def HesapMakinesiMenu():
  print("╔═════════════════════════╗")
  print("║                         ║")
  print("║     HESAP MAKİNASI      ║")
  print("║                         ║")
  print("║ İşlem:                  ║")
  print("║                         ║")
  print("║  1  2  3  %             ║")
  print("║  4  5  6  +             ║")
  print("║  7  8  9  -             ║")
  print("║                         ║")
  print("╚═════════════════════════╝")
  sayi1=int(input("1.Sayiyi girin:"))
  sayi2=int(input("2.Sayiyi girin:"))
  islem=input("İşleminiz nedir?(+,-,*,/)")
  if islem=="+":
    toplamS = sayi1+sayi2
    print(f"{sayi1} + {sayi2} = {toplamS}")
  if islem=="-":
     çıkarmaS=sayi1-sayi2
     print(f"{sayi1} - {sayi2} = {çıkarmaS}") 
  if islem=="*":
     carpmaS=sayi1*sayi2
     print(f"{sayi1} * {sayi2} = {carpmaS}") 
  if islem=="/":
     bolmeS=sayi1/sayi2
     print(f"{sayi1} / {sayi2} = {bolmeS}")
 
