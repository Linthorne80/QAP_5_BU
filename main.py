# one stop Insurance company QAP5
#By: Brokelynn upshall
# date: 2023/05/1
# number 1
# One Stop Insurance Company
f = open("OSICDef.dat", "r")
PolicyNum = int(f.readline())
BasicPrem = float(f.readline())
DISCOUNT = float(f.readline())
ExtraCover = float(f.readline())
GlassCover = float(f.readline())
LoanerCover = float(f.readline())
HST = float(f.readline())
ProcessingFee = float(f.readline())
f.close()

#Starting inputs

while True:
    CustFirstName = input("Enter the customers first name: ").title()
    CustLastName = input("Enter last Name: ").title()

    print()

    StAdd = input("Enter the customer's Street Address:                     ").title()
    City = input("Enter the customer's city:                               ").title()

    # Validate the province with a list.
    ProvList = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "NV", "NT"]
    while True:
        Prov = input("Enter the customer's province(LL):                       ").upper()

        if not Prov in ProvList:
            print("Invalid province, please reenter.")
        else:
            break


    while True:
        postcode = input("Enter customer postal code (X9X9X9):        ").upper().replace("-", "").replace(" ", "")
        if len(postcode) > 6:
            print("ERROR: Postal code length exceeds maximum amount (6 characters)")
        elif len(postcode) == 0:
            print("ERROR: Nothing was entered")
        elif postcode[0:5:2].isalpha() is False or postcode[1:6:2].isdigit() is False:
            print("ERROR: Invalid postal code format (X9X9X9)")
        else:
            break

    while True:
        PhNum = input("Enter the customer's phone number(9999999999):           ")
        if PhNum == "":
            print("Cannot be left blank please reenter.")
        elif len(PhNum) != 10:
            print("Phone number must be 10 digits long, please reenter.")
        elif not PhNum.isdigit():
            print("Phone number must be digits(0-9) only, please reenter.")
        else:
            PhNum = "(" + PhNum[0:3] + ")" + PhNum[3:6] + "-" + PhNum[6:10]
            break

    print()
    while True:
        try:
            CarTot = int(input("Enter Number of insured cars: "))
        except:
            print('Invalid input!')
        else:
            if CarTot >= 1:
                break
            else:
                print('Invalid input!')
    while True:
        GlassCov = input("Would you Like optional Glass coverage? Y/N: ")
        GlassCov = GlassCov.upper()
        if GlassCov == 'Y' or GlassCov == 'N':
            break
        else:
            print("Please Enter Y or N")


    while True:
        ExtraLiab = input("Would you like extra Liability up to $1,000,000? Y/N: ")
        ExtraLiab = ExtraLiab.upper()
        if ExtraLiab == 'Y' or ExtraLiab =='N':
            break
        else:
            print("Please Enter Y or N")
    while True:
        LoanerCar = input("Would you like optional loaner car? Y/N: ")
        LoanerCar = LoanerCar.upper()
        if LoanerCar == 'Y' or LoanerCar == 'N':
            break
        else:
            print("Please Enter Y/N")

        # Calculate monthly payments
        ProcessingFee = 39.99

        PaymentMethod = input("Monthly or Full? (M/F): ").upper()
        if PaymentMethod == "M":
            MonthlyPayment = (FinalTotalCost + ProcessingFee) / 8

        elif PaymentMethod == "F":
            PayMsg = "Your Total is {TotalCost}"

        else:
            # noinspection PyUnresolvedReferences
            print("Invalid Payment. Monthly or Full? (M/F): ").Upper()

    #Calculations here
    if CarTot == 1:
        InsPrem = BasicPrem
    if CarTot > 1:
        InsPrem = BasicPrem + (((BasicPrem) * (CarTot - 1)) * DISCOUNT)
    if ExtraLiab.upper() == 'Y':
        ExtraCharge1 = (CarTot * ExtraCover)
    if GlassCov.upper() == 'Y':
        ExtraCharge2 = (CarTot * GlassCover)
    if LoanerCar.upper() == 'Y':
        ExtraCharge3 = (CarTot * LoanerCover)
    print(ExtraCharge1)
    print(InsPrem)
    print(ExtraCharge2)
    print(ExtraCharge3)
    totalextracharge = ExtraCharge1 + ExtraCharge2 + ExtraCharge3
    TotalPrem = InsPrem + totalextracharge
    TAX = TotalPrem * HST
    FinalTotalCost = TotalPrem + TAX
    MonthlyPayment = (FinalTotalCost + 39.99) // 12


#results
    print("ONE STOP INSURANCE COMPANY")
    print("POLICY LISTING AS OF dd-mon-yy")
    print()
    print("POLICY CUSTOMER             INSURANCE     EXTRA     TOTAL PREMIUM")
    print("NUMBER NAME                 PREMIUM       COSTS                  ")
    print("=============================================================================")
    print("")
    print("".format(PolicyNum, CustFirstName, CustLastName, InsPrem, FinalTotalCost, TotalPrem))

    # Save the data for the claim to a data file.
    f = open("Policies.dat", "a")
    f.write("{},".format(str(PolicyNum)))
    f.write("{},".format(CustFirstName))
    f.write("{},".format(CustLastName))
    f.write("{},".format(StAdd))
    f.write("{},".format(City))
    f.write("{},".format(Prov))
    f.write("{},".format(postcode))
    f.write("{},".format(float(CarTot)))
    f.write("{},".format(str(ExtraLiab)))
    f.write("{},".format(str(GlassCov)))
    f.write("{},".format(str(LoanerCar)))
    f.close()

    print()
    print("Policy information processed and saved.")

    while True:
        ProgramCont = input("Would you like to continue the program? Y/N: ")
        ProgramCont = ProgramCont.upper()
        if ProgramCont != "Y" and ProgramCont != "N":
            print("Please press Y or N")
            continue
        elif ProgramCont == "N":
            PolicyNum += 1
            break
        elif ProgramCont == "Y":
            PolicyNum += 1
            break
    if ProgramCont == "Y":
        continue

#writing back to to OSICDef.dat
    f = open("OSICDef.dat", "w")
    f.write(f"{PolicyNum}\n")
    f.write(f"{BasicPrem:,.2f}\n")
    f.write(f"{DISCOUNT:,.2f}\n")
    f.write(f"{ExtraCover:,.2f}\n")
    f.write(f"{GlassCover:,.2f}\n")
    f.write(f"{LoanerCover:,.2f}\n")
    f.write(f"{HST:,.2f}\n")
    f.write(f"{ProcessingFee:,.2f}\n")
    f.close()