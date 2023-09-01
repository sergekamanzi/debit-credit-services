#!/usr/bin/python3
print("DEBIT and CREDIT services")
code = input("enter the code(*182#/*187#/*188#/*189#): ")
if code == "*182#":
   print("1.kinyarwanda")
   print("2.english")
   option_1 = input("choose option: ")
   if option_1 == "1":
      print("1.kugura")
      print("2.kwishyura")
      print("3.asigayeho")
      option_2 = input("hitamo: ")
      print("biraza...(30s)")

   elif option_1 == "2":
      print("1.buy")
      print("2.pay")
      print("3.remaining money")
      option_3 = input("choose option: ")
      print("loading...(30s)")
elif code == "*187#":
   print("here is your total balance on DEBIT/CREDIT card ")
elif code == "*188#":
   print("here is our contact: ")
   print("name: serge kamanzi")
   print("email: s.kamanzi@alustudent.com")
   print("phone: +250780032791")
elif code == "*189#":
   input("enter your request below: \n")
   print("thanks for your request")

else:
   print("invalid code")
