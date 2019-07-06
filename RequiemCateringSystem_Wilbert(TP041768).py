#Read Variable
customer = 0
breakfast_set = 0
breakfast_total = 0
lunch_set = 0
lunch_total= 0
table_price = 0
table_int = 0
chair_price = 0
chair_int = 0
cloths_price = 0
cloths_int = 0
pay_tot = 0
refund = 0
total_add = 0
total_sum = 0
total_pay_new = 0
total_food = 0

#Ask for the user name
def my_name():
    global myname
    myname=input("Hello,what shall i call you?:\n")
    if len(myname)<15:
        print(40*('='))
        print("Hello",myname,",Nice to meet you!")
        print(40*('='))
        customer_ask()
    else:
        print("You're only allowed to write 15 character!")
        my_name()

#Ask how many people are the user eating with
def customer_ask():
    global customer
    customer_old= 0
    while(customer_old!=999):
        customer_old=int(input("How many people are with you?:\n"))
        customer=int(customer_old)
        print(40*('='))
        if(customer>0 and customer<999):
            print(40*('='))
            main_menu()
        else:
            print("Not more than 999 people,",myname,"!")
            print(40*('='))
            customer_ask()
            

#Display the Main Menu list and ask choices
def main_menu():
    print("         _____________________________________________   ")
    print("        /        __             ___                   /")
    print("       / /   /  /    /    /    /   /                 /")
    print("      / /   /  /    /    /    /   /                 /")
    print("     / /---/  /__  /    /    /   /                 /")
    print("    / /   /  /    /    /    /   /                 / ")
    print("   / /   /  /___ /___ /___ /___/                 /")
    print("  /                                             /")
    print(" /_____________________________________________/")
    print(" |Hello",myname,",Welcome to Requiem Restaurant     |")
    print(" |This is a self ordering program              |")        
    print(" |What would you like to do?                   |")
    print("  ---------------------------------------------")
    print("O-Order")
    print("R-Report")
    print("P-Payment")
    print("U-Promotion")
    print("E-Exit")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="O"):
        print(40*('='))
        order()
    elif(choice_new=="R"):
        print(40*('='))
        report()
    elif(choice_new=="P"):
        print(40*('='))
        payment()
    elif(choice_new=="U"):
        print(40*('='))
        promotion()
    elif(choice_new=="E"):
        print(40*('='))
        print("See you next time!")
        quit()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        main_menu()

#Display the Order Menu list and ask choices
def order():
    print(myname,",This is the Order menu")
    print("What would you like to do?")
    print("F-Place orders for food")
    print("S-Place order for other services")
    print("M-Back to Main menu")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="F"):
        print(40*('='))
        order_food()
    elif(choice_new=="S"):
        print(40*('='))
        order_service()
    elif(choice_new=="M"):
        print(40*('='))
        main_menu()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        order()

#Display order food menu and ask choices
def order_food():
    print(myname,",This is the Order Food menu")
    print("What would you like to do?")
    print("B-Place orders for Breakfast")
    print("L-Place order for Lunch")
    print("O-Back to Order menu")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="B"):
        print(40*('='))
        food_breakfast()
    elif(choice_new=="L"):
        print(40*('='))
        food_lunch()
    elif(choice_new=="O"):
        print(40*('='))
        order()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        order_food()

#Display food breakfast menu and ask choices
def food_breakfast():
    print(myname,",This is the Breakfast menu")
    print("What would you like to do?")
    print("L-See Breakfast menu list")
    print("B-Order Breakfast menu")
    print("F-Back to Order Food menu")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="L"):
        print(40*('='))
        breakfast_list()
    elif(choice_new=="B"):
        print(40*('='))
        breakfast_order()
    elif(choice_new=="F"):
        print(40*('='))
        order_food()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        food_breakfast()

#Display breakfast set list
def breakfast_list():
    print(myname,",This is your Breakfast menu set")
    print("Only 30RM per set")
    print(40*('-'))
    breakfast_list=["1.[2x Nasi Lemak ]",
               "2.[1x Nasi Ayam]",
               "3.[1x Roti Bakar]",
                "4.[1x Roti Channai]",
                "5.[1x Sandwich]",
                "6.[3x Icetea]",
                "7.[3x Tehtong]"]
    for list_1 in breakfast_list:
        print(list_1)
    print(40*('='))
    food_breakfast()

