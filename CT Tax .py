print ("Hello.")
print ("This is a program to calculate a proposed gas tax replacement.")
print ("Thanks")


# defining parameters

mpg_e = 33.70 #this is 33.70 kWh per gallon of gas

ct_kw = 17.55 #17 point 55 cents per kWh

ct_gtr = .38 #CT Gas Tax is 38 cents per gal

c_mpg = int (input("Please enter how many MPG your vehicle gets: "))

convmpg_mpge = int (c_mpg * mpg_e)

milage_d = int(input("How many miles do you drive on average per year? "))

current_tax = int (milage_d / c_mpg * ct_gtr)

# need variable to hold MPGe to total kW conversion
tot_kw = milage_d / convmpg_mpge

yearly_total = int (ct_kw * tot_kw)

def askYesNoQuestion(question):
  YesNoAnswer = input(question).upper()
  if YesNoAnswer == "YES" or YesNoAnswer == "NO":
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)

print ("You currently spend: $", format(current_tax, ",.2f"))

answer = askYesNoQuestion("Are you surprised? (Yes or No)" )
if answer == "YES":
  print ("Of course! With the 38 cents included in the price of gas, you don't really think about it.")
  print ("Driving {} a year at: {} means you use roughly: ".format(milage_d,c_mpg))
  print (milage_d / c_mpg)
  print ("gallons of gas a year.")
if answer == "NO":
    print ("Let's move along then.")

print (
  '''So this proposal is to change by kilowatt hour (kWh) based off yearly usage.
Why (kWh)? Because we can use it across current internal combustion and upcoming electric vehicles.
This is done using MPGe - Miles Per Gallon of gasoline-equivalent.
Gasoline contains 33.70 kWh (33,700) watts of energy''')

print (convmpg_mpge)
# print (format(c_mpg * mpg_e, '.2f'))
print ("This is your MPGe, ")
print ("using your MPGe and your annual mileage we can figure out your kW use:")

#print (format(milage_d / convmpg_mpge, '.2f'))
#print ("We combine this with the ")


print ("Your yearly car cost under this system would be: $", format(yearly_total, ",.2f"))
print ("This change in cost is: $ ")
print (yearly_total - current_tax)