#Staff Payment Record system

#importing libraries
import time
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import *
import csv

#creating window using Tkinter libraies
root = Tk()
root.title("Staff Payment Record System")
root.geometry('1370x720+0+0')
root.maxsize(width=1370, height=720)
root.minsize(width=1370, height=720)

#creating frames with in the window parameter.
Tops = Frame(root, width=1350, height=50, bd=8, bg="light gray")
Tops.pack(side=TOP)
#frame to hold the title of the applicaiton.
f1 = Frame(root, width=600, height=600, bd=8, bg="light gray")
f1.pack(side=LEFT)
#frame to hold the textbox and time line.
f2 = Frame(root, width=300, height=700, bd=8, bg="light gray")
f2.pack(side=RIGHT)
#frame to hold the entry widget
fla = Frame(f1, width=600, height=200, bd=8, bg="light gray")
fla.pack(side=TOP)
#frame to hold the buttons
flb = Frame(f1, width=300, height=600, bd=8, bg="light gray")
flb.pack(side=TOP)
#creating the main title information label
lbl_information = Label(Tops, font=('arial', 45, 'bold'), text="Staff Payment Record System ", relief=GROOVE,  bd=10, bg="Dark Gray", fg="Black")
lbl_information.grid(row=0, column=0)

#function that works with the exit button, prompts window for 'yes' or 'no' for closing window.
def Exit():
    wayOut = tkinter.messagebox.askyesno("Staff Payment Record System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

#funciton to clear the entry box.
def Reset():
    FullName.set("")
    Month.set("")
    Work.set("")
    leave.set("")
    Payable.set("")
    Taxable.set("")
    NetPayable.set("")
    GrossPayable.set("")
    Bonus.set("")
    Designation.set("")
    PhoneNumber.set("")
    txtPaymentSlip.delete("1.0", END)

#function to get inputs from the entry box  and insert in the text box.
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

#function to save data to selected file.
def Save():
    while True:
        messagebox.showinfo("","select a file")
        filepath = filedialog.askopenfilename()
        #exception handling for file if selected file or not selected file.
        try:
            with open(filepath,'a') as txtfile:
                writer = csv.writer(txtfile)

                name = "Full_Name :" + FullName.get()
                mnth = "Month :" + Month.get()
                position = "Designation :" + Designation.get()
                phone = "Phone_Number :" + PhoneNumber.get()
                worked = "Days_Worked :" + Work.get()
                payable =  "Net_Payable :" + NetPayable.get()
                bonos =  "Bonus :" + Bonus.get()
                leaved = "Absent :" + leave.get()
                tax = "Tax_Paid :" + Taxable.get()
                pay =  "Payable :" + Payable.get()
                line = "\n***************************************\n"
                #writing the data to the text box.
                writer.writerow([name])
                writer.writerow([mnth])
                writer.writerow([position])
                writer.writerow([phone])
                writer.writerow([worked])
                writer.writerow([payable])
                writer.writerow([bonos])
                writer.writerow([leaved])
                writer.writerow([tax])
                writer.writerow([pay])
                writer.writerow([line])

                messagebox.showinfo("","File saved!!!!!")
                txtfile.close()
                #root.quit()
                return
        #error occurs when file not selected.
        except FileNotFoundError:
            messagebox.showerror("Error", "no file was selected, try again")
            return

# list of Variables
FullName = StringVar()
Month = StringVar()
leave = StringVar()
Work = StringVar()
Payable = StringVar()
Taxable = StringVar()
NetPayable = StringVar()
GrossPayable = StringVar()
Bonus = StringVar()
Designation = StringVar()
PhoneNumber = StringVar()
TimeOfOrder = StringVar()
DateOfOrder = StringVar()
DateOfOrder.set(time.strftime("%d/%m/%Y"))

# Label Widget, configuring its dimensions.

labelFirstName = Label(fla, text="Full_Name", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(row=0, column=0)

labelMonth = Label(fla, text="Month", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(row=0, column=2)

labelDesignation = Label(fla, text="Designation", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(row=1,
                                                                                                              column=0)
labelPhoneNumber = Label(fla, text="Phone_Number", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(row=1,
                                                                                                               column=2)
labelHoursWorked = Label(fla, text="Days_Worked", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(
    row=2, column=0)
labelHourlyRate = Label(fla, text="Absent", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(
    row=2, column=2)
labelTax = Label(fla, text="Tax", font=('arial', 16, 'bold'), bd=20, anchor='w', fg="black", bg="light gray").grid(row=3,
                                                                                                                column=0)
labelOverTime = Label(fla, text="Bonus", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(row=3,
                                                                                                              column=2)
labelGrossPay = Label(fla, text="GrossPay", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(row=4,
                                                                                                              column=0)
labelNetPay = Label(fla, text="Net_Pay", font=('arial', 16, 'bold'), bd=20, fg="black", bg="light gray").grid(row=4,
                                                                                                           column=2)

# Entry Widget and dimension configuration

txtFullname = Entry(fla, textvariable=FullName, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtFullname.grid(row=0, column=1)

txtMonth = Entry(fla, textvariable=Month, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtMonth.grid(row=0, column=3)

txtDesignation = Entry(fla, textvariable=Designation, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtDesignation.grid(row=1, column=1)

txtdays_worked = Entry(fla, textvariable=Work, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtdays_worked.grid(row=2, column=1)

txtleave = Entry(fla, textvariable=leave, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtleave.grid(row=2, column=3)

txtPhoneNumber = Entry(fla, textvariable=PhoneNumber, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtPhoneNumber.grid(row=1, column=3)

txtGrossPayment = Entry(fla, textvariable=Payable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtGrossPayment.grid(row=4, column=1)

txtNetPayable = Entry(fla, textvariable=NetPayable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtNetPayable.grid(row=4, column=3)

txtTaxable = Entry(fla, textvariable=Taxable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtTaxable.grid(row=3, column=1)

txtBonus = Entry(fla, textvariable=Bonus, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
txtBonus.grid(row=3, column=3)

# Text Widget configuration

payslip = Label(f2, textvariable=DateOfOrder, font=('arial', 21, 'bold'), fg="black", bg="dark grey").grid(row=0,
                                                                                                           column=0)
txtPaymentSlip = Text(f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="black", bg="white")
txtPaymentSlip.grid(row=1, column=0)

# buttons and configuration.

ButtonSalary = Button(flb, text='Save', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14, fg="black",
                   bg="dark gray", command=Save).grid(row=0, column=0)

ButtonReset = Button(flb, text='Reset', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14, command=Reset,
                  fg="black", bg="dark gray").grid(row=0, column=1)

ButtonPaySlip = Button(flb, text='View Payslip', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14,
                    command=InformationEntry, fg="black", bg="dark gray").grid(row=0, column=2)

ButtonExit = Button(flb, text='Exit System', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14, command=Exit,
                 fg="black", bg="dark gray").grid(row=0, column=3)

#creating loop to hold
root.mainloop()
