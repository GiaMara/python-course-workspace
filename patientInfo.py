''' 
This program computes and displays the charges for a patient’s hospital stay. 
It validates that no input is less than zero. 
The program uses two functions to calculate the total charges.
'''

writeReport = open("patientInformation.txt", "w")
def validateResponse():
    if int(response) >=1:
        return(response)
    else:
        return("no")
def inPatientCost():
    total = (days*dailyRate)+servicesCharges+medicationCharges
    return(total)

def outPatientCost():
    total = servicesCharges+medicationCharges
    return(total)
counter  = 1
counterb = 1
days = 0
dailyRate = 0
servicesCharges = 0
medicationCharges = 0
totalBill = 0
patientName = input("Patient Name: ")
writeReport.write("Patient Name: "+patientName+"\n")
patientIn = input("Were you admitted as an in-patient  (Y/N)? ")
patientIn = patientIn.lower()
if patientIn == "y":
    writeReport.write("In-patient or out-patient: In-patient"+"\n")
    response = input("How many days were you admitted in the hospital? ")

    if response.isdigit():
        validateResponse()
        days = int(response)
        writeReport.write("Length of Admission: "+str(days)+" days"+"\n")
        
        response = input("How much was the daily rate for your hospital room? $")
        if response.isdigit():
            validateResponse()
            dailyRate = float(response)
            writeReport.write("Daily Rate: $"+str(dailyRate)+"\n")                
            

            response = input("How much in total were the hospital charges (lab tests, etc.)? $")
            if response.isdigit():
                validateResponse()
                servicesCharges = float(response)
                writeReport.write("Charges for hospital services (lab tests, etc.): $"+str(servicesCharges)+"\n")

 
                response = input("How much in total were the medication charges? $")
                if response.isdigit():
                    validateResponse()
                    medicationCharges = float(response)
                    writeReport.write("Hospital medication charges: $"+str(medicationCharges)+"\n")

                    totalBill = inPatientCost()
                    print()
                    print("Total charges will be: $"+str(totalBill))
                    writeReport.write("Total charges will be: $"+str(totalBill))
    
                else:
                    print("Entry invalid. Please enter response again.")
            else:        
                print("Entry invalid. Please enter response again.")
        else:
            print("Entry invalid. Please re-enter data.")
        
    print()
    
else:
    patientOut = input("Were you treated as an out-patient (Y/N)?")
    patientOut = patientOut.lower()
    if patientOut == "y":
        writeReport.write("In-patient or out-patient: Out-patient"+"\n")
        response = input("How much in total were the hospital charges (lab tests, etc.)? $")
        if response.isdigit():
            validateResponse()
            servicesCharges = float(response)
            writeReport.write("Charges for hospital services (lab tests, etc.): $"+str(servicesCharges)+"\n")
                
            response = input("How much in total were the medication charges? $")
            if response.isdigit():
                validateResponse()
                medicationCharges = float(response)
                writeReport.write("Hospital medication charges: $"+str(medicationCharges)+"\n")
                
                totalBill = outPatientCost()
                print()
                print("Total charges will be: $"+str(totalBill))
                writeReport.write("Total charges will be: $"+str(totalBill))               

            else:
                print("Entry invalid. Please enter response again.")
        else:
            print("Entry invalid. Please enter response again.")
    else:
        print("No charges incurred.")    