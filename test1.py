# for i in range(1, 31):
#     if i==25:
#         continue
#     print(i)

# i = 1
# while i<31:
#     i+=1
#     if i==25:
#         continue
    
#     print(i)
    
    
# for i in range(1, 31):
#     if i==25:
#         continue
#     print(i)

# i = 0
# while i<30:
#     i+=1 
#     if i==25:
#         continue
#     print(i)

# result = 1
# for i in range(10):
#     a = int(input("San jaz: "))
#     # if a:
#     result *= a
# print(result)
    
# res = 1
# for i in range(1,11):
#     a = int(input("San jaz: "))
#     if a:
#         res = res * a
# print("The result is: ", res)

# def deco(myfunc):
#     def simple():
#         print("Start")
#         myfunc()
#         print("Finish")
#     return simple()
    
# @deco
# def simp():
#     print("Hello, ")
    
    

# a = int(input("San jaz: "))
# for i in range(2, a+1):
#     if a%i==0:
#         break
# print(i)

# a = float(input("San jaz: "))
# if a<=2:
#     print(a*10.5)
# else:
#     print(21+((a-2)*4))


# a = str(input("Soz jaz: "))
# b = "siniy"
# if b in a:
#     print("yes")
# else:
#     print("no")

a, b, c = str((input("bir: ")).split())
print(min(a, b, c, key=len), max(a, b, c, key=len))








    