#Display order food menu and ask choices
def breakfast_order():
    global breakfast_total
    global breakfast_set
    breakfast_set = 0
    breakfast_total = 0
    print(myname,",How many set would like to order?")
    print("Just simply input with 0 value to cancel/clear the order :)")
    print("*Reminder: If you insert any words / letter, this program will close itself :) *")
    print("*Please input the number of set you want*")
    print()
    breakfast_set=int(input("How many set:\n"))
    breakfast_total=float(breakfast_set*30.00)
    breakfast_ask()

#Ask user to check order
def breakfast_ask():
    print(40*('='))
    print(myname,",Are you sure with your order?")
    print("A-Yes")
    print("B-No")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="A"):
        print(40*('='))
        print("Your payment has added!")
        print(40*('='))
        main_menu()
    elif(choice_new=="B"):
        print(40*('='))
        print("Redo your Breakfast Order")
        print(40*('='))
        breakfast_order()
    else:
        print(40*('='))
        print("Wrong input/type!")
        breakfast_ask()

#Display Lunch menu and ask choices
def food_lunch():
    print(myname,",This is the Lunch menu")
    print("What would you like to do?")
    print("L-See Lunch menu list")
    print("O-Order Lunch menu")
    print("F-Back to Order Food menu")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="L"):
        print(40*('='))
        lunch_list()
    elif(choice_new=="O"):
        print(40*('='))
        lunch_order()
    elif(choice_new=="F"):
        print(40*('='))
        order_food()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        food_lunch()

#Display Lunch menu set
def lunch_list():
    print(myname,",This is your Lunch menu set ")
    print("It is only RM60/set")
    print(40*('-'))
    lunch_list=["1.[2x Marmite Fish Rice]",
               "2.[1x Fish and Chip]",
               "3.[2x Baked Rice]",
                "4.[1x Chicken Steak]",
                "5.[1x Fu Yong Hai with Rice]",
                "6.[4x Icetea]",
                "7.[3x Tehtong]"]
    for list_2 in lunch_list:
        print(list_2)
    print(40*('='))
    food_lunch()

#Ask user how many set he/she would like to order
def lunch_order():
    global lunch_total
    global lunch_set
    lunch_set = 0
    lunch_total = 0
    print(myname,",How many set would you like to order?")
    print("Just simply input with 0 value to cancel/clear the order :)")
    print("*Reminder: If you insert any words / letter, this program will close itself :) *")
    print("*Please input the number of set you want*")
    print()
    lunch_set=int(input("How many set?:\n"))
    lunch_total=lunch_set*60.00
    lunch_ask()

#Ask user whether his/her order is correct
def lunch_ask():
    print(40*('='))
    print(myname,",Is your order correct?")
    print("A-Yes")
    print("B-No")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="A"):
        print(40*('='))
        print("Your payment has added!")
        print(40*('='))
        main_menu()
    elif(choice_new=="B"):
        print(40*('='))
        print("Redo your Lunch Order")
        print(40*('='))
        lunch_order()
    else:
        print(40*('='))
        print("Wrong input/type!")
        lunch_ask()

#Display service menu and ask choices
def order_service():
    print(myname,",This is the Service menu")
    print("What would you like to do?")
    print("S-Check Services prices")
    print("T-Add/Reserve Party Services")
    print("M-Back to Main menu")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="S"):
        print(40*('='))
        service_list()
    elif(choice_new=="T"):
        print(40*('='))
        service_add()
    elif(choice_new=="P"):
        print(40*('='))
        service_clear()
    elif(choice_new=="M"):
        print(40*('='))
        main_menu()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        order_service()

#Display serice price list
def service_list():
    print(myname,",This is the Service prices list")
    print(40*('='))
    service_list=["1.[.Add Tables - 10Tables/RM20]",
               "2.[Add Chair - 40Chairs/RM15]",
               "3.[Add Tables Cloths - 10Cloths/RM10"]
    for list_3 in service_list:
        print(list_3)
    print(40*('='))
    order_service()

