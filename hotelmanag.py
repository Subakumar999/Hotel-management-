print("my name is Subalakshmi K")
print("my emailid is subalakshmimonika@gmail.com")
print("python batch74")


print("***** welcomE to AV HOTEL*******")
print("how can I help you")

def reciption(type1,enter):
    type1="Stay"
    enter="non stay"
    custormer=input("enter you want")

    if custormer=="type1":
        print("i need your details")
        def custormer(name,aadhaar_card,phone_number,otp):
            name=input(f"enter your name")
            aadhaar_card=int(input(f"enter your aadhaar card number:"))
            phone_number=int(input(f"enter your phone number:"))
            while phone_number==10:
                print(f"turn to next page")
            
            
            import random
            print(f"otp send successfully to you {phone_number}")
            otp_number=random.randint(0000,9999)
            print(f"***your otp is {otp_number}")
            otp=int(input(f"enter your otp number:"))
            print(f"your name is {name}")
            print(f"your aadhaar card number is {aadhaar_card}")
            print(f"your phone number is {phone_number}")
            print(f"your otp number is {otp}")
            
            
            def type1(booking):
                booking=["luxuary","AC room","non-AC room"]
                luxuary=5000
                AC_room=4000
                non_AC_room=3000
                
                custormer=input(f"enter your booking:")
                
                how_many=int(input(f"how many rooms do you want :"))
                how_many_days=int(input(f"how many days do  you want to spend:"))
                
                if custormer=="luxuary":
                    total=how_many*how_many_days*luxuary
                    print(f"you need to pay amount is Rs{total}")
                    print(f"total is {total}")
                if custormer=="AC room":
                    total=how_many*how_many_days*AC_room
                    print(f"you need to pay amount is Rs{total}")
                    print(f"total is {total}")
                if custormer=="non AC room":
                    total=how_many*how_many_days*non_AC_room
                    print(f"you need to pay amount is Rs{total}")
                    print(f"total is {total}")
                non_booked_room=200
                free_room=non_booked_room-how_many
              
                print(f"available room is {free_room}")   
                print(f"your room is booked")
            
            type1("booking")
            
            print(f"thanks for waiting for long time \nplease, our staff will take your luggage's to your room")
            
        custormer("name","aadhaar_card","phone_number","otp")            

    if custormer=="enter":
        print(f"your want is {enter}")
        def custormer(wish):
            wish=["veg","non veg"]    
            
            custormer=input("enter your wish:")
            
            if custormer=="veg":
                print("please go to the B building")
            
            if custormer=="non veg":
                print("please go the C block")
        custormer("wish")

        def enter(table):
            table=["inner","outer"]
            
            custormer=input("what kind of tables do you want:")
            
            if custormer=="inner":
                print(f"go to the 2nd floor in B block")

                inner=["party","function","normal"]
            
                custormer=input(f"enter your coming:")

                if custormer=="party":
                    print(f"go the 1st left room")
                if custormer=="function":
                    print(f"go to the 2nd right room")
                if custormer=="normal":
                    print("go to the 3rd left room")
            if custormer=="outer":

                outer=["swimming pool","terrace"]
                custormer=input("enter your visit:")
                
                if custormer=="swimming pool":
                    print(f"our staff take you to the swimming pool")
                if custormer=="terrace": 
                     print(f"our staff take you to the terrace")

            print(f"enjoying the holiday")

        enter("table")
       
    print(f"*****thanks for comming***********")
    print(f"be safe and welcome back again")

reciption("type1","enter")
