import unittest

def InformationEntry():
    txtPaymentSlip.delete("1.0", END)
    txtPaymentSlip.insert(END, "\t\tPay Slip\n\n")
    txtPaymentSlip.insert(END, "Full_Name :\t\t" + FullName.get() + "\n\n")
    txtPaymentSlip.insert(END, "Month :\t\t" + Month.get() + "\n\n")
    txtPaymentSlip.insert(END, "Designation :\t\t" + Designation.get() + "\n\n")
    txtPaymentSlip.insert(END, "Phone_Number :\t\t" + PhoneNumber.get() + "\n\n")
    txtPaymentSlip.insert(END, "Days_Worked :\t\t" + Work.get() + "\n\n")
    txtPaymentSlip.insert(END, "Net_Payable :\t\t" + NetPayable.get() + "\n\n")
    txtPaymentSlip.insert(END, "Absent :\t\t" + leave.get() + "\n\n")
    txtPaymentSlip.insert(END, "Tax_Paid :\t\t" + Taxable.get() + "\n\n")
    txtPaymentSlip.insert(END, "Payable :\t\t" + Payable.get() + "\n\n")
    txtPaymentSlip.insert(END, "Bonus :\t\t" + Bonus.get() + "\n\n")
