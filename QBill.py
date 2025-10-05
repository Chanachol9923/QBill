import os.path
import time
import datetime
import sys

# ────────────────────────────────────────────────────────────────────────────
# ─██████████████───██████████████───██████████─██████─────────██████─────────
# ─██░░░░░░░░░░██───██░░░░░░░░░░██───██░░░░░░██─██░░██─────────██░░██─────────
# ─██░░██████░░██───██░░██████░░██───████░░████─██░░██─────────██░░██─────────
# ─██░░██──██░░██───██░░██──██░░██─────██░░██───██░░██─────────██░░██─────────
# ─██░░██──██░░██───██░░██████░░████───██░░██───██░░██─────────██░░██─────────
# ─██░░██──██░░██───██░░░░░░░░░░░░██───██░░██───██░░██─────────██░░██─────────
# ─██░░██──██░░██───██░░████████░░██───██░░██───██░░██─────────██░░██─────────
# ─██░░██──██░░██───██░░██────██░░██───██░░██───██░░██─────────██░░██─────────
# ─██░░██████░░████─██░░████████░░██─████░░████─██░░██████████─██░░██████████─
# ─██░░░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─████████████████─████████████████─██████████─██████████████─██████████████─
# ────────────────────────────────────────────────────────────────────────────


ServiceC = 0

def FFileCheck(File) :
    Check = os.path.isfile(File)
    return (Check)
def FOdinals(i) :
    if i == 1:
        Odinals = "st"
    elif i == 2:
        Odinals = "nd"
    elif i == 3:
        Odinals = "rd"
    else:
        Odinals = "th"

    return (Odinals)
def FCreateProfile() :
    try :
        os.remove("Profile.txt")
    except FileNotFoundError:
        pass
    os.system('cls')
    print("")
    print("==================================================")
    print("              Create New Profile! \n       Lets setup your buffet restaurant! ")
    print("==================================================")

    try :
        with open("Profile.txt", "w") as Profile:
            PackageAmt = int(input("How many Buffet Packages does your restaurant have? : "))
            print("")
            PackageList = []
            for i in range (PackageAmt) :
                i += 1
                Odinals = FOdinals(i)

                PackagePrice = float(input("    What is your "+str(i)+Odinals+" Package Price? : "))
                PackageList.append(PackagePrice)
                #print(PackageList[i - 1])
                Profile.write(str(PackageList[i-1])+" ")

            print("==================================================")
            time.sleep(0.5)
            os.system('cls')
            print("")
            Table = int(input("How many table you have in your restaurant? : "))
            time.sleep(0.5)
            os.system('cls')
            print("")
            ServiceC = float(input("Service Charge in percentage, if none type 0 (Enter only number) : "))
            print("")
            ServiceC/=100
            Profile.write("\n" + str(Table) + "\n" + str(ServiceC))

            IsVat = (input("Enable VAT7% or not? (Y/N) : ")).upper()
            print("==================================================")
            if IsVat == "Y" :
                Profile.write("\n" + "0.07")
            elif IsVat == "N" :
                Profile.write("\n" + "0")
            else:
                print("                 Invalid Command \n Vat is Disable come back and fix later in the menu")
                Profile.write("\n" + "0")
        time.sleep(0.5)
        os.system('cls')
        FShowProfileInfo()

        IsCorrect = input("Is your profile correct? (Y/N) : ").upper()

        if IsCorrect == "Y" :
            print("====================================================================================================")
            print('                       Your restaurant profile is setup successfully!\n If you want to edit your restaurant profile you can go to "New Profile" in "View Profile" section')
            print("====================================================================================================")
            time.sleep(2)
            FMainMenu()

        else:
            print("")
            print("==================================================")
            print("                 Let try again!")
            os.remove("Profile.txt")
            print("==================================================")
            time.sleep(0.5)
            os.system('cls')
            FCreateProfile()

    except ValueError:
        os.system('cls')
        print("")
        print("==================================================")
        print("*"*50)
        print(" >>>>>> Invalid Value ,Please Try again!.. <<<<<< ")
        print("*"*50)
        FCreateProfile()
