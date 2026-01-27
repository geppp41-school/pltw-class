##############################################################################
# a215_security_checklist.py
##############################################################################

print("Let's check your security. Answer y or n to each of the questions.")

phish = input("Can you recognize phishing emails? ")
pw = input("Is your passord strong? ")
auth = input("Do you use multi-factor authentication? ")
enc = input("Do you know how to encrypt sensitive information? ")

# if (phish =='y'):
#   if (pw =='y'):
#     if (auth == 'y'):
#       if (enc == "y"):
#         print("You have good security habits.")
# else:
#   print("You can improve your security habits.")

good_security_standards = 0
improvements = 0

if(phish == 'y'):
    good_security_standards += 1
else:
    improvements += 1

if (pw =='y'):
    good_security_standards += 1
else:
    improvements += 1

if (auth == 'y'):
    good_security_standards += 1
else:
    improvements += 1

if (enc == "y"):
    good_security_standards += 1
else:
    improvements += 1

print(f"your got {good_security_standards} good security habits")

if(improvements == 0):
    print("you dont seem to need any improvements")
else:
    print(f"you need to imporove on {improvements} things")
