# Ex1---------------------------------------
product = 'Jean'
price = 30
quantity = 3
print(f"Product Name : {product}\nPrice : {price}\nQuantity : {quantity}\nToatal : {quantity * price}")

# Ex3---------------------------------------
score = int(input("Enter Your Score: "))
if 90 <= score <= 100 :
    print('A')
elif 80 <= score <= 89 :
    print('B')
else :
    print("C")

# Ex6------------------------------------------------
numbers = [4, 9, 12, 7, 18, 5]
for i in numbers :
    if i > 10 :
        print(i)
        break

# Ex10------------------------------------------------
guess = 10
num = int(input("Enter Number : "))
attempt = 1
while num != guess :
    num = int(input("Enter Number : "))
    attempt += 1
    if num > (2*guess):
        print("Too High!")
    elif num < (guess / 2):
        print('Too Low!')
print(f"Congratulations (Attempt : {attempt})")