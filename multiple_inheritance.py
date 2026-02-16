class a:
    a = 10
class b:
    b = 20
class c(a,b):
    c = a.a + b.b  # Accessing class attributes using the class names
c1=c()
print(c1.a)
print(c1.b)
print(c1.c)