def FShowProfileInfo() :
    with open("Profile.txt", "r") as Profile:
        Data = Profile.read().splitlines()
        PackageData = Data[0].split()
        print("                  Your Profile")
        print("==================================================")
        print("You got ",len(PackageData)," Packages")
        for i in range(len(PackageData)) :
            print("%-4s %-1d %-0s %-1s %.2f %-1s" %("Your ",i+1 ,FOdinals(i+1), "Package is ",float(PackageData[i])," Bath"))
        print("")
        print("You have",Data[1],"Tables\n")
        print("%-5s %.2f %-10s" %("Service Charge is ",(float(Data[2])*100),"%"))
        print("%-1s %.1f %-1s" %("VAT ",(float(Data[3])*100),"%"))
        print("==================================================")
def FMainMenu():
    try:
        os.system('cls')

        print("\n   >>>>> Select Menu below <<<<< ")
        print("")
        print("     Open New Bill   : Press O ")
        print("     Close Bill      : Press C ")
        print("     Table Status    : Press T ")
        print("     Que             : Press Q ")
        print("")
        print("     Summary         : Press S ")
        print("     View Profile    : Press V ")
        print("")
        print("     End Program     : Press E ")
        print("")
        Cmd = input("Select Menu ( O C Q S V E ): ").upper()
        if Cmd == "O" :
            os.system('cls')
            print("\n")
            FOpenTable()
        elif Cmd == "V" :
            os.system('cls')
            FShowProfileInfo()
            print("\n     New Profile     : Press N ")
            Cmd = input("\nPress E to exit to Main Menu or Press N to create New Profile : ").upper()
            if Cmd == "N" :
                Check = input("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n > Are you sure you want to create new profile?\n    This process will REPLACE your old profile!\n     And will clear all Data\n\nPress (Y/N) >>>>> ").upper()
                if Check == "Y":

                        CusList.clear()
                        CusAmtList.clear()
                        CusTotalList.clear()
                        CusTotalAndVat.clear()
                        PackageList.clear()
                        QCusList.clear()
                        QCusAmtList.clear()
                        QCusTotalList.clear()
                        QCusTotalAndVat.clear()
                        QPackageList.clear()
                        print(" >>>>> Restart Program To Setup New Profile! <<<<< ")
                        time.sleep(2)
                        P = open("Profile.txt","w")
                        P.close()
                        os.remove("Profile.txt")
                        os.execv(sys.executable, ['QBill.py'] + sys.argv)

                else:
                    FMainMenu()
            else:FMainMenu()
        elif Cmd == "E" :
            print("\n========== Exiting program... ==========")
            time.sleep(2)
            exit()
        elif Cmd == "T" :
            FTableStatus()

        elif Cmd == "C" :
            FCloseTable()

        elif Cmd == "Q" :
            FQ()
        elif Cmd == "S" :
            FSum()
        else:
            print("\n\n          !!!!! Wrong Command! ,Try again !!!!!")
            time.sleep(1)
            FMainMenu()
    except IndexError:
        os.system('cls')
        os.remove("Profile.txt")
        print("\n\n             >>>>> Profile.txt is corrupted <<<<<\n\n                 Let setup your profile again!")
        #print("\n\n                 >>>>> Program Restarting... <<<<<")
        print("                     ======================")
        time.sleep(2)
        FCreateProfile()
