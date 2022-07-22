

# from datetime import datetime
# x=["py", "19.07.22"]
# y=x[1]
# date_goal = datetime.strptime(y, '%d.%m.%y')

# print(date_goal)



# today = datetime.today()
# print(today)

# dif=today-date_goal
# print(dif)





from datetime import datetime
user=input("enter your goal: deadline seperated by comma \n")
input=user.split(":")
deadline=input[1]
datetime_object = datetime.strptime(deadline, "%d/%m/%Y")

# print (deadline)


current=datetime.today()


d=datetime_object-current
print (d)
print(f"dear bro you have {d} seconds left")
