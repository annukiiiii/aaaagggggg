sum=0
j=0
while sum<5:# mexri na ginoun kai oi 6 elenxoi
    passw = input ("dwse kodiko: ")
    for x in passw:
        j+=1
    if j>=6 and j<=16:
        sum+=1      
    for x in passw:
        if x in ("qwertyuiopasdfghjklzxcvbnm"):
            sum+=1
            
        if x in ("QWERTYUIOPASDFGHJKLZXCVBNM"):
            sum+=1
            
        if x in ("1234567890"):
            sum+=1
           
        if x in ("$#@"):
            sum+=1
            
        
print("swstos kodikos")