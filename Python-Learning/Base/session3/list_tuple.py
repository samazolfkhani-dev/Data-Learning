# # Ex1------------------------------------------------
# numbers = [12, 5, 8, 20, 3, 15, 8, 25, 10]
# numbers.remove(20)
# numbers.insert(2 , 8)
# for i in range(3):
#     numbers.pop() 
# # or 
# del numbers[-3:]
# numbers.append(100)
# print(numbers.index(8))
# print(numbers.count(8))
# numbers.sort(reverse = True)

# # Ex2------------------------------------------------
# data = [10, 20, 30, 40, 50, 60, 70, 80]
# data[0:3] = [100, 200, 300]
# del data[-2:]
# data.extend([400 , 500])
# data[1:5] = data[4:0:-1]
# print(data)

# # Ex3------------------------------------------------
# sales = [
#     250, 400, 0, 150, -50,
#     300, 400, 0, 700, 250,
#     None, 500, -100, 800
# ]
# size1 = len(sales)
# while i < len(sales):
#     if sales[i] == 0 or sales[i] is None or sales[i] < 0 :
#         sales.pop(i)
#     else:
#         i += 1
    

# total_sum = sum(sales)
# avg = total_sum / len(sales)
# print(avg)
# print(max(sales))
# print(min(sales))
# sales2 = sales.copy()
# sales2.remove(max(sales))
# print(f"second max value : {max(sales2)}")

# print(sorted(sales))

# # Ex4--------------------------------------------------------
# sales = [
#     [1200, 1500, 900, 1800],
#     [800, 1100, 1400, 1000],
#     [2000, 1700, 1600, 1900]
# ]
# total = []
# for i in range(3):
#     total.append(sum(sales[i]))
# print(total)
# for i in range(3):
#     print(total[i] / len(sales[i]))

# for j in range(4):
#     column_sum = 0

#     for i in range(3):
#         column_sum += sales[i][j]

#     print(column_sum)

# print(total[total.index(max(total))])
# print(max(total))

# l1 = []
# for i in range(3):
#     l1.extend(sales[i])
# print(l1)

# # Ex5------------------------------------------
# orders = [
#     ("O101", "Ali", 1200, 2),
#     ("O102", "Sara", 800, 3),
#     ("O103", "Ali", 500, 1),
#     ("O104", "John", 2000, 2),
#     ("O105", "Sara", 800, 2),
#     ("O106", "Mina", 1500, 1),
#     ("O107", "Ali", 700, 3),
#     ("O108", "John", 900, 2)
# ]
# per_value = []
# total_quantity = 0
# for i in range(0 , 7):
#     per_value.append(orders[i][2] * orders[i][3])
#     total_quantity += orders[i][3]
# print(per_value)
# print(sum(per_value))
# print(sum(per_value) / total_quantity)

# customers = []
# for i in range(0 , 7):
#     customers.append(list(orders[i][1] , 0))
# for i in range(0 , 7):
#     cu