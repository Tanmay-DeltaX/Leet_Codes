lst1=[1,4,5,5]
lst2=[4,7,3]
lst3=[]
lst4=[lst1,lst2]
assumed=0


for k in lst4:
    for i,value in enumerate(k):
        value*=(10**(len(k)-i-1))
        assumed+=value


# for k,value2 in enumerate(lst2):
#     value2*=(10**(len(lst2)-k-1))
#     assumed+=value2
        

for j in str(assumed):
    lst3.append(int(j))    
print(lst3)    