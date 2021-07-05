# juft_son = int(input('Juft son kiriting: '))
# if juft_son % 2 == 0:
#     print('Rahmat!')
# else:
#     print('Bu juft son emas.')
# yosh = int(input("Yoshingiz nechida? "))
# if yosh <= 4 or yosh >= 60:
#     print("Bilet bepul")
# elif yosh < 18:
#     print("Bilet narxi 10000 so'm")
# elif yosh >= 18:
#     print("Bilet narxi 20000 so'm")
# son_1 = int(input('Birinchi sonni kiriting: '))
# son_2 = int(input('Ikkinchi sonni kiriting: '))
# if son_1 < son_2:
#     print(son_1, "<", son_2)
# elif son_1 > son_2:
#     print(son_1, ">", son_2)
# elif son_1 == son_2:
#     print(son_1, "=50", son_2)
# mahsulotlar = ['uzum', 'hurmo', 'anor', 'anjir', 'zaytun', 'olma', 'nok', 'shaftoli', 'apelsin', 'banan']
# savat = []
# for n in range(5):
#     savat.append(input(f"savatga {n+1}-mahsulotni qo'shing: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
# mahsulotlar = ['uzum', 'hurmo', 'anor', 'anjir', 'zaytun', 'olma', 'nok', 'shaftoli', 'apelsin', 'banan']
# savat = []
# for n in range(5):
#     savat.append(input(f"savatga {n+1}-mahsulotni qo'shing: "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahzulotlar do'konimizda bor")
# foydalanuvchilar = ['anvar', 'ikrom', 'zokir', 'bahrom', 'asror']
# login = input('Yangi login tanlang: ')
# if login in foydalanuvchilar:
#     print("Login band, yangi login tanlang")
# else:
#     print(f'Xush kelibsiz! {login.title()}')
son = int(input('Istalgan butun son kiriting: '))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")