#Ask user if he/she wants to add service
def service_add():
    print(myname,",This is the Service adding menu")
    print("What would you like to add?")
    service_table()
    service_chair()
    service_cloths()
    order()

#Ask user if he/she wants to add tables service
def service_table():
    print(myname,",How many Tables would you like to add?")
    print("1.Add 0 Tables")
    print("2.Add 10 Tables")
    print("3.Add 20 Tables")
    print("4.Add 30 Tables")
    choice=int(input("Your Choice?:\n"))
    if(choice==1):
        global table_price
        table_price = 0
        global table_int
        table_int = 0
        print(40*('='))
        table_price = int(0)
        table_int = 0
        service_chair()
    elif(choice==2):
        table_price = 0
        table_int = 0
        print(40*('='))
        table_price = 20
        table_int = 10
        service_chair()
    elif(choice==3):
        table_price = 0
        table_int = 0
        print(40*('='))
        table_price = 40
        table_int = 20
        service_chair()
    elif(choice==4):
        table_price = 0
        table_int = 0
        print(40*('='))
        table_price = 60
        table_int = 30
        service_chair()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        service_table()

#Ask user if he/she wants to add chair services        
def service_chair():
    print(myname,",How many Chairs would you like to add?")
    print("1.Add 0 Chairs")
    print("2.Add 40 Chairs")
    print("3.Add 80 Chairs")
    print("4.Add 120 Chairs")
    choice=int(input("Your Choice?:\n"))
    if(choice==1):
        global chair_price
        chair_price = 0
        global chair_int
        chair_int = 0
        print(40*('='))
        chair_price = 0
        chair_int = 0
        service_cloths()
    elif(choice==2):
        chair_price = 0
        chair_int = 0
        print(40*('='))
        chair_price = 15
        chair_int = 40
        service_cloths()
    elif(choice==3):
        chair_price = 0
        chair_int = 0
        print(40*('='))
        chair_price = 30
        chair_int = 80
        service_cloths()
    elif(choice==4):
        chair_price = 0
        chair_int = 0
        print(40*('='))
        chair_price = 45
        chair_int = 120
        service_cloths()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        service_chair()

#Ask user if he/she wants to add cloths services     
def service_cloths():
    print(myname,",How many Cloths would you like to add?")
    print("1.Add 0 Cloths")
    print("2.Add 10 Cloths")
    print("3.Add 20 Cloths")
    print("4.Add 30 Cloths")
    choice=int(input("Your Choice?:\n"))
    if(choice==1):
        global cloths_price
        cloths_price = 0
        global cloths_int
        cloths_int = 0
        print(40*('='))
        cloths_price = 0
        cloths_int = 0
        print("Added to payment!")
        print(40*('='))
        main_menu()
    elif(choice==2):
        cloths_price = 0
        cloths_int = 0
        print(40*('='))
        cloths_price = 10
        cloths_int = 10
        print("Added to payment!")
        print(40*('='))
        main_menu()
    elif(choice==3):
        cloths_price = 0
        cloths_int = 0
        print(40*('='))
        cloths_price = 20
        cloths_int = 20
        print("Added to payment!")
        print(40*('='))
        main_menu()
    elif(choice==4):
        cloths_price = 0
        cloths_int = 0
        print(40*('='))
        cloths_price = 30
        cloths_int = 30 
        print("Added to payment!")
        print(40*('='))
        print("To clear the service, simply reinput 0(1) in the service order :)")
        print(40*('='))
        main_menu()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        service_cloths()

#Display the payment menu
def payment():
    print(myname,",This is the Payment menu")
    print("What would you like to do?")
    print("T-Display total amount")
    print("P-Make Payment")
    print("M-Back to Main menu")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="T"):
        print(40*('='))
        payment_total()
    elif(choice_new=="P"):
        print(40*('='))
        payment_pay()
    elif(choice_new=="M"):
        print(40*('='))
        main_menu()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        payment()

