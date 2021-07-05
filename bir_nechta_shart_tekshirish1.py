# son = 50
# if son <0:
#     print('Manfiy son')
# else:
#     print("Musbat son")
# yosh = int(input("Yoshingiz nechida? "))
# if yosh <=4:
#     print("Kirish bepul")
# elif yosh<=12:
#     print("Kirish 5000 so'm")
# elif yosh<=18:
#     print("Kirish 8000 so'm")
# else:
#     print("Kirish 10000 so'm")
# yosh = int(input("Yoshingiz nechida? "))
# if yosh <=4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# elif yosh<=18:
#     narx = 8000
# else:
#     narx = 10000
# print(f"Sizga kirish {narx} so'm")
# kun = input("Bugun nima kun?>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")
# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower() == 'yakshanba' and harorat>=30:
#     print("Cho'milgani kettik!")
# elif kun.lower() == 'yakshanba' and harorat<30:
#     print("Uyda qolamiz")
# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat>=30:
#     print("Cho'milgani kettik!")
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat<30:
#     print("Uyda qolamiz")
# narh = 15000
# choy = True
# salat = True
# if choy and salat:
#     narh += 10000
# elif choy or salat:
#     narh += 5000
# print(f'Jami {narh} som')
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = 1
# if choy:
#     print('Mijoz choy oldi')
#     narh += 3000
# if salat:
#     print('Mijoz salat oldi')
#     narh += 5000
# if non:
#     print('Mijoz non oldi')
#     narh += 2000
# if kompot:
#     print('Mijoz kompot oldi')
#     narh += 5000
# if assorti:
#     print('Mijoz assorti oldi')
#     narh += 15000
# print(f'Jami {narh} som')
# menu = ['osh', 'qozonkabob', "shashlik", "norin", "somsa"]
# "manti" in menu
# menu = ['osh', 'qozonkabob', "shashlik", "norin", "somsa"]
# ovqat = input('Nima ovqat yeysiz? ')
# if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo'q")
# else:
#     print("Buyurtma qabul qilindi")
# menu = ['osh', 'qozonkabob', "shashlik", "norin", "somsa"]
# buyurtmalar = ['osh', "somsa", 'manti', "shashlik"]
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
# menu = ['osh', 'qozonkabob', "shashlik", "norin", "somsa"]
# buyurtmalar = ['osh', "somsa", 'manti', "shashlik"]
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else:
#     print('Savatchangiz bosh')