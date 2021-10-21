'''
List comprehension 
'''

# squares = []
# for x in range (10):
#   squares.append (x ** 2)
# print(squares)

#with list comprehension 
# print ([x ** 2 for x in range (10)])

#you can also warp the list in a varibale and print the varible 

'''
Conditinals in List comprehension 
'''

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# print(combs)

# # with list comprehension
# combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(combs)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

res = []
for i in range(4):
    res.append([row[i] for row in matrix])

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(res)

# =========================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

res = []
for i in range(4):
    res_row = []
    for row in matrix:
        res_row.append(row[i])
    res.append(res_row)

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(res)

# =========================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

res = list(zip(*matrix))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print(res)
