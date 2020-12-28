''' TIME VALUE OF MONEY VALUATION'''


#Input amount desired in the future.

FV = float(input("\n\tInsert the Future Value you desire to aquiere: $"))
while FV <= 0:
    print("\tError. Value must be grater than 0.")
    FV = float(input("\n\tInsert the Future Value you desire to aquiere: $"))
    
    

#Input the amount of periods to invest.
N = float(input("\tInsert the amount of periods you plan to invest: "))
while N <= 0:
    print("\tError. Value must be grater than 0.")
    N = float(input("\n\tInsert the amount of periods you plan to invest: "))
    

#Input the rate of interest
R = float(input("\tInsert the Interest rate: %"))/100

while R <= 0:
     print("\tError. Value must be grater than 0.")
     R = float(input("\tInsert the Interest rate: %"))
    
#Calculate the PV.
PV = FV / (1 + R)**N

#Return values.

print("PV=", format(PV,".2f"))
