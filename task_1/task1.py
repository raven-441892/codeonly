#Beckett Pizza Plaza cashier, Chloe The Pizza Price Calculator


def input_validation(a):
    """checks if the user input has any errors or not and runs the code till right entry is taken"""
    while True:
        try:
            user = input(a).lower()
            if user not in ['y','yes','n','no']:
                raise ValueError("Please enter 'y' or 'n'") #if value error not raised then if wrong input is entered then that error raising info runs into infinite loop 
            return user
        except ValueError as e:
            print(f"Invalid input! {e}")

def customer_input():
    """Takes input from the user"""
    
    print("Welcome to Beckett Pizza Plaza")
    print("================================")
    print("Hello Customer, I'm Chloe The Pizza Price Calculator\n")
    while True:
        try: 
            number_of_pizza = int(input("How many pizzas ordered? "))
            if number_of_pizza < 0:
                print("Please enter a positive integer!")
            else:
                delivery = input_validation("Is delivery required? (y/n): ")
                day = input_validation("Is it Tuesday? (y/n): ")
                app = input_validation("Did the customer use the BPP app? (y/n): ")
                return number_of_pizza, delivery, day, app
        except ValueError as v:
            print("Something went wrong: ", v)


def pizza_price(number_of_pizza):
    """ Calculation for the pizza price only without any discount """
    pizza_price_per_piece=12
    total=pizza_price_per_piece*number_of_pizza
    return total

def tuesday_discount_offer(day,total):
    """ Calculation for the pizza price with Tuesday discount offer"""
    if day.lower()=="y" or day.lower()=="yes":
        tuesday_discount= total*0.5
        return tuesday_discount
    else:
        return 0
    
def delivery_charge(number_of_pizza,delivery):
    """ Calculation for pizza price weather to add delivery charge or not"""
    if delivery.lower()=="y" or delivery.lower()=="yes":
        if number_of_pizza>=5:
            return 0
        else:
            delivery_amt=2.50
            return delivery_amt
                 
    else:
        return 0

def app_discount(app, total, delivery_amt, day):
    """Calculate the app discount"""
    if app.lower() == "y" or app.lower()=="yes":
        if day.lower() == "y":
            discount_price_tuesday = (total + delivery_amt) * 0.5
            app_discount_price = discount_price_tuesday * 0.25
        else:
            app_discount_price = (total + delivery_amt) * 0.25
        return app_discount_price
    return 0


def calculation(total, tuesday_discount, delivery_amt, app_discount_price):
    """Calculate the total price with above present discounts"""
    grand_total = total
    
    if tuesday_discount > 0:
        grand_total -= tuesday_discount
        
    grand_total += delivery_amt
    
    if app_discount_price > 0:
        grand_total -= app_discount_price
    
    return grand_total

                     
def output(total,tuesday_discount,delivery_amt,app_discount_price,grand_total):
    """"Displays the grand total of the pizza"""
    print(f"Dear Customer, Your total charge for the order is: \n Total pizza price ---- £{total:.2f} \n Tuesday discount ---- £{tuesday_discount:.2f}\n Delivery charge ---- £{delivery_amt:.2f}\n App discount ---- £{app_discount_price:.2f} \n ==============================\n Grand Total ---- £{grand_total:.2f}")
    print("\nPlease Visit Again !!!\n")
                       
                    
num,delivery,day,app=customer_input()
price=pizza_price(num)
tuesday=tuesday_discount_offer(day,price)
delivery_stuff=delivery_charge(num,delivery)
apps=app_discount(app,price,delivery_stuff,day)
calculate=calculation(price,tuesday,delivery_stuff,apps)
display=output(price,tuesday,delivery_stuff,apps,calculate)

                        
#num=number_of_pizza
# delivery=delivery
# day=day
# app=app
# price=total 
# tuesday=tuesday_discount 
# delivery_stuff=delivery_amt 
# apps=app_discount_price 
# calculate=grand_total              
            
