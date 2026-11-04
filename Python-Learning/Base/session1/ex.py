a = [1, 2, 3]
b = a
c = a.copy()

a.append(4)
b[0] = 100
c.append(5)

print(a)
print(b)
print(c)

x = 10
y = 10

print(x is y)
print(x == y)

p = [1, 2, 3]
q = [1, 2, 3]

print(p is q)
print(p == q)

# == checks whether two objects have the same value.
# is checks whether two variables refer to the exact same object in memory.


# _____________________________________________________________________________________________
print(bool("False"))
print(bool(""))
print(bool([]))
print(bool([0]))

print(int(3.99))
print(int(-3.99))

print("5" * 3)
print(5 * "3")

print(10 / 2)
print(10 // 3)
print(10 % 3)

print("10" + "5")
print(int("10") + int("5"))

# ______________________________________________________________________________________________
n = [12, 5, 8, 20, 3, 15, 8]
n.remove(20)
n.insert(2 , 10)
n.reverse()
n.count(8)
print(min(n))
print(max(n))
print(sum(n))
print(sum(n) / len(n))
n[0] = n[-1]
n.pop()
print(n)