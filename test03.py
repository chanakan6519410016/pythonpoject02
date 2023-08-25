#รับค่า/ป้อนทางแป้นพิมพ์ ใช้ฟังก์ชั้น input() โดยสิ่งที่ป้อนทั้งหมดถือเป็น String
 
#ตัวแปร variable เป็น identifier มีหน้าที่เก็บช้อมูลที่เกิดขึ้นในโปรแกรม ช้อมูลที่เก็บจะอยู่ใน RAM
#identifier คือ ชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฏการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdํYearBorn = input('ป้อนปีเกิด : ')
print('---------------------')
stdAge =2023 - int(stdํYearBorn) #ต้องแปลง String เป็น number -> int( ), float( )
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
print(f"คุณเกิดปี {stdํYearBorn} อายุ {stdAge}")
print('---------------------')
print("ยินดีต้อนรับ",std_id,"ชื่อ",std_name) #ใช้,
print("คุณเกิดปี",stdํYearBorn,"อายุ",stdAge)
print('---------------------')
print("ยินดีต้อนรับ "+str(std_id)+" ชื่อ "+str(std_name)) #ใช้ +
print("คุณเกิดปี "+str(stdํYearBorn)+" อายุ "+str(stdAge))
print('---------------------')
print("ยินดีต้อนรับ {} ชื่อ {} ".format(std_id,std_name)) 
print("คุณเกิดปี {} อายุ {} ".format(stdํYearBorn,stdAge))
print('---------------------')
print("ยินดีต้อนรับ %s ชื่อ %s " %(std_id,std_name))
print("คุณเกิดปี %s อายุ %s " %(stdํYearBorn,stdAge))