#Display the total amount of cost
def payment_total():
    global total_sum
    global total_add
    total_add = 0
    total_sum = 0
    total_add = breakfast_total+lunch_total+table_price+chair_price+cloths_price
    total_sum = total_add
    if(total_sum==0):
        print(myname,",you havent order anything yet")
        print(40*('='))
        main_menu()
    elif(total_sum>0):
        print("This payment is before the discount and gst is applied")
        print("The total payment you have to pay is:")
        print("RM. %0.2f"%total_sum)
        print(40*('='))
        main_menu()
    else:
        print

#Ask user how much he/she would like to pay
def payment_pay():
    global pay_tot
    global refund
    refund = 0
    print(myname,",This is the Payment menu")
    print("Be sure to check the invoice before paying")
    print("To cancel the payment,type 0 in the input")
    print(40*('='))
    pay_tot=float(input("How much do you want to pay?:\nRM "))
    if(pay_tot>=total_pay_new): 
        refund = pay_tot - total_pay_new
        print(40*('='))
        print("Thank you for coming",myname,",you'll get"" RM %0.2f"%refund,"as a change")
        print(40*('='))
        main_menu()
    else:
        print(40*('='))
        print("You got no enough money to pay the bill")
        print("Cancelled Payment")
        print(40*('='))
        main_menu()

#Display Promotion
def promotion():
    print("Our Promotion are listed below:")
    print(40*('-'))
    print("Customer with 10-25 people/guest will get 5% discount")
    print("Customer with 26-50 people/guest will get 10% discount")
    print("Customer with 51-100 people/guest will get 15% discount")
    print("Customer with +100 people/guest will get 20% discount")
    print("*With a minimal total amount of RM200")
    print(40*('-'))
    print("Customer with less than 10 people will get 10% discount")
    print("*With a minimal total amount of RM50")
    print(40*('='))
    main_menu()

#Display Report menu
def report():
    print(myname,",This is the Report menu")
    print("What would you like to do?")
    print("I-Display invoice for order made")
    print("S-Display the summary of orders and payment made")
    print("M-Back to Main menu")
    print()
    choice=str(input("Your Choice?:\n"))
    choice_new = choice.upper()
    if(choice_new=="I"):
        print(40*('='))
        report_invoice()
    elif(choice_new=="S"):
        print(40*('='))
        report_summary()
    elif(choice_new=="M"):
        print(40*('='))
        main_menu()
    else:
        print(40*('='))
        print("Wrong input/type!")
        print(40*('='))
        report()

#Display Invoice bill
def report_invoice():
    import time
    print("This is your invoice:")
    print(80*('-'))
    print("\t\t\tInvoice")
    print(80*('-'))
    print("\t\t\tRequiem Restaurant")
    print("Name:",myname)
    localdate = time.strftime("%x")
    print("Date:",localdate)
    localtime = time.strftime("%I:%M:%S")
    print("Time:",localtime)
    print("Invoice Number: 000000001")
    print(80*('-'))
    print("Description:\t\tQuantity:\tUnit Price:\t\tAmount:")
    invoice_breakfast()
    invoice_lunch()
    invoice_service1()
    invoice_service2()
    invoice_service3()
    invoice_food()
    invoice_gst()
    total_bayar()
    print(80*('-'))
    print(40*('='))
    main_menu()
        
#Display Breakfast set in the invoice
def invoice_breakfast():
    if(breakfast_set>0):
        print(80*('-'))
        print("Breakfast set:\t\t",breakfast_set,"\t\tRM 30.00\t\tRM %0.2f"%int(breakfast_set*30))
        print(80*('-'))
        print("Nasi Lemak\t\t",int(2*breakfast_set))
        print("Nasi Ayam\t\t",int(1*breakfast_set))
        print("Roti Bakar\t\t",int(1*breakfast_set))
        print("Roti Channai\t\t",int(1*breakfast_set))
        print("Sandwich\t\t",int(1*breakfast_set))
        print("Ice Tea\t\t\t",int(3*breakfast_set))
        print("Tehtong\t\t\t",int(3*breakfast_set))
    else:
        print


