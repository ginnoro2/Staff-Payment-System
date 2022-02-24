import unittest

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
