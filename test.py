


from ast import Num


number_of_units=24
units= "hours"

def time_try(days):
        # print(days>0)
        # if days > 0 : 
            
    return ( f"{days} days are {days*number_of_units} {units}" )
        # elif days ==0:
        #     return ("you entered zero")
        # else:
        #     return("enter a +ve val")   
        # print("please enter a digit")



# def validate():
#     if x.isdigit():
#         x=int(X)
#         z=time_try(x)   
#         print(z)
#     else:
#         print("enter a number")


def check():
    # x=input("enter the no of days: \n")
    # if num1.isdigit():
    try:

        x=int(i)
        if x > 0:
            # x=int(xb)
            z=time_try(x)   
            print(z)
        elif x == 0: 
            print ("yu enetered 0")
        elif x  < 0:
            print ("enter +ve val")
    except ValueError:
        print ("dont blow up my code")
  
# num1= ""
# while num1 != "exit" :
num1=input("enter the no of days: \n")
print(num1.split(", "))
for i in  num1.split(", "):
    check()



# validate()