def FOpenTable():
    global StrVatSer
    global StrTotal
    print("\n"," "*12,"-"*50)
    print(" "*12,"                    Open Bill")
    print(" "*12,"                    ==========")
    print(" "*12,">>>>> Press E to Exit and go back to Main menu <<<<<")

    with open("Profile.txt", "r") as Profile:
        Data = Profile.read().splitlines()
        PackageData = Data[0].split()
        print(" "*12,"==================================================")
        print(" "*25,"\n         Select 1 from your ", len(PackageData), " Packages","\n")
        for i in range(len(PackageData)):
            print(" "*12,"%-1s %-1d %-0s %-1s %.2f %-1s %-1d" % ("   For ",i + 1, FOdinals(i+1), "Package ", float(PackageData[i]), " Bath :  Press >>> ", i+1))
        print("")
        print(" "*12,"You have",int(Data[1]) - len(CusList),"Tables left\n")
        print(" "*12, len(QCusList), "In Que\n")
        print(" "*12,"==================================================")

    CusPackage = input("\n          Select Package Customer has order or press E to Exit : ").upper()

    try:
        if CusPackage == "E":
            print("\n", " " * 12, "             >>> Exiting <<< ")
            print(" " * 12, "     ===================================== ")
            time.sleep(0.5)
            FMainMenu()

        elif int(CusPackage) <= 0 :
            os.system('cls')
            print("")
            print("     >>>>>>>>>> Invalid Value, Please Enter the right value again <<<<<<<<<< ")
            FOpenTable()

        elif (CusPackage.isdigit()) and 0 < int(CusPackage) <= (len(PackageData)) :

            print("\n\n           > Open Table for how many customers? ")
            CusAmt = input("\n                Put customers amount or press E to Exit : ").upper()

            if int(CusAmt) <= 0:
                os.system('cls')
                print("")
                print("     >>>>>>>>>> Invalid Value, Please Enter the right value again <<<<<<<<<< ")
                FOpenTable()

            elif CusAmt == "E":
                print("\n", " " * 12, "             >>> Exiting <<< ")
                print(" " * 12, "     ===================================== ")
                time.sleep(0.5)
                FMainMenu()

            elif int(CusAmt) > 0:
                global BillCount
                global BillNumber
                global QBillNumber

                if len(QCusList) == 0 :
                    if int(len(CusList)) >= int(Data[1]):
                        BillCount += 1
                        QBillNumber += 1

                        QPackageList.append(CusPackage)
                        QCusList.append(FCustomerNumGen())
                        QCusAmtList.append(int(CusAmt))
                        CusTotal = (int(CusAmt) * (float(PackageData[int(CusPackage) - 1])))
                        QCusTotalList.append(CusTotal)
                        VatSer = int(QCusTotalList[(QBillNumber) - 1]) * (float(Data[2]) + (float(Data[3])))
                        Total = int(QCusTotalList[(QBillNumber) - 1]) + VatSer
                        QCusTotalAndVat.append(Total)
                        StrTotal = (("%.2f") % (Total))
                        StrVatSer = (("%.2f") % (VatSer))

                        print("")
                        print("_" * 55, "\n|", "\n|")
                        print("|", " " * 20, "Bill Number", QCusList[(QBillNumber) - 1])
                        print("|", " " * 20, "================\n|")
                        print("|", " " * 10, QCusAmtList[(QBillNumber) - 1], "Persons")
                        print("|", " " * 10, "Package", PackageData[int(CusPackage) - 1], "Bath each")
                        print("|", " " * 12, QCusTotalList[(QBillNumber) - 1], "Bath\n|\n|")
                        print("|", " " * 10, "%-5s %.2f %-10s" % ("Service Charge is ", (float(Data[2]) * 100), "%"))
                        print("|", " " * 10, "%-1s %.1f %-1s" % ("VAT ", (float(Data[3]) * 100), "%"))
                        print("|", " " * 12, StrVatSer, "Bath")
                        print("|", "\n|", " " * 15, "Total Price ", StrTotal, "Bath")
                        print("|", " " * 14, "============================\n|")
                        print("_" * 55)

                        print("\n\n             Printing out bill ...")  # จำลองการปริ้นบิลนะครับ 5555
                        time.sleep(0.5)
                        print(CusList, "\n", QCusList)
                        input("\n         Press Enter to continue...")

                        os.system('cls')
                        print("\n")
                        FMainMenu()

                    else :
                        BillCount += 1
                        BillNumber += 1

                        PackageList.append(CusPackage)
                        CusList.append(FCustomerNumGen())
                        CusAmtList.append(int(CusAmt))
                        CusTotal = (int(CusAmt) * (float(PackageData[int(CusPackage) - 1])))
                        CusTotalList.append(CusTotal)
                        VatSer = int(CusTotalList[(BillNumber) - 1]) * (float(Data[2]) + (float(Data[3])))
                        Total = int(CusTotalList[(BillNumber) - 1]) + VatSer
                        CusTotalAndVat.append(Total)
                        StrTotal = (("%.2f") % (Total))
                        StrVatSer = (("%.2f") % (VatSer))

                        print("")
                        print("_" * 55, "\n|", "\n|")
                        print("|", " " * 20, "Bill Number", CusList[(BillNumber) - 1])
                        print("|", " " * 20, "================\n|")
                        print("|", " " * 10, CusAmtList[(BillNumber) - 1], "Persons")
                        print("|", " " * 10, "Package", PackageData[int(CusPackage) - 1], "Bath each")
                        print("|", " " * 12, CusTotalList[(BillNumber) - 1], "Bath\n|\n|")
                        print("|", " " * 10, "%-5s %.2f %-10s" % ("Service Charge is ", (float(Data[2]) * 100), "%"))
                        print("|", " " * 10, "%-1s %.1f %-1s" % ("VAT ", (float(Data[3]) * 100), "%"))
                        print("|", " " * 12, StrVatSer, "Bath")
                        print("|", "\n|", " " * 15, "Total Price ", StrTotal, "Bath")
                        print("|", " " * 14, "============================\n|")
                        print("_" * 55)

                        print("\n\n             Printing out bill ...")  # จำลองการปริ้นบิลนะครับ 5555
                        time.sleep(0.5)
                        print(CusList, "\n", QCusList)
                        input("\n         Press Enter to continue...")

                        os.system('cls')
                        print("\n")
                        FMainMenu()

                elif len(QCusList) > 0 and len(CusList) == 0:
                    QBillNumber += 1
                    BillCount += 1

                    QPackageList.append(CusPackage)
                    QCusList.append(FCustomerNumGen())
                    QCusAmtList.append(int(CusAmt))
                    CusTotal = (int(CusAmt) * (float(PackageData[int(CusPackage) - 1])))
                    QCusTotalList.append(CusTotal)
                    VatSer = int(QCusTotalList[(QBillNumber) - 1]) * (float(Data[2]) + (float(Data[3])))
                    Total = int(QCusTotalList[(QBillNumber) - 1]) + VatSer
                    QCusTotalAndVat.append(Total)
                    StrTotal = (("%.2f") % (Total))
                    StrVatSer = (("%.2f") % (VatSer))

                    print("")
                    print("_" * 55, "\n|", "\n|")
                    print("|", " " * 20, "Bill Number", QCusList[(QBillNumber) - 1])
                    print("|", " " * 20, "================\n|")
                    print("|", " " * 10, QCusAmtList[(QBillNumber) - 1], "Persons")
                    print("|", " " * 10, "Package", PackageData[int(CusPackage) - 1], "Bath each")
                    print("|", " " * 12, QCusTotalList[(QBillNumber) - 1], "Bath\n|\n|")
                    print("|", " " * 10, "%-5s %.2f %-10s" % ("Service Charge is ", (float(Data[2]) * 100), "%"))
                    print("|", " " * 10, "%-1s %.1f %-1s" % ("VAT ", (float(Data[3]) * 100), "%"))
                    print("|", " " * 12, StrVatSer, "Bath")
                    print("|", "\n|", " " * 15, "Total Price ", StrTotal, "Bath")
                    print("|", " " * 14, "============================\n|")
                    print("_" * 55)

                    print("\n\n             Printing out bill ...")  # จำลองการปริ้นบิลนะครับ
                    time.sleep(0.5)
                    input("\n         Press Enter to continue...")

                    os.system('cls')
                    print("\n")
                    FMainMenu()

                else :
                    BillCount += 1
                    QBillNumber += 1

                    QPackageList.append(CusPackage)
                    QCusList.append(FCustomerNumGen())
                    QCusAmtList.append(int(CusAmt))
                    CusTotal = (int(CusAmt) * (float(PackageData[int(CusPackage) - 1])))
                    QCusTotalList.append(CusTotal)
                    VatSer = int(QCusTotalList[(QBillNumber) - 1]) * (float(Data[2]) + (float(Data[3])))
                    Total = int(QCusTotalList[(QBillNumber) - 1]) + VatSer
                    QCusTotalAndVat.append(Total)
                    StrTotal = (("%.2f") % (Total))
                    StrVatSer = (("%.2f") % (VatSer))

                    print("")
                    print("_" * 55, "\n|", "\n|")
                    print("|", " " * 20, "Bill Number", QCusList[(QBillNumber) - 1])
                    print("|", " " * 20, "================\n|")
                    print("|", " " * 10, QCusAmtList[(QBillNumber) - 1], "Persons")
                    print("|", " " * 10, "Package", PackageData[int(CusPackage) - 1], "Bath each")
                    print("|", " " * 12, QCusTotalList[(QBillNumber) - 1], "Bath\n|\n|")
                    print("|", " " * 10, "%-5s %.2f %-10s" % ("Service Charge is ", (float(Data[2]) * 100), "%"))
                    print("|", " " * 10, "%-1s %.1f %-1s" % ("VAT ", (float(Data[3]) * 100), "%"))
                    print("|", " " * 12, StrVatSer, "Bath")
                    print("|", "\n|", " " * 15, "Total Price ", StrTotal, "Bath")
                    print("|", " " * 14, "============================\n|")
                    print("_" * 55)

                    print("\n\n             Printing out bill ...")  # จำลองการปริ้นบิลนะครับ 5555
                    time.sleep(0.5)
                    print(CusList, "\n", QCusList)
                    input("\n         Press Enter to continue...")

                    os.system('cls')
                    print("\n")
                    FMainMenu()

        else:
            try:
                os.system('cls')
                print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
                print(" >>>>> There's no package number ", CusPackage, " Please enter only package you have! <<<<<")
                FOpenTable()
            except ValueError :
                print("\n\n          !!!!! Wrong Command! ,Try again !!!!!")
                time.sleep(1)
                FOpenTable()

    except ValueError:
        print("\n\n          !!!!! Wrong Command! ,Try again !!!!!")
        time.sleep(1)
        os.system('cls')
        FOpenTable()
    except IndexError: FMainMenu()