#Display Lunch set in the invoice
def invoice_lunch():
    if(lunch_set>0):
        print(80*('-'))
        print("Lunch set:\t\t",lunch_set,"\t\tRM 60.00\t\tRM %0.2f"%int(lunch_set*60))
        print(80*('-'))
        print("Marmite Fish Rice\t",int(2*lunch_set))
        print("Fish and Chip\t\t",int(1*lunch_set))
        print("Baked Rice\t\t",int(2*lunch_set))
        print("Chicken Steak\t\t",int(1*lunch_set))
        print("Fu Yong Hai with Rice\t",int(1*lunch_set))
        print("Ice Tea\t\t\t",int(4*lunch_set))
        print("Tehtong\t\t\t",int(3*lunch_set))
    else:
        print


#Display Tables service in the invoice
def invoice_service1():
    print(80*('-'))
    print("Services:")
    if(table_int==0):
        print
    elif(table_int==10):
        print("Add Tables\t\t 10\t\tRM 20.00""\t\tRM 20.00")
    elif(table_int==20):
        print("Add Tables\t\t 20\t\tRM 20.00""\t\tRM 40.00")
    elif(table_int==30):
        print("Add Tables\t\t 30\t\tRM 20.00""\t\tRM 60.00")
    else:
        print
        
#Display Chair service in the invoice
def invoice_service2():
    if(chair_int==0):
        print
    elif(chair_int==40):
        print("Add Chairs\t\t 40\t\tRM 15.00""\t\tRM 15.00")
    elif(chair_int==80):
        print("Add Chairs\t\t 80\t\tRM 15.00""\t\tRM 30.00")
    elif(chair_int==120):
        print("Add Chairs\t\t 120\t\tRM 15.00""\t\tRM 45.00")
    else:
        print

#Display Table Cloths service in the invoice
def invoice_service3():
    global cloths_sum
    cloths_sum = 0
    if(cloths_int==0):
        print
    elif(cloths_int==10):
        print("Add Cloths\t\t 10\t\tRM 10.00""\t\tRM 10.00")
        cloths_sum = 10
    elif(cloths_int==20):
        print("Add Cloths\t\t 20\t\tRM 10.00""\t\tRM 20.00")
        cloths_sum = 20
    elif(cloths_int==30):
        print("Add Cloths\t\t 30\t\tRM 10.00""\t\tRM 30.00")
        cloths_sum = 30
    else:
        print

#Display Discount in the invoice
def invoice_food():
    global total_food
    print(80*('-'))
    total_food = int(breakfast_total+lunch_total)
    if(customer<10 and total_food>=50):
        print("Discount 10%""\t\t\t\t\t\t\tRM",total_food*0.1,("-"))
        print("on Food&Drinks")
    elif(customer>=10 and customer<=25 and total_food>=200):
        print("Discount 5%""\t\t\t\t\t\t\tRM",total_food*0.05,("-"))
        print("on Food&Drinks")
    elif(customer>=26 and customer<=50 and total_food>=200):
        print("Discount 10%""\t\t\t\t\t\t\tRM",total_food*0.1,("-"))
        print("on Food&Drinks")
    elif(customer>=51 and customer<=100 and total_food>=200):
        print("Discount 15%""\t\t\t\t\t\t\tRM",total_food*0.15,("-"))
        print("on Food&Drinks")
    elif(customer>100 and total_food>=200):
        print("Discount 20%""\t\t\t\t\t\t\tRM",total_food*0.2,("-"))
        print("on Food&Drinks")
    else:
        print("No Discount""\t\t\t\t\t\t\tRM 0 -")
        print("on Food&Drinks")

#Display GST in the invoice
def invoice_gst():
    print(80*('-'))
    if(total_sum>0):
        print("GST 6%:\t\t\t\t\t\t\t\tRM",total_sum*6/100)
        print(80*('-'))    
    else:
        print("GST 6%:\t\t\t\t\t\t\t\tRM",000/100)
        print(80*('-'))    

