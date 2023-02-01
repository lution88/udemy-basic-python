''' 
# 본인의 최대 심박수 계산
(210-자신의 나이/2) - 자신의 몸무게 *0.05 + 4(남성) or 0(여성)

# 존2 심박수 계산
최대심박수 * 0.6~0.7
'''
age = int(input("당신의 나이는? "))
weight = int(input("당신의 몸무게는? "))
gender = input("남성 or 여성? ")
if gender == "남성":
    gender = 4
elif gender == "여성":
    gender = 0
else:
    print("gender 오류")
    gender = 0
    
max_blood_press = (210 - age/2) - weight * 0.05 + gender

# Zone2 심박수 계산
zone2_blood_press = round(max_blood_press * 0.67)
print(zone2_blood_press)