def FTableStatus():
    os.system('cls')
    with open("Profile.txt", "r") as Profile:
        Data = Profile.read().splitlines()
        PackageData = Data[0].split()
        print("")
        print("                    Table Status")
        print("                    ============\n")
        print("             There are ",len(CusList),"Tables in used" )
        print("            And you have", int(Data[1]) - len(CusList), "Tables left")
        print("                   ",len(QCusList),"Bills In Que\n")
        print("     ========== Active Customer Number ==========")
        for i in range (len(CusList)):
            print(" >>> Bill Number",CusList[i]," | ",CusAmtList[i]," Person  |  Package ",PackageList[i]," |  Total ",CusTotalAndVat[i],"Bath")
    print("\n\n > Close Bill Press C ")
    Cmd = input("\n Input command or press E to Exit : ").upper()
    if Cmd == "E" :
        print("\n"," "*12,"          >>> Exiting Table status <<< ")
        print(" "*12,"       ===================================== ")
        time.sleep(0.5)
        FMainMenu()
    elif Cmd == "C":
        FCloseTable()
    else:
        print("          !!!!! Wrong Command! ,Try again !!!!!")
        time.sleep(1)
        FCloseTable()
def FFirstRun():
    ProfileFCheck = FFileCheck("Profile.txt")
    if ProfileFCheck == False:
        try:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n **  Look like you don't have any profile yet! ** ")
            FCreateProfile()
        except ValueError:
            os.system('cls')
            print("")
            print("==================================================")
            print("*" * 50)
            print(" >>>>>> Invalid Value ,Please Try again!.. <<<<<< ")
            print("*" * 50)
            os.remove("Profile.txt")
            FCreateProfile()
        except KeyboardInterrupt:
            os.system('cls')
            print("")
            print("\n", "*" * 50)
            print("         Invalid Value ,Please Try again...")
            print("", "*" * 50)
            os.remove("Profile.txt")
        except FileNotFoundError:
            os.system('cls')
            print("")
            print("==================================================")
            print("*" * 50)
            print(">>> Invalid Value ,Please Try again!.. <<<")
            print("*" * 50)
            FCreateProfile()

    else:
        print("         Welcome to QBill !!\nYour restaurant Que and Bill assistant")
        FMainMenu()
