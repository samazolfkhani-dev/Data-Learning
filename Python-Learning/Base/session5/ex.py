# Ex1 ---------------------------------------
def calculator(num1 , num2 , op = "add"):
    if op == "add":
        return num1 + num2
    if op == "dif":
        return num1 - num2
    if op == "mul":
        return num1 * num2
    if op == "div":
        if num2 == 0 :
            return "Can not division by zero!"
        return num1 / num2

print(calculator(3 , 5 , "div"))

# Ex2 -------------------------------------
def analyze_students(students = list):
    student_avg_score = {}
    for k , v in students.items():
        student_avg_score[k] = sum(v) / len(v)

    top_avg_students = []
    for k , v in student_avg_score.items():
        if v >= 17 :
            top_avg_students.append(k)

    topest = sorted(student_avg_score.items() , key = lambda x : x[1])

    accepted = []
    for k , v in student_avg_score.items():
        if v > 12 :
            accepted.append(k)

    return f"Students Score Avg : {student_avg_score}\nTop Students : {top_avg_students}\n Topest student : {topest[-1][0]}\nAccepted Students : {accepted}"

students = {
    "Ali": (18, 15, 20),
    "Sara": (19, 20, 18),
    "Reza": (12, 14, 16),
    "Mina": (20, 19, 20)
}

print(analyze_students(students))

# Ex3 ------------------------------------------
orders = [
    (101, "Ali", "P1"),
    (102, "Sara", "P2"),
    (103, "Ali", "P2"),
    (104, "Reza", "P3"),
    (105, "Sara", "P1"),
    (106, "Ali", "P3"),
    (107, "Mina", "P1")
]
def customer_products(orders):
    customer_orders = {}
    for order in orders :
        if order[1] in customer_orders:
            customer_orders[order[1]].append(order[2])
        else :
            customer_orders[order[1]] = [order[2]]
    print(customer_orders)

    print("Customers Whom Bought P1 & P2 \n")
    for k ,v in customer_orders.items():
        if "P1" in v and "P2" in v:
            print(k)

    customer_product_unique = {}
    for k , v in customer_orders.items():
        customer_product_unique[k] = len(v)
    print(customer_product_unique)

customer_products(orders)


# Ex4 ----------------------------------------
inventory = {
    "Laptop": (10, 500),
    "Mouse": (50, 20),
    "Keyboard": (15, 50),
    "Monitor": (8, 200)
}

def inventory_report(inventory):
    inventory_evaluation = {}
    for k , v in inventory.items():
        inventory_evaluation[k] = v[0] * v[1]
    print(inventory_evaluation)

    total_value = 0
    for v in inventory_evaluation.values():
        total_value += v
    print(f"Total Value : {total_value}")

    products_under_10_uantity = []
    for k , v in inventory.items():
        if v[0] < 10:
            products_under_10_uantity.append(k)
    print(products_under_10_uantity)

    max_key = None
    max_value = 0
    for k , v in inventory.items():
        if v[1] > max_value :
            max_value = v[1]
            max_key = k
    print(max_key , " : ", max_value)

    print(sorted(inventory.items() , key = lambda v: v[1][0] * v[1][1]))

inventory_report(inventory)

# Ex5 --------------------------------------------------
users = [
    {
        "id": 1,
        "name": "Ali",
        "age": 22,
        "skills": {"Python", "SQL", "Linux"}
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 20,
        "skills": {"Python", "Django"}
    },
    {
        "id": 3,
        "name": "Reza",
        "age": 25,
        "skills": {"SQL", "Linux", "Docker"}
    },
    {
        "id": 4,
        "name": "Mina",
        "age": 21,
        "skills": {"Python", "SQL", "Django"}
    }
]

def age_filter(users , age):
    for user in users:
        if user["age"] > age : 
            return user

def filter_by_skills(users , skill):
    for user in users :
        if skill in user["skills"] :
            return user

def common_skills(users):
    skill_user = {}
    for user in users :
        for skill in user["skills"]:
            if skill in skill_user:
                skill_user[skill].add(user["id"])
            else :
                skill_user[skill] = {user["id"] ,}
    for k , v in skill_user.items():
        if len(v) == 4:
            print(k)
            




            
