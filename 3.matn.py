# ism = 'Okiljon'
# shahar = 'Тошкент'
# viloyat = 'Тошкент 🗺'
# tuman =  'Зангиота'
# smayl = '😀'
# print(shahar)
# print(viloyat)
# print(smayl)

# ism = 'Okiljon'
# familiya = 'Olimjonov'
# ism_sharif = f"Mening ismi sharifim-{ism} {familiya}"
# print(ism_sharif)

# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')

# ism = 'Okiljon'
# familiya = 'Olimjonov'
# ism_sharif = f"{ism} {familiya}"
# print (ism_sharif.upper())
# print (ism_sharif.lower())
# print (ism_sharif.title())
# print (ism_sharif.capitalize())

# meva = '    olma    '
# print(meva)
# print('Men ' + meva.lstrip() + " yaxshi ko'raman")
# print('Men ' + meva.rstrip() + " yaxshi ko'raman")
# print('Men ' + meva.strip() + " yaxshi ko'raman")

# INPUT
# ism = input('Ismi sharifingiz nima?\n')
# print('Assalomu alaykum, ' + ism.title())

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = 'Bodomzor'
# viloyat = 'Samarqand'
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil.upper())

# kochangiz = input('Kochangizni kiriting: ')
# mahallangiz = input('Mahallangizni kiriting: ')
# tumaningiz = input('Tumaningizni kiriting: ')
# viloyatingiz = input('Viloyatingizni kiriting: ')
# print(kochangiz.title().rstrip(), "ko'chasi,\n", mahallangiz.title().rstrip(), 'mahallasi,\n', tumaningiz.title().rstrip(), 'tumani,\n', viloyatingiz.title().rstrip(), 'viloyati.')

kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
#       tuman + " tumani, " + viloyat + " viloyati")   

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
print(kocha.title() + " ko'chasi,\n" + mahalla.title() + " mahallasi,\n" + \
      tuman.title() + " tumani,\n" + viloyat.title() + " viloyati")