num  = input("sonlarni vergul bilan ajratib kiriting: ")
list1 = num.split(",")
list1 = list(map(int,list1))
max_value =list1[0]
min_value =list1[0]
    

if len(list1) == 5 :
    for i in list1:
        if i < min_value:
            min_value = i
            
    for i in list1:
        if i > max_value:
            max_value = i
    print(min_value,max_value)

else:
    print("5 ta son kiriting")