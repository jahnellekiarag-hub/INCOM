print("Kiara Pizza Store")
print("Pizza Flavours (Pepperoni Pizza, Taco Pizza, BBQ Chicken Pizza)")

KiaraFlavor1 = [
    ("Pepperoni", 200, 350, 550),
    ("Taco", 250, 400, 650),
    ("BBQ", 370, 550, 750),
]

KiaraFlavor = input("Enter a Pizza Flavor: ").lower()
KiaraSize = input("Enter size (Small/Medium/Large): ").lower()

KiaraPrice = 0

print("\nReceipt Price")


for pizza in KiaraFlavor1:

    if pizza[0].lower() == KiaraFlavor:

        if KiaraSize == "small":
            KiaraPrice = pizza[1]

        elif KiaraSize == "medium":
            KiaraPrice = pizza[2]

        elif KiaraSize == "large":
            KiaraPrice = pizza[3]

        else:
            print("Invalid size")
            print("Please Try Again")

        break

else:
    print("Invalid Pizza Flavor")


if LuzonPrice > 0:
    print("\n----- RECEIPT -----")
    print(f"Pizza: {KiaraFlavor.title()}")
    print(f"Size: {KiaraSize.title()}")
    print(f"Price: {KiaraPrice}")
    print("Thank you for purchasing!")
