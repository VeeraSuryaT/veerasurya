num=11
if num>1:
    for i in range(2,num//2):
    if (num % i) == 0: 
           print(num, "no") 
           break
   else: 
       print(num, "yes") 
  
else: 
   print(num, "no") 