def FCustomerNumGen():
    CusNum = (str(BillCount).zfill(4))
    return (CusNum)

def FFileNameDate():
    Date = datetime.date.today()
    DateNum = Date.strftime("%d%m%y")
    print(DateNum)
def FCloseTable() :
    os.system('cls')
    import datetime
    global DateFormat

    print("")
    print("\n","-"*60)
    print("                         Close Table")
    print("                         ===========")
    print("     >>>>> Press E to Exit and go back to Main menu <<<<<\n")
    with open("Profile.txt", "r") as Profile:
        Data = Profile.read().splitlines()
        print("")
        print("                         Table Status")
        print("                         ============\n")
        print("                  There are ",len(CusList),"Tables in used" )
        print("                 And you have", int(Data[1]) - len(CusList), "Tables left\n")
        print("            ========== Active Bill Number ==========   ",len(QCusList),"In Que \n                 vvvv")
        for i in range (len(CusList)):
            print(" >>> Bill Number",CusList[i]," | ",CusAmtList[i]," Person  |  Package ",PackageList[i]," |  Total ",CusTotalAndVat[i],"Bath")
    print("___________________________________________________________________________")
    print("\n\n >>> Which Bill do you want to close? ( Input Bill number such as 0001 ) ")
    Cmd = input("\n  > Enter Bill Number or E to Exit to Main menu : ").upper()
    if Cmd == "E":
        print("\n", " " * 5, "             >>> Exiting <<< ")
        print(" " * 5, "     ===================================== ")
        time.sleep(0.5)
        FMainMenu()
    elif Cmd.isdigit():
        try :
            Close = CusList.index(str(Cmd))
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!\n  Are you sure you want to close Bill Number", Cmd,
                  "?\n   This process cannot be undone!\n")
            Check = input("> Press (Y/N) : ").upper()
            if Check == "Y":
                global BillNumber
                global QBillNumber
                CloseBillList.append((CusList[Close]))
                CloseCusAmtList.append(int(CusAmtList[Close]))
                CloseTotal.append(float(CusTotalList[Close]))
                BillNumber -= 1

                CusList.pop(Close)
                CusAmtList.pop(Close)
                CusTotalAndVat.pop(Close)
                CusTotalList.pop(Close)

                Vat = ("%.2f" % (sum(CloseTotal) * (float(Data[2]))))
                Ser = ("%.2f" % (sum(CloseTotal) * (float(Data[3]))))
                Net = ("%.2f" % (sum(CloseTotal) + (float(Vat)) + (float(Ser))))
                Date = datetime.date.today()
                with open(DateFormat+'_Summary.txt'+str(), 'w') as File:
                    File.write(">>>>>_Date_: "+Date.strftime("%d/%m/%Y")+" <<<<<\n")
                    File.write("Bills_amount_: "+str(len(CloseBillList))+" Bills\n")
                    File.write("Customers_amount_: "+str(sum(CloseCusAmtList))+" Persons\n")
                    File.write("Total_Vat_: "+Vat+" Bath\n")
                    File.write("Total_Service_Charge_: "+Ser+" Bath\n")
                    File.write("Total_: "+str(sum(CloseTotal))+" Bath\n")
                    File.write("NET_Total_Amount_: "+Net+" Bath\n")


                FCloseTable()
            else:
                FCloseTable()
        except ValueError :
            print("\n!!!!! There is no Bill number", Cmd, " ,Please type number from list above !!!!!")
            time.sleep(1)
            FCloseTable()

    else:
        print("          !!!!! Wrong Command! ,Try again !!!!!")
        time.sleep(1)
        FCloseTable()
