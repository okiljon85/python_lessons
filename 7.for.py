# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# # print('Salom', mehmonlar[0])
# # print('Salom', mehmonlar[1])
# # print('Salom', mehmonlar[2])

# # for mehmon in mehmonlar:
# #     print('Salom', mehmon)
# #     print('Xayr', mehmon)
# # print('Xayr', mehmon) 
# # for mehmon in mehmonlar:
# #     print(f'Hurmatli {mehmon}, Sizni 20 Dekabr kuni yoziladigan nahorgi osh dasturxonimizga taklif qilamiz')
# #     print('Hurmat bilan Palonchiyevlar oilasi\n')

# # sonlar = list(range(1,11))
# # for son in sonlar:
# #     print(f'{son}ning kvadrati {son**2}ga teng')

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []
# print("5 ta eng yaqin dostingiz kim?")
# for n in range (5):
#     dostlar.append(input(f'{n+1}-dostingizni ismini kiriting'))
# print(dostlar)

# ismlar = ['Abdurrohman', 'Akram', 'Aliy', 'Abror', 'Mubashshir']
# for ism in ismlar:
#     print('Salom', ism)
# print('Kod', len(ismlar), 'marta takrorlandi')
# t_sonlar = list(range(11, 100, 2))
# for t_son in t_sonlar:
#     print(t_son**3)

# kinolar = []
# print('5 ta sevimli kinoingiz?')
# for n in range(5):
#     kinolar.append(input(f'{n+1}-sevimli kinoingizni kiriting: '))
# print(kinolar)

a = (int(input('Bugungi suhbatdoshlar soni:')))
suhbatdoshlar = []
for n in range(a):
    suhbatdoshlar.append(input(f'{n+1}-Bugungi suhbatdoshingiz kim: '))
print(suhbatdoshlar)