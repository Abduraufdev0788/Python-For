num  = input("sonlarni vergul bilan ajratib kiriting: ")
list1 = num.split(",")
list1 = list(map(int,list1))
a = len(list1)
b = 0
for i in list1:
    b+=i
    d = b/a
print(d)