def FQ():
    os.system('cls')
    global QBillNumber
    global BillNumber
    with open("Profile.txt", "r") as Profile:
        Data = Profile.read().splitlines()
        print("")
        print("               Que Status")
        print("               ============\n")
        print(">>>>> Press E to Exit and go back to Main menu <<<<<\n")
        print("        There are ", len(CusList), "Tables in used")
        print("       And you have", int(Data[1]) - len(CusList), "Tables left\n")
        print("  ========== ",len(QCusList), "Customers In Que, ==========   \n")
        try:
            print("  >>>>>>>>>> Next Que Is Bill Number ",QCusList[0]," <<<<<<<<<<")
            print("\n   > Press C to Call bill number ",QCusList[0],"(Next)")
            print(" ==================================================")
            Cmd = input("\n Input command or press E to Exit : ").upper()
            if Cmd == "E":
                print("\n", " " * 12, "          >>> Exiting Que Menu <<< ")
                print(" " * 12, "       ===================================== ")
                time.sleep(0.5)
                FMainMenu()

            elif Cmd == "C":
                if len(CusList) >= int(Data[1]) :
                    print("\n   !!!!! The Tables is full! !!!!! : ",(Data[1]),"/",(Data[1]),"Tables")
                    time.sleep(1)
                    FQ()

                else:
                    print("> Customer number",QCusList[0],"still here? \n If Customer ",QCusList[0],"Not here anymore the que will be skip!\n")
                    Cmd = input("> (Y/N) : ").upper()
                    if Cmd == "Y" :
                        print ("\nWelcome ",QCusList[0], " Enjoy your meals!")
                        CusList.append(QCusList[0])
                        CusAmtList.append(QCusAmtList[0])
                        CusTotalList.append(QCusTotalList[0])
                        CusTotalAndVat.append(QCusTotalAndVat[0])
                        PackageList.append(QPackageList[0])

                        QCusList.pop(0)
                        QCusAmtList.pop(0)
                        QCusTotalList.pop(0)
                        QCusTotalAndVat.pop(0)
                        QPackageList.pop(0)

                        QBillNumber -= 1
                        BillNumber += 1

                        time.sleep(1)
                        FQ()

                    elif Cmd == "N" :
                        print("\nSkipping que",QCusList[0],"....")
                        QCusList.pop(0)
                        QCusAmtList.pop(0)
                        QCusTotalList.pop(0)
                        QCusTotalAndVat.pop(0)
                        QPackageList.pop(0)
                        time.sleep(1)
                        FQ()
                    else:
                        print("          !!!!! Wrong Command! ,Try again !!!!!")
                        time.sleep(1)
                        FQ()
            else:
                print("          !!!!! Wrong Command! ,Try again !!!!!")
                time.sleep(1)
                FQ()
        except IndexError :
            print("  >>>>>>>>>> There's no next Que yet! <<<<<<<<<<")

            Cmd = input("\n press E to Exit : ").upper()
            if Cmd == "E":
                print("\n", " " * 12, "          >>> Exiting Que Menu <<< ")
                print(" " * 12, "       ===================================== ")
                time.sleep(0.5)
                FMainMenu()
            else:
                print("          !!!!! Wrong Command! ,Try again !!!!!")
                time.sleep(1)
                FQ()
