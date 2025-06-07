num = int(input("sooni kiriting:"))

juft = 0
toq = 0
for i in range(1,num +1):
    if i % 2 ==0:
        juft += i
        
    if i % 2 ==1 :
        toq +=i
print(juft,toq)        
        