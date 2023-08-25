#1. ใช้ ,
print("Hello...",456,'Hi...',True,10+20,"Hey...")
#2. ใช้ + มีข้อแม้ว่าทุกตัวที่เอามาต่อกันต้องเป็น String
print("Hello... "+str(456)+' Hi... '+str(True)+' '+str(10+20)+" Hey...")
#3. ใช้เมธอด format
print("Hello... {} Hi... {} {} Hay...".format(456,True,10+20))
print("Hello... {0} Hi... {1} {2} Hay...".format(456,True,10+20)) #index number
#4. ใช้ f-string
print(f"Hello... {456} Hi... {True} {10+20} Hay...")
#5. ใช้ modulo operator (%) -> %d, %f, %s, .....
print("Heiio... %d Hi... %s %d Hey..." %(456,True,10+20) )