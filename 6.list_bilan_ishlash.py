# cars = ['bmw', 'mercedes-benz', 'volvo', 'genetal motors', 'tesla', 'audi']
# # cars.sort()
# # print(cars)
# # cars.sort(reverse=True)
# # print(sorted(cars, reverse=True))

# sonlar = [12, 45, 23, 56, 998, 1, -5, -7.2]
# print(sorted(sonlar))
# print(sonlar)
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# print(sonlar)
# print(len(cars))
# print(len(sonlar))
# uzunlik = len(sonlar)

# sonlar1 = list(range(1,11))
# print(sonlar1)
# toq_sonlar = list(range(1,20,2))
# print(toq_sonlar)
# juft_sonlar = list(range(0,20,2))
# print(juft_sonlar)
# sanash = list(range(0,101,10))
# print(sanash)
# max_qiyamt = max(toq_sonlar)
# print(max_qiyamt)
# narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# print(min(narxlar))
# print(max(narxlar))
# print(sum(narxlar))
# print(cars[0:3])
# print(cars[2:5])
# print(cars[3:7])
# print(cars[1:])
# print(cars[:])
# print(cars[:2])
# my_cars = cars
# print(my_cars)
# my_cars.remove('volvo')
# print(my_cars)
# my_cars[0] = 'lacetti'
# print(my_cars)
# print(cars)
# cars.append('bmw')
# print(cars)
# cars = ['bmw', 'mercedes-benz', 'volvo', 'genetal motors', 'tesla', 'audi']
# my_cars = cars[:]
# my_cars.remove('bmw')
# print(my_cars)
# print(cars)
# # TUPLE - O'zgarmas ro'yxat
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[-1])
# print(toys[2:5])
# print(toys[3:])
# # toys[0] = 'teddy'
# # print(toys)

# # toys.remove('bear')
# toys = list(toys)
# print(type(toys))
# toys.append('teddy')
# toys = tuple(toys)
# print(type(toys))

davlatlar = ['Saudiya Arabistoni', 'Turkiya', 'Suriya', 'Misr', "O'zbekiston", "Qozog'iston", 'Iroq', 'Bahrayin']
davlatlar.append('Indonezia')
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
j_sonlar = list(range(120,1201,2))
print(sum(j_sonlar))
print(max(j_sonlar) - min(j_sonlar))
print(len(j_sonlar))
print(j_sonlar[0:21])
print(j_sonlar[260:281])
print(j_sonlar[520:542])
taomlar = ['osh', "lag'mon", 'qozon kabob', 'shashlik', 'mohora']
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove("lag'mon")
nonushta.remove('qozon kabob')
nonushta.append('non')
nonushta.append('saryog')
print(nonushta, taomlar)
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)