#Display Total sum in the invoice
def total_bayar():
    global total_pay_new
    total_pay_new = 0
    global gst_total
    gst_total = total_sum*6/100
    if(customer<10 and total_food>=50):
        print("Total Payment:""\t\t\t\t\t\t\tRM",(total_sum-total_food*0.1)+(total_sum*0.06))
        total_pay_new=(total_sum-total_food*0.1)+(total_sum*6/100)
        print(80*('-'))
    elif(customer>=10 and customer<=25 and total_food>=200):
         print("Total Payment:""\t\t\t\t\t\t\tRM",(total_sum-total_food*0.05)+(total_sum*0.06))
         total_pay_new=(total_sum-total_food*0.05)+(total_sum*6/100)
         print(80*('-'))
    elif(customer>=26 and customer<=50 and total_food>=200):
         print("Total Payment:""\t\t\t\t\t\t\tRM",(total_sum-total_food*0.1)+(total_sum*0.06))
         total_pay_new=(total_sum-total_food*0.1)+(total_sum*6/100)
         print(80*('-'))
    elif(customer>=51 and customer<=100 and total_food>=200):
        print("Total Payment:""\t\t\t\t\t\t\tRM",(total_sum-total_food*0.15)+(total_sum*0.06))
        total_pay_new=(total_sum-total_food*0.15)+(total_sum*6/100)
        print(80*('-'))
    elif(customer>100 and total_food>=200):
         print("Total Payment:""\t\t\t\t\t\t\tRM",(total_sum-total_food*0.2)+(total_sum*0.06))
         total_pay_new=(total_sum-total_food*0.2)+(total_sum*6/100)
         print(80*('-'))
    else:
         print("Total Payment:""\t\t\t\t\t\t\tRM",(total_sum+(total_sum*0.06)))
         total_pay_new=(total_sum+(total_sum*0.06))

#Display Summary
def report_summary():
    import time
    print("This is your Purchase summary")
    if(pay_tot>0):
        print(80*('-'))
        print("\t\t\tRequiem Restaurant")
        print(80*('-'))
        print("Name:",myname)
        localdate = time.strftime("%x")
        print("Date:",localdate)
        localtime = time.strftime("%I:%M:%S")
        print("Time:",localtime)
        print("Invoice Number: 000000001")
        print(80*('-'))
        print("Description:\t\tQuantity:\t\tAmount:")
        print(80*('-'))
        breakfast_summary()
        lunch_summary()
        service1_summary()
        service2_summary()
        service3_summary()
        discount_summary()
        summary_gst()
        summary_total()
        summary_payment()
        summary_changes()
        print(80*('-'))
        print("\t\t\tThank you for coming!")
        print(40*('='))
        
        main_menu()
    else:
        print("Cant show summary yet if you havent pay in the payment menu :)")
        print(40*('='))
        main_menu()

#Display Breakfast set in the summary        
def breakfast_summary():
    if(breakfast_set>0):
        print("Breakfast set\t\t",breakfast_set,"\t\t\tRM %0.2f"%int(breakfast_set*30))
        print(80*('-'))
    else:
        print

#Display Lunch set in the summary        
def lunch_summary():
    if(lunch_set>0):
        print("Lunch set\t\t",lunch_set,"\t\t\tRM %0.2f"%int(lunch_set*60))
        print(80*('-'))
    else:
        print

#Display Tables service in the summary
def service1_summary():
    if(table_int==0):
        print
    elif(table_int==10):
        print("Add Tables\t\t10\t\t\tRM 20.00")
        print(80*('-'))
    elif(table_int==20):
        print("Add Tables\t\t20\t\t\tRM 40.00")
        print(80*('-'))
    elif(table_int==30):
        print("Add Tables\t\t30\t\t\tRM 60.00")
        print(80*('-'))
    else:
        print

#Display Chair service in the summary       
def service2_summary():
    if(chair_int==0):
        print
    elif(chair_int==40):
        print("Add Chairs\t\t40\t\t\tRM 15.00")
        print(80*('-'))
    elif(chair_int==80):
        print("Add Chairs\t\t80\t\t\tRM 30.00")
        print(80*('-'))
    elif(chair_int==120):
        print("Add Chairs\t\t120\t\t\tRM 45.00")
        print(80*('-'))
    else:
        print

