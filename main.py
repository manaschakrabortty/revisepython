# print(f"20 days are xxx {20 * 24 *60} minitues")
# cal_to_units=24*60*60
# name_of_unit="seconds"
# print(f"20 days are {20 * cal_to_units} minitues")
# print(f"20 days are {20 * 24 *60} {name_of_unit}")

# def days_to_units():
#     print(f"20 days are {20 * 24 *60} {name_of_unit}")
#     print("manas")

# days_to_units()

# cal_to_units=24*60*60
# name_of_unit="seconds"

# def days_to_units(num_days, custom_message):
#     print(f"{num_days} days are {20 * 24 *60} {name_of_unit}")
#     print(custom_message)
# # days_to_units(20, "manas")
# # days_to_units(30, "chakrabortty")
# user_input=input("hey a number of days and it convwrt to hours\n ")
# print(user_input)


# cal_to_units=24*60*60
# name_of_unit="seconds"

# def days_to_units(num_days):
#     return f"{num_days} days are {20 * 24 *60} {name_of_unit}"


# my_var=days_to_units(20)
# print(my_var)

# # days_to_units(20, "manas")
# # days_to_units(30, "chakrabortty")
    
# # user_input=input("hey a number of days and it convwrt to hours\n ")
# # print(user_input)


# cal_to_units=24*60*60
# name_of_unit="seconds"

# def days_to_units(num_days):
#     return f"{num_days} days are {20 * 24 *60} {name_of_unit}"

# user_input=input("hey a number of days and it convwrt to hours\n ")
# int(user_input)
# cal_val=days_to_units(user_input)
# print(cal_val)




# cal_to_units=24
# name_of_unit="hours"

# def days_to_units(num_of_days):
#     if num_of_days > 0:
#         return f"{num_of_days} days are {num_of_days *cal_to_units} {name_of_unit}"
#     elif (num_of_days==0):
#         return "nyou entire a 0"
    
# def valid_and_exe():
#     if user_input.isdigit():
#         user_input_number=int(user_input)

#     else:
#         print("you entired a non valid number ")

# user_input=input("hey a number of days and it convwrt to hours\n ")
# valid_and_exe()




# cal_to_units=24
# name_of_unit="hours"

# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days *cal_to_units} {name_of_unit}"
    

# def valid_and_exe():
#     if user_input.isdigit():
#         user_input_number=int(user_input)
#         if user_input_number >0:
#             calculated_value =days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number==0:
#             print("you input is not avalid number")
#     else:
#         print("you entired a non valid number ")

# user_input=input("hey a number of days and it convwrt to hours\n ")
# valid_and_exe()



#USE TRY AND EXCEPT

# cal_to_units=24
# name_of_unit="hours"

# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days *cal_to_units} {name_of_unit}"
    
    
# def valid_and_exe():
#     try:
#         user_input_number=int(user_input)
#         if user_input_number >0:
#             calculated_value =days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number==0:
#             print("you input is not avalid number")
#         else:
#             print("it is a negative number")
#     except ValueError:
#         print("you entired a non valid number ")

# user_input=input("hey a number of days and it convwrt to hours\n ")
# valid_and_exe()



#USE WHILE LOOP

# cal_to_units=24
# name_of_unit="hours"

# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days *cal_to_units} {name_of_unit}"
# def valid_and_exe():
#     try:
#         user_input_number=int(user_input)
#         if user_input_number >0:
#             calculated_value =days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number==0:
#             print("you input is not avalid number")
#         else:
#             print("it is a negative number")
#     except ValueError:
#         print("you entired a non valid number ")

# user_input=""#assign empty string to user_input
# while user_input != "exit":#condition gets evaluated
#     user_input=input("hey a number of days and it convwrt to hours\n ")#user is prompted for its input
#     valid_and_exe()#Functions is called and input is validated and executed



#LIST AND FOR LOOP


# cal_to_units=24
# name_of_unit="hours"

# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days *cal_to_units} {name_of_unit}"
# def valid_and_exe():
#     try:
#         user_input_number=int(num_of_days_ele)
#         if user_input_number >0:
#             calculated_value =days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number==0:
#             print("you input is not avalid number")
#         else:
#             print("it is a negative number")
#     except ValueError:
#         print("you entired a non valid number ")
# user_input=""
# while user_input != "exit":
#     user_input=input("HEY USER ,ENTIRE NUMBER OF DAYS AS A COMA SEPARATED LIST AND I WILL convwrt to hours :--- \n ")
#     print(type(user_input.split(",")))
#     print(user_input.split(","))
#     for num_of_days_ele in user_input.split(","):
#         valid_and_exe()
    

#SETS



    #BASIC SET OPERATION
        #Create a set
        #Access items only via loop
        #Add an item to the set
        #Remove an item from the set
    #@note- UNORDERED AND UNCHANGEABLE
        #items in a set do not have defined order!
        #items cannot be referred to by index!
        #items cannot be changed, only added/removed!
# my_set={"jan","feb","march"}




#DISCTIONARY 


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit =="hours":
        return f"{num_of_days} days are {num_of_days *24} {conversion_unit}"
    elif conversion_unit=="mintiues":
         return f"{num_of_days} days are {num_of_days *60} {conversion_unit}"
    else:
        return"UNSUPPORTED UNIT"
def valid_and_exe():
    try:
        user_input_number=int(days_and_unit_disc["days"])
        if user_input_number >0:
            calculated_value =days_to_units(user_input_number,days_and_unit_disc["unit"])
            print(calculated_value)
        elif user_input_number==0:
            print("you input is not avalid number")
        else:
            print("it is a negative number")
    except ValueError:
        print("you entired a non valid number ")
user_input=""
while user_input != "exit":
    user_input=input("HEY USER ,ENTIRE NUMBER OF DAYS AND CONVERSION UNIT :--- \n ")
    days_and_unit =user_input.split(":")
    print(days_and_unit)
    days_and_unit_disc={"days":days_and_unit[0], "unit":days_and_unit[1]}
    print(days_and_unit_disc)
    valid_and_exe()
