# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for n in a:
#     if n < 5:
#         print(n)
# print(list(filter(lambda n: n < 5, a)))
# print([n for n in a if n < 5])
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(filter(lambda n: n in b,a))
# print(result)
# print([n for n in a if n in b])
# print(list(set(a) & set(b)))
# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(dict(sorted(d.items(), key=operator.itemgetter(1))))
# print(dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)))
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
# res = {}
# for d in (dict_a, dict_b, dict_c):
#     res.update(d)
# print(res)
# print({**dict_a, **dict_b, **dict_c})
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(sorted(my_dict, key=my_dict.get, reverse=True)[:3])
from heapq import nlargest
print(nlargest(3, my_dict, key=my_dict.get))