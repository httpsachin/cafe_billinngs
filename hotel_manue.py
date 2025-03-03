name=input("enter your name:")
num=input("enter you mobile number:")
print(f"welcome {name} to royal cafe")
print("pasta:50\ndosa:60\nsamosa:15\nicecream:25\nburger:80\nsandwich:40\nkachori:20\npizza:100\ncoffee:150\njalebi(100g):35\npanipuri:30\nbdapaw:20")
total = 0
while True:
    manue={"pasta":50 ,
           "dosa":60,
           "samosa":15,
           "icecream":25,
           "burger":80,
           "sandwich":40,
           "kachori":20,
           "pizza":100,
           "coffee":150,
           "jalebi":35,
           "panipuri":30,
           "bdapaw":20,
           }



    order_1=input("enter you order here:")

    if order_1 in manue:
        quantity = int(input(f"how many {order_1} "))
        total+=manue[order_1]*quantity
    else:
        print("please enter a valid manue")

    chhoice=input("you want add another item yes/no")
    if chhoice =="no":
         print(f"your total is {total}")
         print("thank you for visiting royal  cafe")
         break;