#Display Cloths service in the summary              
def service3_summary():
    if(cloths_int==0):
        print
    elif(table_int==10):
        print("Add Cloths\t\t10\t\t\tRM 10.00")
        print(80*('-'))
    elif(table_int==20):
        print("Add Cloths\t\t20\t\t\tRM 20.00")
        print(80*('-'))
    elif(table_int==30):
        print("Add Cloths\t\t30\t\t\tRM 30.00")
        print(80*('-'))
    else:
        print

#Display Discount in the summary
def discount_summary():
    if(customer<10 and total_food>=50):
        print("Discount 10% on Food&Drinks""\t\t\tRM",total_food*0.1,"-")
        print(80*('-'))
    elif(customer>=10 and customer<=25 and total_food>=200):
        print("Discount 5% on Food&Drinks""\t\t\tRM",total_food*0.05,"-")
        print(80*('-'))
    elif(customer>=26 and customer<=50 and total_food>=200):
        print("Discount 10% on Food&Drinks""\t\t\tRM",total_food*0.1,"-")
        print(80*('-'))
    elif(customer>=51 and customer<=100 and total_food>=200):
        print("Discount 15% on Food&Drinks""\t\t\tRM",total_food*0.15,"-")
        print(80*('-'))
    elif(customer>100 and total_food>=200):
        print("Discount 20% on Food&Drinks""\t\t\tRM",total_food*0.2,"-")
        print(80*('-'))
    else:
        print("No Discount on Food&Drinks""\t\t\tRM 0 -")
        print(80*('-'))

#Display Tables service in the summary
def summary_gst():
    if(total_sum>0):
        print("GST 6%:\t\t\t\t\t\tRM",total_sum*0.06)
        print(80*('-'))    
    else:
        print("GST 6%:\t\t\t\t\t\tRM")
        print(80*('-')) 

#Display Total amount in the summary
def summary_total():
    if(customer<10 and total_food>=50):
        print("Total Payment:""\t\t\t\t\tRM",(total_sum-total_food*0.1)+(total_sum*0.06))
        total_pay_new=(total_sum-total_food*0.1)+(total_sum*0.06)
        print(80*('-'))
    elif(customer>=10 and customer<=25 and total_food>=200):
         print("Total Payment:""\t\t\t\t\tRM",(total_sum-total_food*0.05)+(total_sum*0.06))
         total_pay_new=(total_sum-total_food*0.05)+(total_sum*0.06)
         print(80*('-'))
    elif(customer>=26 and customer<=50 and total_food>=200):
         print("Total Payment:""\t\t\t\t\tRM",(total_sum-total_food*0.1)+(total_sum*0.06))
         total_pay_new=(total_sum-total_food*0.1)+(total_sum*0.06)
         print(80*('-'))
    elif(customer>=51 and customer<=100 and total_food>=200):
        print("Total Payment:""\t\t\t\t\tRM",(total_sum-total_food*0.15)+(total_sum*0.06))
        total_pay_new=(total_sum-total_food*0.15)+(total_sum*0.06)
        print(80*('-'))
    elif(customer>100 and total_food>=200):
         print("Total Payment:""\t\t\t\t\tRM",(total_sum-total_food*0.2)+(total_sum*0.06))
         total_pay_new=(total_sum-total_food*0.2)+(total_sum*0.06)
         print(80*('-'))
    else:
         print("Total Payment:""\t\t\t\t\tRM",(total_sum+(total_sum*0.06)))
         total_pay_new=(total_sum+(total_sum*0.06))
         print(80*('-'))

#Display Payment in the summary
def summary_payment():
    if(pay_tot>0):
        print("Your payment:\t\t\t\t\tRM",pay_tot)
        print(80*('-')) 
    else:
        print("Your Payment:\t\t\t\t\tRM")
        print(80*('-')) 

#Display Payment changes in the summary
def summary_changes():
    if(pay_tot>0):
        print("Your change:\t\t\t\t\tRM",refund*100/100)
        print(80*('-')) 
    else:
        print("Your change:\t\t\t\t\tRM")
        print(80*('-')) 

#Start of Program
my_name()
main_menu()
