# These exercises are combination of list , tuple , dictionary and set.
#Ex1 ---------------------------------------------------------
students = [
    ("S101", "Sara", 18, "Python"),
    ("S102", "Ali", 15, "SQL"),
    ("S103", "Mina", 19, "Python"),
    ("S104", "Reza", 12, "Linux"),
    ("S105", "Neda", 17, "SQL"),
    ("S106", "Amir", 9, "Python"),
    ("S107", "Sara", 18, "Python"),
    ("S108", "Hadi", 14, "Linux")
]

course_dict = {}
for i in range(0 , 7):
    if students[i][3] in course_dict.keys():
        course_dict[students[i][3]].append(students[i][2])
    else :
        course_dict[students[i][3]] = list([students[i][2]])

print(course_dict)

course_avg_score = {}
for key , value in course_dict.items():
    course_avg_score[key] = sum(value) / len(value)
print(course_avg_score)

top_15_student = set()
for student in students :
    if student[2] >= 15 :
        top_15_student.add(student[1])
print(top_15_student)

under_10_student = []
for student in students :
    if student[2] < 10 :
        under_10_student.append(student[1])
print(under_10_student)


top_student = max(students , key = lambda student : student[2])
print(top_student[1])

top_course_set = set()
for key , value in course_dict.items():
    if len(value) >= 2:
        top_course_set.add(key)
print(top_course_set)

# Ex2 -------------------------------------------------
orders = [
    ("O101", "Ali", "Laptop", 1, 800),
    ("O102", "Sara", "Mouse", 2, 25),
    ("O103", "Ali", "Keyboard", 1, 60),
    ("O104", "Mina", "Laptop", 1, 800),
    ("O105", "Sara", "Monitor", 2, 150),
    ("O106", "Reza", "Mouse", 3, 25),
    ("O107", "Ali", "Monitor", 1, 150),
    ("O108", "Mina", "Keyboard", 2, 60),
    ("O109", "Sara", "Laptop", 1, 800),
    ("O110", "Reza", "Monitor", 1, 150)
]

customer_info = {}
for order in orders :
    if order[0] in customer_info :
        customer_info[order[0]] = customer_info.get(order[0]) + (order[3] * order[4])
    else :
        customer_info[order[0]] = order[3] * order[4]
print(customer_info)

sold_quantity = {}
for order in orders:
    if order[2] in sold_quantity :
        sold_quantity[order[2]] = sold_quantity.get(order[2]) + order[3]
    else : 
        sold_quantity[order[2]] = order[3]
print(sold_quantity)

# Ex3 --------------------------------------------------
registrations = [
    ("Sara", "Python"),
    ("Ali", "Python"),
    ("Mina", "SQL"),
    ("Sara", "SQL"),
    ("Reza", "Linux"),
    ("Ali", "Linux"),
    ("Mina", "Python"),
    ("Neda", "SQL"),
    ("Sara", "Linux"),
    ("Hadi", "Python"),
    ("Reza", "SQL"),
    ("Neda", "Linux")
]
student_register_count = {}
for register in registrations :
    if register[0] in student_register_count :
        student_register_count[register[0]] = student_register_count.get(register[0]) + 1
    else :
        student_register_count[register[0]] = 1
for k ,  v in student_register_count.items():
    if v == 3 :
        print(k)

for k ,  v in student_register_count.items():
    if v == 2 :
        print(k)

for k ,  v in student_register_count.items():
    if v == 1 :
        print(k)

student_info = []
for k , v in student_register_count.items():
    student_info.append((k , v))
print(student_info)

print(sorted(student_info , key = lambda x : x[1]))

# Ex4 ---------------------------------------------
products = {
    "P1": ("Laptop", 800, 10),
    "P2": ("Mouse", 25, 50),
    "P3": ("Keyboard", 60, 30),
    "P4": ("Monitor", 150, 15),
    "P5": ("Headphone", 45, 20)
}

orders = [
    ("O1", "Sara", "P1", 1),
    ("O2", "Ali", "P2", 3),
    ("O3", "Sara", "P3", 2),
    ("O4", "Mina", "P1", 1),
    ("O5", "Ali", "P4", 2),
    ("O6", "Reza", "P2", 5),
    ("O7", "Mina", "P5", 2),
    ("O8", "Sara", "P4", 1),
    ("O9", "Ali", "P3", 1),
    ("O10", "Reza", "P1", 1),
    ("O11", "Sara", "P2", 4),
    ("O12", "Mina", "P3", 3)
]

price_per_order = {}
for order in orders : 
    price_per_order[order[0]] = order[3] * products[order[2]][1]
print(price_per_order)

product_set = set(products.keys())
sold_product_set = set()
for k in products:
    sold_product_set.add(k)
print(product_set - sold_product_set)

customer_info = {}
for order in orders:
    if order[1] in customer_info :
        customer_info[order[1]] = [customer_info[order[1]][0] + order[3] , customer_info[order[1]][1] + order[3] * products[order[2]][1]]
    else :
        customer_info[order[1]] = [order[3] , products[order[2]][1]]
print(customer_info)

top_customers = []
for k , v in customer_info.items():
    if v[1] > 1000 :
        top_customers.append(k)
print(top_customers)

customer_product = {}
for order in orders :
    if order[1] in customer_product :
        customer_product[order[1]].add(order[2])
    else :
        customer_product[order[1]] = {order[2]}

for k , v in customer_product.items():
    if "P1" in v and "P2" in v:
        print(k)

for k , v in customer_product.items():
    if len(v) >= 2:
        print(k)