def FSum():
    os.system('cls')
    import datetime
    global BillCount
    global DateFormat
    Date = datetime.date.today()
    print("\n\n                    ",DateFormat,"'s Summary (Today)")
    print("                  =================================\n")
    try :
        with open(DateFormat+'_Summary.txt', 'r') as File:
            Data = File.read().splitlines()
            for Line in Data :
                Item = Line.split()
                print("           %-25s %-15s %-10s\n" %(Item[0],Item[1],Item[2]))
    except FileNotFoundError :
        print("\n\n   >>> No Data to display yet... waiting for customers payment! <<<")
        print("     ============================================================")
        input("\n           > Press Enter to go back to Main Menu : ")
        FMainMenu()

    input("\n           > Press Enter to go back to Main Menu : ")
    print("\n", " " * 12, "       >>> Exiting Bill Summary <<< ")
    print(" " * 12, "       ================================== ")
    time.sleep(0.5)
    FMainMenu()

Date = datetime.date.today()
DateFormat = Date.strftime("%d-%m-%y")

CusList = []
CusAmtList = []
CusTotalList = []
CusTotalAndVat = []
PackageList = []

QCusList = []
QCusAmtList = []
QCusTotalList = []
QCusTotalAndVat = []
QPackageList = []

CloseBillList = []
CloseCusAmtList = []
CloseTotal = []

BillCount = 0
BillNumber = 0
QBillNumber = 0

FFirstRun()

