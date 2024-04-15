"""val = input("")
if(val.isupper()):
    print(val.lower())
elif(val.islower()):
    print(val.upper())
elif(val == "" or val == ''):
    print(None)
elif(val.isdigit()):
    print("Number")

    """




"""score = input("score : ")
score = int(score)

if (81 <= score <= 100):
    print("A")
elif(61 <= score <= 80):
    print("B")
elif(41 <= score <= 60):
    print("C")
elif(21 <= score <= 40):
    print("D")
elif(0 <= score <= 20):
    print("F")
else:
    print("Error")
"""




"""user = input("money: ")
token = user.split()
number = float(token[0])
currency = token[1]

info =  {
    "달러" : 1346
    "엔" : 0,89
    "유로" : 1454
    "위안" : 186
    }
print(info)
if currency == "달러":
    print(number*1346, "원")
elif currency == "엔":
    print(number*0.89, "원")
elif currency == "유로":
    print(number*1454, "원")
elif currency == "위안":
    print(number*186, "원")
"""



number = input("우편번호:")
if (number[0:2] == "01"):
    if(number[2:3]== "0" or number[2:3] == "1" or number[2:3] "2"):
        print("강북구")
    elif(number[2:3] == "3" or number[2:3] == "4" or number[2:3] == "5"):
        print("도봉구")
    elif(number[2:3] == "6" or number[2:3] == "7" or number[2:3] == "8" or number[2:3] == "9"):
        print("노원구")    
else:
    print("없는 정보 입니다.")
