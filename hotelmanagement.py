from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
from tkinter import messagebox
import mysql.connector
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import date



#cd desktop/PYTHONTEAM/PYTHON-PROJECT
global root
root = Tk()

# CREATING DATABASE .
# mb=mysql.connector.connect(
# host="localhost",
# user="root",
# password="Nana#773_9z",
# database="hotel"
# )
# my_cursor = mb.cursor()
# my_cursor.execute("CREATE DATABASE Hotel")
#mb.commit()
# mb.close()


mb=mysql.connector.connect(
host="localhost",
user="root",
password="Nana#773_9z",
database="hotel"
)
my_cursor = mb.cursor()
mb.commit()
mb.close()

class HOMEPAGE:
    def __init__ (self , master):
        self.master = master
        self.master.title("Hotel Management")
        self.master.iconbitmap("./IMAGE/Graphicloads-Polygon-Files.ico")
        self.master.geometry("1366x768")
        self.master.attributes("-transparentcolor", "dodger blue")
        self.frame = Frame(self.master)
        self.frame.pack()
        global LoginImage
        global myimage
        global SignUpImage

        #This is a simple function used to display images .
        def ImageDisplay(imgpath):
            theimage = ImageTk.PhotoImage (Image.open(imgpath))
            return theimage
        
        #calling the above func to display an image
        myimage =ImageDisplay("./IMAGE/realhotelbg.jpg")  
        self.background_label = Label(master, image=myimage)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.myLabel = Label(master , text = ("HOTEL MANAGEMENT SYSTEM") , justify = CENTER ,font = "Helvetica 30 bold italic" , bg= "#ffffff" ).pack()

        LoginImage = ImageDisplay("./IMAGE/LoginImage.jpg")
        self.Loginbutton = Button(master , image =LoginImage  , border = 0 ,command =self.thelogin)
        self.Loginbutton.place(relx = 0.35, rely = 0.75, anchor = CENTER )

        SignUpImage = ImageDisplay("./IMAGE/SignupImage.jpg")
        self.Signupbutton = Button(master , image =SignUpImage  , border = 0 ,command = self.thesignup) 
        self.Signupbutton.place(relx = 0.65, rely = 0.75, anchor = CENTER )

    def thelogin(self):
        self.newWindow = Toplevel(self.master)
        self.app = loginWindow(self.newWindow)

    def thesignup(self):
        self.newWindow = Toplevel(self.master)
        self.app = signupWindow(self.newWindow)
        # self.master.destroy()

class loginWindow(HOMEPAGE):
    def __init__(self , master):
        self.master = master
        self.master.title("Hotel Management-LOGIN")
        self.master.iconbitmap("./IMAGE/Graphicloads-Polygon-Files.ico")
        self.master.geometry("1366x768")
        self.master.config(bg = "#ffebee")
        

        self.loginlabel = Label(self.master , text = "LOGIN" , font = ('arial' , 35 , 'italic') , bg = "#ffebee" , fg ="black" )
        self.loginlabel.pack(side = TOP )

        self.loginframe = Frame(self.master , width = 1000 , bg = "#fce4ec",  height = 400 , relief = 'ridge' , bd = 2)
        self.loginframe.place(x=150 , y=120)

        def logincheck():
            usernamevalue = self.UserNameEntry.get()
            passwordvalue =self.PasswordNameEntry.get()
            n = 2
            mb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nana#773_9z",
            database="hotel"
            )
            my_cursor = mb.cursor()
            my_cursor.execute("select *from user_details")
            records=my_cursor.fetchall()
            # print(records)
            for record in records:
                if usernamevalue == record[1] and passwordvalue == record[5]:
                    #Deletes all fields after login is done .
                    self.UserNameEntry.delete(0 , END)
                    self.PasswordNameEntry.delete(0 , END)
                    self.theHome()
                    
                    break

            else:
                self.UserNameEntry.delete(0 , END)
                self.PasswordNameEntry.delete(0 , END)
                messagebox.showwarning("ERROR!" , "INCORRECT USERNAME OR PASSWORD" , parent = self.master)
                
    

            mb.commit()
            mb.close()

            
           
    



        u_name = StringVar()
        self.fieldsUsername = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Username : " ,50 , 50 )
        self.UserNameEntry = Entry(self.loginframe ,textvariable = u_name , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" )  )
        self.UserNameEntry.place(x = 350 , y = 70)



        u_password = StringVar()
        self.fieldspassword = AnyName(self.loginframe ,"./IMAGE/passwordImage.png" , "Password : " ,50 , 120 )
        self.PasswordNameEntry = Entry(self.loginframe ,textvariable = u_password , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" ) , show = "*")
        self.PasswordNameEntry.place(x = 350 , y = 140)

        self.Submit_image = ImageTk.PhotoImage(Image.open("./IMAGE/Submit.jpg"))
        self.SubmitButton = Button(self.loginframe , image=self.Submit_image , border = 0  , command = logincheck)
        self.SubmitButton.place(x = 350 , y = 200)


    def thehompage(self):
        self.newWindow = Toplevel(self.master)
        self.app = HOMEPAGE(self.newWindow)

    def theHome(self):
        self.newWindow = Toplevel(self.master)
        self.app = HomeWindow(self.newWindow)
        

class HomeWindow(loginWindow):
    def __init__(self , master):
        self.master = master
        self.master.title("Hotel Management-HOME")
        self.master.iconbitmap("./IMAGE/Graphicloads-Polygon-Files.ico")
        self.master.geometry("1366x768")
        self.master.config(bg = "#fce4ec")

        self.welcomelabel = Label(self.master , text = "WELCOME !! " , font = ('arial' , 35 , 'italic')  , fg ="black" , bg = "#fce4ec")
        self.welcomelabel.pack(side = TOP )

        self.addlabel = Label(self.master , text = "Add" , font = ('arial' , 10 , 'italic')  , fg ="black" , bg = "#FFFFFF")
        self.addlabel.place(x=170 , y = 48)


        self.editlabel = Label(self.master , text = "Edit" , font = ('arial' , 9 , 'italic')  , fg ="black" , bg = "#FFFFFF")
        self.editlabel.place(x=590 , y = 49)

        self.deletelabel = Label(self.master , text = "Delete" , font = ('arial' , 9 , 'italic')  , fg ="black" , bg = "#FFFFFF")
        self.deletelabel.place(x=1050 , y = 49)

        self.searchlabel = Label(self.master , text = "Search " , font = ('arial' , 9 , 'italic')  , fg ="black" , bg = "#FFFFFF")
        self.searchlabel.place(x=1050 , y = 520)

        self.addframe = Frame(self.master , width = 400 , bg = "#fce4ec",  height = 600 , relief = 'ridge' , bd = 10)
        self.addframe.place(x=10 , y=70)




        def deleteguest():
            mb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nana#773_9z",
            database="hotel"
            )
            my_cursor = mb.cursor()

            my_cursor.execute("select *from Guest_Info")
            records=my_cursor.fetchall()
            
            for record in records:
                if self.deleteNumberEntry.get() == record[4]:
                    my_cursor.execute("DELETE FROM Guest_Info WHERE phone_no ="+self.deleteNumberEntry.get())
                    messagebox.showinfo("DELETED!" , "The guest has been deleted " , parent = self.master)
                    break
            else:
                messagebox.showerror("ERROR!" , "The guest is not present" , parent = self.master)

            mb.commit()
            mb.close()

            self.deleteNumberEntry.delete(0 , END)


        def addUserToDb():
            #Creating Guest Details Database .
            mb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nana#773_9z",
            database="hotel"
            )
            my_cursor = mb.cursor()
            #Creating The Tables In The Database
            # my_cursor.execute("""CREATE TABLE Guest_Info (
            #                          userid INT AUTO_INCREMENT PRIMARY KEY, 
            #                          firstname VARCHAR(200) NOT NULL,
            #                          lastname VARCHAR(200) NOT NULL, 
            #                          email VARCHAR(200) NOT NULL, 
            #                          phone_no VARCHAR(200) NOT NULL , 
            #                          address VARCHAR(200) NOT NULL , 
            #                          state VARCHAR(200) NOT NULL ,
            #                          room_type VARCHAR(200) NOT NULL,
            #                          arrival DATE NOT NULL,
            #                          departure DATE NOT NULL
            #                          )""")

            
            s = "INSERT INTO Guest_Info(firstname ,lastname , email ,phone_no , address ,state ,room_type ,arrival,departure) VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s)"
            data = (f"{self.guestsFirstNameEntry.get()}",f"{self.guestsLastNameEntry.get()}" ,  f"{self.guestsEmailNameEntry.get()}" , f"{self.guestsNumberEntry.get()}" ,f"{self.guestsAddressEntry.get()}" , f"{self.state.get()}"  ,f"{self.roomtype.get()}" ,f"{self.arrivalyear.get()}-{self.arrivalmonth.get()}-{self.arrivalday.get()}" , f"{self.depatureyear.get()}-{self.depaturemonth.get()}-{self.depatureday.get()}" )
            my_cursor.execute(s,data)
            p = "SELECT DATEDIFF(%s, %s)"
            thedate = ( f"{self.depatureyear.get()}-{self.depaturemonth.get()}-{self.depatureday.get()}" , f"{self.arrivalyear.get()}-{self.arrivalmonth.get()}-{self.arrivalday.get()}"  )
            my_cursor.execute(p,thedate)
            dateinterval = my_cursor.fetchall()
            roomselected = self.roomtype.get()

            roomselectedamount = ""

            if roomselected == "Select Room Type...":
                self.AMOUNTLabel = Label(self.master ,text = "00.00" ,  bg = "#fce4ec" , font = ('CHARLESWORTH' , 25) )
                self.AMOUNTLabel.place(x=1100 , y=680)

            else:
                for i in range (13 , 17):
                    roomselectedamount += str(roomselected[i])
                
                totalamounttobepaid = int(dateinterval[0][0])*int(roomselectedamount)
                self.AMOUNTLabel = Label(self.master ,text = totalamounttobepaid ,  bg = "#fce4ec" , font = ('CHARLESWORTH' , 26) )
                self.AMOUNTLabel.place(x=1100 , y=680)

            response = messagebox.askyesno("INVOICE" , "Do You Want To Print Invoice?" ,  parent = self.master)

            

            today = date.today()

    
            if response == 1:
                def  drawMyRuler(pdf):
                    pdf.drawString(100,810 , ' ')
                    pdf.drawString(200,810 , ' ')
                    pdf.drawString(300,810 , ' ')
                    pdf.drawString(400,810 , ' ')
                    pdf.drawString(500,810 , ' ')

                    pdf.drawString(10,100 , ' ')
                    pdf.drawString(10,200 , ' ')
                    pdf.drawString(10,300 , ' ')
                    pdf.drawString(10,400 , ' ')
                    pdf.drawString(10,500 , ' ')
                    pdf.drawString(10,600 , ' ')
                    pdf.drawString(10,700 , ' ')
                    pdf.drawString(10,800 , ' ')

                data_file = f"{self.guestsFirstNameEntry.get()}.pdf"
                name = f"{self.guestsFirstNameEntry.get()} {self.guestsLastNameEntry.get()}"
                title = "THE VIEW HOTEL"

                documentTitle = name+"'s  RECIEPT"

                subtitle = "WELCOME TO THE VIEW HOTEL"
                print(today)
                #Importing the date
                thedate = f"DATE : {today}"
                

                textlines = [

                    f"Name            : {name}" ,  
                    f"Email           : {self.guestsEmailNameEntry.get()} " ,
                    f"Address         : {self.guestsAddressEntry.get()} ",
                    f'Telephone Number: {self.guestsNumberEntry.get()}' ,
                    f'State           : {self.state.get()}',
                    f'Room Selected   : {self.roomtype.get()} ',
                    f'Days Booked     : {int(dateinterval[0][0])}' , 
                    ' ',
                    ' ',
                    ' ',
                    f'Amount Paid For  : Rs.{totalamounttobepaid}'
                ]

                pdf = canvas.Canvas(data_file)
                pdf.setTitle(documentTitle)

                #This is used to refer to the above ruler 
                drawMyRuler(pdf) 

                #This is to view available fonts 
                for font in pdf.getAvailableFonts():
                    print(font)

                pdf.setFont('Courier-Bold' , 18)
                pdf.drawString(350 , 800 , thedate)

                #Accessing Downloaded Font.
                pdfmetrics.registerFont(TTFont('abc' , 'Carnevalee Freakshow.ttf'))

                pdf.setFont('abc' , 36)

                #This is used to set the co-ordinates.
                # pdf.drawString(270,770,title)

                #This is used to center the string
                pdf.drawCentredString(300,760,title)

                #Creating a SubTitle
                pdf.setFont('Courier-Bold' , 24)
                pdf.drawCentredString(290 , 720 , subtitle)

                #Drawing A Line 
                pdf.line(110 , 710 , 470 , 710)

                #Inserting The Text.
                text = pdf.beginText(40 , 680)
                text.setFont('Courier' , 18)

                for line in textlines:
                    text.textLine(line)

                pdf.drawText(text)

                pdf.save()

            else:
                messagebox.showerror("ERROR!" , "Guest Not Present In The System." , parent = self.master)

            messagebox.showinfo("SAVED!" , "Guests Details Has Been Saved Successfully." , parent = self.master)
            mb.commit()
            mb.close()

            self.guestsFirstNameEntry.delete(0 , END)
            self.guestsLastNameEntry.delete(0 , END)
            self.guestsEmailNameEntry.delete(0 , END)
            self.guestsNumberEntry.delete(0 , END)
            self.guestsAddressEntry.delete(0 , END)
            self.roomtype.set("Select Room Type...")
            self.state.set(statelist[0])
            self.depatureday.set(depaturedays[0])
            self.depatureyear.set(depatureyears[0])
            self.depaturemonth.set(depaturemonths[0])
            self.arrivalday.set(arrivaldays[0])
            self.arrivalyear.set(arrivalyears[0])
            self.arrivalmonth.set(arrivalmonths[0])


        def editGuest_Info():
            self.updateFirstNameEntry.delete(0 , END)
            self.updateLastNameEntry.delete(0 , END)
            self.updateEmailNameEntry.delete(0 , END)
            self.updateNumberEntry.delete(0 , END)
            self.updateAddressEntry.delete(0 , END)
            self.updatestate.set(statelist[0])
            self.updateroomtype.set("Select Room Type...")
            
            self.updatedepatureday.set(depaturedays[0])
            self.updatedepatureyear.set(depatureyears[0])
            self.updatedepaturemonth.set(depaturemonths[0])


            
            mb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nana#773_9z",
            database="hotel"
            )
            my_cursor = mb.cursor()
            try:
                my_cursor.execute("SELECT *FROM Guest_Info WHERE phone_no ="+self.EditNumberEntry.get())
                records = my_cursor.fetchall()
                print(records)
            
                for record in records:
                    self.updateFirstNameEntry.insert(0 , record[1])
                    self.updateLastNameEntry.insert(0 , record[2])
                    self.updateEmailNameEntry.insert(0 , record[3])
                    self.updateNumberEntry.insert(0 , record[4])
                    self.updateAddressEntry.insert(0 , record[5])
                    self.updatestate.set(record[6])
                    self.updateroomtype.set(record[7])
                    
                    thearrivaldate = str(record[9])
                    
                    year =""
                    for i in range (0 , 4):
                        year += str(thearrivaldate[i])
                    print(year)

                    self.updatedepatureyear.set(year)
                    month =""
                    for i in range (5 , 7):
                        month += str(thearrivaldate[i])
                    print(month)

                    self.updatedepaturemonth.set(month)
                    day =""
                    for i in range (8 , 10):
                        day += str(thearrivaldate[i])
                    print(day)

                    self.updatedepatureday.set(day)

            except mysql.connector.errors.ProgrammingError:
                print("Enter the right guess Number")
                messagebox.showerror("ERROR!" , "Guest Not Present In The System." , parent = self.master)

            mb.commit()
            mb.close()

        def updateguestsinfo():
            mb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nana#773_9z",
            database="hotel"
            )
            my_cursor = mb.cursor()
            sql = "UPDATE Guest_Info SET firstname=%s , lastname = %s , email = %s , phone_no = %s , address = %s , state =%s , room_type = %s , departure = %s WHERE phone_no = %s"
            data = (f"{self.updateFirstNameEntry.get()}",f"{self.updateLastNameEntry.get()}" ,  f"{self.updateEmailNameEntry.get()}" , f"{self.updateNumberEntry.get()}" ,f"{self.updateAddressEntry.get()}" , f"{self.updatestate.get()}"  ,f"{self.updateroomtype.get()}" , f"{self.updatedepatureyear.get()}-{self.updatedepaturemonth.get()}-{self.updatedepatureday.get()}" , f"{self.EditNumberEntry.get()}")

            my_cursor.execute(sql , data)
            mb.commit()
            mb.close()

            messagebox.showinfo("UPDATED!" , "Guest Info Has Been Updated Successfully." , parent = self.master)

            self.updateFirstNameEntry.delete(0 , END)
            self.updateLastNameEntry.delete(0 , END)
            self.updateEmailNameEntry.delete(0 , END)
            self.updateNumberEntry.delete(0 , END)
            self.updateAddressEntry.delete(0 , END)
            self.updatestate.set(statelist[0])
            self.updateroomtype.set("Select Room Type...")
            self.updatedepatureday.set(depaturedays[0])
            self.updatedepatureyear.set(depatureyears[0])
            self.updatedepaturemonth.set(depaturemonths[0])







        guest_f_name = StringVar()
        self.FirstnameLabel = HomeForms(self.addframe ,"First Name : " , 10 , 20 )
        self.guestsFirstNameEntry = Entry(self.addframe ,textvariable = guest_f_name , width = 17 , bd = 2 , font = ('Arial' , 14 , "italic" )  )
        self.guestsFirstNameEntry.place(x = 170 , y = 25)

        guest_l_name = StringVar()
        self.LastnameLabel = HomeForms(self.addframe ,"Last Name : " , 10 , 80 )
        self.guestsLastNameEntry = Entry(self.addframe ,textvariable = guest_l_name , width = 17 , bd = 2 , font = ('Arial' , 14 , "italic" )  )
        self.guestsLastNameEntry.place(x = 170 , y = 85)

        guest_mail = StringVar()
        self.EmailLabel = HomeForms(self.addframe ,"Email : " , 10 , 140 )
        self.guestsEmailNameEntry = Entry(self.addframe ,textvariable = guest_mail , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.guestsEmailNameEntry.place(x = 170 , y = 145)

        guest_Tel_no = StringVar()
        self.NUmberLabel = HomeForms(self.addframe ,"Phone NO : " , 10 , 200 )
        self.guestsNumberEntry = Entry(self.addframe ,textvariable = guest_Tel_no , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.guestsNumberEntry.place(x = 170 , y = 205)


        guest_Address = StringVar()
        self.AddressLabel = HomeForms(self.addframe ,"Address :" , 10 , 260 )
        self.guestsAddressEntry = Entry(self.addframe ,textvariable = guest_Address , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.guestsAddressEntry.place(x = 170 , y = 265)

        self.StateLabel = HomeForms(self.addframe ,"State :" , 10 , 320 )
        options = ["Select State.....","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
    
        statelist = options
        self.state =StringVar()
        self.state.set(statelist[0])
        self.StateDropdown = OptionMenu(self.addframe ,self.state,*statelist ).place(x=170 , y=325 , width = 200)

        
        self.RoomTypeLabel = HomeForms(self.addframe ,"Room Type:" , 10 , 380 )
        roomoptions = ["Single Price(1000)" , "Double Price(1500)" , "Triple Price(2000)" , "King   Price(1700)" , "Queen  Price(1700)" , "Twin   Price(1900)"]
        
        roomlist = roomoptions
        self.roomtype = StringVar()
        self.roomtype.set("Select Room Type...")
        self.RoomDropdown= OptionMenu(self.addframe ,self.roomtype,*roomlist ).place(x = 170 , y = 385 , width = 200)
        
        self.ArrivalDate = HomeForms(self.addframe ,"Arrival Date :" , 10 , 440 )
        self.ArrivalDateDayLabel = Label(self.addframe ,text = "Day" , bg ="#fce4ec").place(x=170 , y=430)
        self.DateDiv = Label(self.addframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 20 ) ).place(x=225   , y=448)
        self.DateMonthLabel = Label(self.addframe ,text = "Month" , bg ="#fce4ec").place(x=240 , y=430)
        self.DateDiv1 = Label(self.addframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 20 ) ).place(x=295 , y=448)
        self.DateYearLabel = Label(self.addframe ,text = "Year" , bg ="#fce4ec").place(x=310 , y=430)
        
        def dropdownRange(start , end):
            end = end+1
            options = []
            for i in range(start,end):
                options.append(i)
            return options

        arrivaldays = dropdownRange(1,31)
        self.arrivalday =IntVar()
        self.arrivalday.set(arrivaldays[0])
        self.DateDay = OptionMenu(self.addframe , self.arrivalday,*arrivaldays ).place(x=170 , y=450)

        arrivalmonths = dropdownRange(1,12)
        self.arrivalmonth =IntVar()
        self.arrivalmonth.set(arrivalmonths[0])
        self.DateMonth = OptionMenu(self.addframe , self.arrivalmonth,*arrivalmonths ).place(x=240 , y=450)

        arrivalyears = dropdownRange(2020,2030)
        self.arrivalyear =IntVar()
        self.arrivalyear.set(arrivalyears[0])
        self.DateYear = OptionMenu(self.addframe , self.arrivalyear,*arrivalyears ).place(x=310 , y=450)



        self.depatureDate = HomeForms(self.addframe ,"Depature :" , 10 , 500 )
        self.depatureDateDayLabel = Label(self.addframe ,text = "Day" , bg ="#fce4ec").place(x=170 , y=490)
        self.DateDiv = Label(self.addframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 20 ) ).place(x=225   , y=508)
        self.DateMonthLabel = Label(self.addframe ,text = "Month" , bg ="#fce4ec").place(x=240 , y=490)
        self.DateDiv1 = Label(self.addframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 20 ) ).place(x=295 , y=508)
        self.DateYearLabel = Label(self.addframe ,text = "Year" , bg ="#fce4ec").place(x=310 , y=490)
        
        def dropdownRange(start , end):
            end = end+1
            options = []
            for i in range(start,end):
                options.append(i)
            return options

        depaturedays = dropdownRange(1,31)
        self.depatureday =IntVar()
        self.depatureday.set(depaturedays[0])
        self.DateDay = OptionMenu(self.addframe , self.depatureday,*depaturedays ).place(x=170 , y=510)

        depaturemonths = dropdownRange(1,12)
        self.depaturemonth =IntVar()
        self.depaturemonth.set(depaturemonths[0])
        self.DateMonth = OptionMenu(self.addframe , self.depaturemonth,*depaturemonths ).place(x=240 , y=510)

        depatureyears = dropdownRange(2020 , 2030)
        self.depatureyear =IntVar()
        self.depatureyear.set(depatureyears[0])
        self.DateYear = OptionMenu(self.addframe , self.depatureyear,*depatureyears ).place(x=310 , y=510)

        self.SubmitButton = Button(self.addframe , text = "BOOK NOW !!" , command = addUserToDb).place(x = 50 , y = 555 , width = 300)


        self.contactFrame = Frame(self.master , width = 400 , bg = "#fce4ec",  height = 70 , relief = 'ridge' , bd = 10)
        self.contactFrame.place(x=10 , y=670)

        self.ContactButton = Button(self.contactFrame , text = "CONTACT MASTER !!" , command =  self.StaffContact).place(y=0 , x=0, width=380 , height = 50)

        self.editframe = Frame(self.master , width = 400 , bg = "#fce4ec",  height = 670 , relief = 'ridge' , bd = 10)
        self.editframe.place(x=410 , y=70)

        editTel_no = StringVar()
        self.editByPhone = Label(self.editframe , text = "Enter Phone Number Of The Customer" , bg = "#fce4ec" ,font = ('CHARLESWORTH' , 15) , compound = LEFT ).place(x = 10 , y = 5)
        self.EditNumberEntry = Entry(self.editframe ,textvariable = editTel_no , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.EditNumberEntry.place(x =70 , y = 35)

        self.EditButton = Button(self.editframe , text = "EDIT" , command = editGuest_Info).place(x=150 , y=65)

        self.updateframe = Frame(self.editframe , width = 380 , bg = "#fce4ec",  height = 565 , relief = 'ridge' , bd =2)
        self.updateframe.place(x=0 , y=90)


        updatef_name = StringVar()
        self.FirstnameLabel = HomeForms(self.updateframe ,"First Name : " , 10 , 5 )
        self.updateFirstNameEntry = Entry(self.updateframe ,textvariable = updatef_name , width = 17 , bd = 2 , font = ('Arial' , 14 , "italic" )  )
        self.updateFirstNameEntry.place(x = 170 , y = 10)

        updatel_name = StringVar()
        self.LastnameLabel = HomeForms(self.updateframe ,"Last Name : " , 10 , 65 )
        self.updateLastNameEntry = Entry(self.updateframe ,textvariable = updatel_name , width = 17 , bd = 2 , font = ('Arial' , 14 , "italic" )  )
        self.updateLastNameEntry.place(x = 170 , y = 70)

        updatemail = StringVar()
        self.EmailLabel = HomeForms(self.updateframe ,"Email : " , 10 , 125 )
        self.updateEmailNameEntry = Entry(self.updateframe ,textvariable = updatemail , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.updateEmailNameEntry.place(x = 170 , y = 130)

        updateTel_no = StringVar()
        self.NUmberLabel = HomeForms(self.updateframe ,"Phone NO : " , 10 , 185 )
        self.updateNumberEntry = Entry(self.updateframe ,textvariable = updateTel_no , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.updateNumberEntry.place(x = 170 , y = 190)


        updateAddress = StringVar()
        self.AddressLabel = HomeForms(self.updateframe ,"Address :" , 10 , 245 )
        self.updateAddressEntry = Entry(self.updateframe ,textvariable = updateAddress , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.updateAddressEntry.place(x = 170 , y = 250)

        self.StateLabel = HomeForms(self.updateframe ,"State :" , 10 , 305 )
        options = ["Select State.....","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
    
        statelist = options
        self.updatestate =StringVar()
        self.updatestate.set(statelist[0])
        self.StateDropdown = OptionMenu(self.updateframe ,self.updatestate,*statelist ).place(x=170 , y=310 , width = 200)

        
        self.RoomTypeLabel = HomeForms(self.updateframe ,"Room Type:" , 10 , 380 )
        roomoptions = ["Single Price-(800)" , "Double Price-(1500)" , "Triple Price-(2000)" , "King Price-(1700)" , "Queen Price-(1700)" , "Twin Price-(1900)"]
        
        roomlist = roomoptions
        self.updateroomtype = StringVar()
        self.updateroomtype.set("Select Room Type...")
        self.RoomDropdown= OptionMenu(self.updateframe ,self.updateroomtype,*roomlist ).place(x = 170 , y = 385 , width = 200)


        self.depatureDate = HomeForms(self.updateframe ,"Depature :" , 10 , 445 )
        self.depatureDateDayLabel = Label(self.updateframe ,text = "Day" , bg ="#fce4ec").place(x=170 , y=435)
        self.DateDiv = Label(self.updateframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 20 ) ).place(x=225   , y=453)
        self.DateMonthLabel = Label(self.updateframe ,text = "Month" , bg ="#fce4ec").place(x=240 , y=435)
        self.DateDiv1 = Label(self.updateframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 20 ) ).place(x=295 , y=453)
        self.DateYearLabel = Label(self.updateframe ,text = "Year" , bg ="#fce4ec").place(x=310 , y=435)
        
        def dropdownRange(start , end):
            end = end+1
            options = []
            for i in range(start,end):
                options.append(i)
            return options

        depaturedays = dropdownRange(1,31)
        self.updatedepatureday =IntVar()
        self.updatedepatureday.set(depaturedays[0])
        self.DateDay = OptionMenu(self.updateframe , self.updatedepatureday,*depaturedays ).place(x=170 , y=455)

        depaturemonths = dropdownRange(1,12)
        self.updatedepaturemonth =IntVar()
        self.updatedepaturemonth.set(depaturemonths[0])
        self.DateMonth = OptionMenu(self.updateframe , self.updatedepaturemonth,*depaturemonths ).place(x=240 , y=455)

        depatureyears = dropdownRange(2020,2030)
        self.updatedepatureyear =IntVar()
        self.updatedepatureyear.set(depatureyears[0])
        self.DateYear = OptionMenu(self.updateframe , self.updatedepatureyear,*depatureyears ).place(x=310 , y=455)

        self.UpdatetButton = Button(self.updateframe , text = "UPDATE USER"  , command = updateguestsinfo).place(x = 50 , y = 530 , width = 300)


        self.deleteframe = Frame(self.master , width = 555 , bg = "#fce4ec",  height = 120 , relief = 'ridge' , bd = 10)
        self.deleteframe.place(x=810 , y=70)

        deleteTel_no = StringVar()
        self.deleteByPhone = Label(self.deleteframe , text = "Enter Phone Number Of The Customer" , bg = "#fce4ec" ,font = ('CHARLESWORTH' , 15) , compound = LEFT ).place(x = 55 , y = 5)
        self.deleteNumberEntry = Entry(self.deleteframe ,textvariable = deleteTel_no , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.deleteNumberEntry.place(x =115 , y = 35)

        self.deleteButton = Button(self.deleteframe , text = "DELETE" , command = deleteguest).place(x=202 , y=70)

        def getallguests():
            #Adding a scrollbar .......
            #mainframe
            self.viewguestsframe = Frame(self.master , width = 420 , bg = "#FFFFFF",  height = 300 , relief = 'ridge' , bd = 10)
            self.viewguestsframe.place(x=810 , y=220)

            #Adding canvas in the frame
            viewguestscanvas = Canvas(self.viewguestsframe)
            viewguestscanvas.pack(side = LEFT , fill = BOTH , expand = 1)


            viewguestsscrollbar = ttk.Scrollbar(self.viewguestsframe , orient = VERTICAL, command = viewguestscanvas.yview)
            viewguestsscrollbar.pack(side = RIGHT , fill = Y)

            viewguestscanvas.configure(yscrollcommand =viewguestsscrollbar.set)
            viewguestscanvas.bind('<Configure>' , lambda e : viewguestscanvas.configure(scrollregion = viewguestscanvas.bbox("all")))

            #Another frame in the canvas
            self.viewguestslistframe = Frame(viewguestscanvas) 
            viewguestscanvas.create_window((0,0) , window = self.viewguestslistframe, anchor = "nw")
            mb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nana#773_9z",
            database="hotel"
            )
            my_cursor = mb.cursor()
            my_cursor.execute("SELECT *FROM Guest_Info")
            allguests = my_cursor.fetchall()

            print_records=""

            for guest in allguests:
                print_records +="First Name : "+ str(guest[1]) + "\n" +"Last Name : " + str(guest[2])  + "\n" +"Email : " + str(guest[3]) + "\n" + "Phone Number : "+ str(guest[4]) + "\n" + "Room Type : " + str(guest[7])+"\n\n\n\n"
            
            NameLabel= Label(self.viewguestslistframe , text = print_records ,font = ('CHARLESWORTH' , 15) , compound = LEFT ).pack(side = LEFT)
            mb.commit()
            mb.close()


        self.viewguestslistButton = Button(self.master , text = "View List" , command = getallguests).place(x=1225 , y=220, height = 290 , width = 145)

        # #Adding a scrollbar .......
        # #mainframe
        self.viewguestsframe = Frame(self.master , width = 420 , bg = "#FFFFFF",  height = 300 , relief = 'ridge' , bd = 10)
        self.viewguestsframe.place(x=810 , y=220)

        #Adding canvas in the frame
        viewguestscanvas = Canvas(self.viewguestsframe)
        viewguestscanvas.pack(side = LEFT , fill = BOTH , expand = 1)


        viewguestsscrollbar = ttk.Scrollbar(self.viewguestsframe , orient = VERTICAL, command = viewguestscanvas.yview)
        viewguestsscrollbar.pack(side = RIGHT , fill = Y)

        viewguestscanvas.configure(yscrollcommand =viewguestsscrollbar.set)
        viewguestscanvas.bind('<Configure>' , lambda e : viewguestscanvas.configure(scrollregion = viewguestscanvas.bbox("all")))

        #Another frame in the canvas
        self.viewguestslistframe = Frame(viewguestscanvas) 
        viewguestscanvas.create_window((0,0) , window = self.viewguestslistframe, anchor = "nw")

        self.alertincanvas = Label(self.viewguestslistframe ,  text = "CLICK VIEW LIST TO GET ALL USERS." , font = ('CHARLESWORTH' , 15)).pack()

        self.searchframe = Frame(self.master , width = 555 , bg = "#fce4ec",  height = 120 , relief = 'ridge' , bd = 10)
        self.searchframe.place(x=810 , y=540)

        # This is the function used to search for a user in the system
        def searchuser():
            #Adding a scrollbar .......
            #mainframe
            self.viewguestsframe = Frame(self.master , width = 420 , bg = "#FFFFFF",  height = 300 , relief = 'ridge' , bd = 10)
            self.viewguestsframe.place(x=810 , y=220)

            #Adding canvas in the frame
            viewguestscanvas = Canvas(self.viewguestsframe)
            viewguestscanvas.pack(side = LEFT , fill = BOTH , expand = 1)


            viewguestsscrollbar = ttk.Scrollbar(self.viewguestsframe , orient = VERTICAL, command = viewguestscanvas.yview)
            viewguestsscrollbar.pack(side = RIGHT , fill = Y)

            viewguestscanvas.configure(yscrollcommand =viewguestsscrollbar.set)
            viewguestscanvas.bind('<Configure>' , lambda e : viewguestscanvas.configure(scrollregion = viewguestscanvas.bbox("all")))

            #Another frame in the canvas
            self.viewguestslistframe = Frame(viewguestscanvas) 
            viewguestscanvas.create_window((0,0) , window = self.viewguestslistframe, anchor = "nw")
            mb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nana#773_9z",
            database="hotel"
            )
            my_cursor = mb.cursor()
            my_cursor.execute("SELECT *FROM Guest_Info WHERE phone_no ="+self.searchNumberEntry.get())
            guest_info = my_cursor.fetchall()

            print_records=""

            for guest in guest_info:
                print_records +="First Name : "+ str(guest[1]) + "\n" +"Last Name : " + str(guest[2])  + "\n" +"Email : " + str(guest[3]) + "\n" + "Phone Number : "+ str(guest[4]) + "\n" + "Room Type : " + str(guest[7])+"\n\n\n\n"
            
            NameLabel= Label(self.viewguestslistframe , text = print_records ,font = ('CHARLESWORTH' , 15) , compound = LEFT ).pack(side = LEFT)
            mb.commit()
            mb.close()


        searchTel_no = StringVar()
        self.searchByPhone = Label(self.searchframe , text = "Enter Phone Number Of The Customer" , bg = "#fce4ec" ,font = ('CHARLESWORTH' , 15) , compound = LEFT ).place(x = 55 , y = 5)
        self.searchNumberEntry = Entry(self.searchframe ,textvariable = searchTel_no , width = 17  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.searchNumberEntry.place(x =120 , y = 35)

        self.searchButton = Button(self.searchframe , text = "SEARCH" , command = searchuser).place(x=202 , y=65)

        self.PriceLabel = Label(self.master ,text = "TOTAL PRICE : " ,  bg = "#fce4ec" , font = ('CHARLESWORTH' , 25) )
        self.PriceLabel.place(x=850 , y=680)

        self.AMOUNTLabel = Label(self.master ,text = "0000.00" ,  bg = "#fce4ec" , font = ('CHARLESWORTH' , 25) )
        self.AMOUNTLabel.place(x=1100 , y=680)

    
    def StaffContact(self):
        self.newWindow = Toplevel(self.master)
        self.app = Staff_info_window(self.newWindow)

        


class Staff_info_window(HomeWindow):
    def __init__(self , master):
        self.master = master
        self.master.title("Hotel Management-MNG. STAFF CONTACT")
        self.master.iconbitmap("./IMAGE/Graphicloads-Polygon-Files.ico")
        self.master.geometry("700x200")
        self.master.config(bg = "#ffebee")

        self.Ceolabel = Label(self.master , text = "CEO            - RODNEY OWUSU AGYEMAN  - CONTACT(7997407569) " , font = ('CHARLESWORTH 13 bold italic' ) ,bg = "#ffebee" , anchor = CENTER).pack()
        self.Ceolabel = Label(self.master , text = "CEO            - SHRUTHI KUMARI        - CONTACT(9334716004) " , font = ('CHARLESWORTH 13 bold italic' ) ,bg = "#ffebee" , anchor = CENTER).pack()
        self.Ceolabel = Label(self.master , text = "CEO            - DEEEPAK GARG          - CONTACT(9996509558) " , font = ('CHARLESWORTH 13 bold italic' ) ,bg = "#ffebee" , anchor = CENTER).pack()
        self.Ceolabel = Label(self.master , text = "MANAGER        - SAMSON NKRUMAH KWAKU  - CONTACT(7997407569) " , font = ('CHARLESWORTH' , 13) ,bg = "#ffebee" , anchor = CENTER).pack()
        self.Ceolabel = Label(self.master , text = "BUSINESS ANAL. - EDMOND ANING          - CONTACT(7997407569) " , font = ('CHARLESWORTH' , 13) ,bg = "#ffebee" , anchor = CENTER).pack()
        self.Ceolabel = Label(self.master , text = "ASST. MANAGER  - MAXWELL FRANKLIN  - CONTACT(7997407569) " , font = ('CHARLESWORTH' , 13) ,bg = "#ffebee" , anchor = CENTER).pack()



class signupWindow(HOMEPAGE):
    def __init__(self , master):
        self.master = master
        self.master.title("Hotel Management-SIGNUP")
        self.master.iconbitmap("./IMAGE/Graphicloads-Polygon-Files.ico")
        self.master.geometry("1366x768")
        self.master.config(bg = "#ffebee")
        
        global loginframe
        self.loginlabel = Label(self.master , text = "SIGNUP" , font = ('arial' , 35 , 'italic') , bg = "#ffebee" , fg ="black" )
        self.loginlabel.pack(side = TOP )

        self.loginframe = Frame(self.master , width = 1000 , bg = "#fce4ec",  height = 1000 , relief = 'ridge' , bd = 2)
        self.loginframe.place(x=150 , y=120)

        def details_stored():

            #THIS IS FOR CREATING THE TABLE FOR USER SIGNUP DETAILS.
            # my_cursor.execute("""CREATE TABLE USER_DETAILS (
            #                         userid INT AUTO_INCREMENT PRIMARY KEY,
            #                         username VARCHAR(200) NOT NULL, 
            #                         firstname VARCHAR(200) NOT NULL,
            #                         lastname VARCHAR(200) NOT NULL, 
            #                         email VARCHAR(200) NOT NULL, 
            #                         password VARCHAR(200) NOT NULL,
            #                         DOB DATE NOT NULL
            #                         )""")

            def fieldchecker(n):
                if n == "" or n ==" ":
                    return 1


            usernamevalue = self.UserNameEntry.get()
            firstnamevalue = self.FirstNameEntry.get()
            lastnamevalue = self.LastNameEntry.get()
            emailvalue = self.EmailNameEntry.get()
            passwordvalue =self.PasswordNameEntry.get()

            u = fieldchecker(usernamevalue)
            f =fieldchecker(firstnamevalue) 
            l = fieldchecker(lastnamevalue)
            e =fieldchecker(emailvalue)
            p =fieldchecker(passwordvalue)

            if u == 1 or f == 1 or l == 1 or e == 1 or p ==1 :
                messagebox.showwarning("ERROR!" , "Fill all spaces....",parent = self.master)
                master.destroy()
            
            else:
                #INSERTING INTO DATABASE .

                mb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nana#773_9z",
                database="hotel"
                )
                my_cursor = mb.cursor()
                s = "INSERT INTO user_details(username ,firstname ,lastname , email , password , DOB) VALUES(%s , %s , %s , %s , %s , %s)"
                data = (f"{self.UserNameEntry.get()}",f"{self.FirstNameEntry.get()}" ,  f"{self.LastNameEntry.get()}" , f"{self.EmailNameEntry.get()}" ,f"{self.PasswordNameEntry.get()}" ,f"{self.year.get()}-{self.month.get()}-{self.day.get()}" )
                my_cursor.execute(s,data)
                mb.commit()
                mb.close()

                messagebox.showinfo("SAVED!" , "Your Details Has Been Saved Successfully." , parent = self.master)

                #Closing the SignUp Window after all details has been saved 
                master.destroy()




        u_name = StringVar()
        self.fieldsUsername = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Username : " ,50 , 50 )
        self.UserNameEntry = Entry(self.loginframe ,textvariable = u_name , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" )  )
        self.UserNameEntry.place(x = 350 , y = 70)

        f_name = StringVar()
        self.fieldsFirstName = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Firstname : " ,50 , 120 )
        self.FirstNameEntry = Entry(self.loginframe ,textvariable = f_name , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.FirstNameEntry.place(x = 350 , y = 140)

        l_name = StringVar()
        self.fieldsLastName = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Lastname : " ,50 , 200 )
        self.LastNameEntry = Entry(self.loginframe ,textvariable = l_name , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.LastNameEntry.place(x = 350 , y = 220)

        mail = StringVar()
        self.fieldsEmail = AnyName(self.loginframe ,"./IMAGE/email.jpg" , "Email : " ,50 , 280 )
        self.EmailNameEntry = Entry(self.loginframe ,textvariable = mail , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" ) )
        self.EmailNameEntry.place(x = 350 , y = 300)

        u_password = StringVar()
        self.fieldspassword = AnyName(self.loginframe ,"./IMAGE/passwordImage.png" , "Password : " ,50 , 360 )
        self.PasswordNameEntry = Entry(self.loginframe ,textvariable = u_password , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" ) , show = "*")
        self.PasswordNameEntry.place(x = 350 , y = 380)

        self.date_image = ImageTk.PhotoImage(Image.open("./IMAGE/DateImage.jpg"))
        self.DateLabel = Label(self.loginframe ,image =self.date_image , text = "Date O/B: ",font = ('CHARLESWORTH' , 35 ) , compound = LEFT , bg ="#fce4ec" )
        self.DateLabel.place(x=50 , y=440)
        # self.DateDay = Spinbox(self.loginframe  , from_ = 0 , to=31, width = 10)
        self.DateDayLabel = Label(self.loginframe ,text = "Day" , bg ="#fce4ec").place(x=350 , y=440)
        self.DateDiv = Label(self.loginframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 35 ) ).place(x=420 , y=440)
        self.DateMonthLabel = Label(self.loginframe ,text = "Month" , bg ="#fce4ec").place(x=450 , y=440)
        self.DateDiv1 = Label(self.loginframe , text = "/", bg ="#fce4ec" , font = ('CHARLESWORTH' , 35 ) ).place(x=520 , y=440)
        self.DateYearLabel = Label(self.loginframe ,text = "Year" , bg ="#fce4ec").place(x=550 , y=440)
        
        def dropdownRange(start , end):
            end = end+1
            options = []
            for i in range(start,end):
                options.append(i)
            return options

        days = dropdownRange(1,31)
        self.day =IntVar()
        self.day.set(days[0])
        self.DateDay = OptionMenu(self.loginframe , self.day,*days ).place(x=350 , y=460)

        months = dropdownRange(1,12)
        self.month =IntVar()
        self.month.set(months[0])
        self.DateDay = OptionMenu(self.loginframe , self.month,*months ).place(x=450 , y=460)

        years = dropdownRange(1980,2005)
        self.year =IntVar()
        self.year.set("1990")
        self.DateDay = OptionMenu(self.loginframe , self.year,*years ).place(x=550 , y=460)

        


        self.Submit_image = ImageTk.PhotoImage(Image.open("./IMAGE/Submit.jpg"))
        self.SubmitButton = Button(self.loginframe, image=self.Submit_image , border = 0 , command = details_stored )
        self.SubmitButton.place(x = 350 , y = 520)


    


         
# class MessageShowInfo(Tk):
#     def __init__(self ,master, title , text):
#         self.messagebox.showinfo(title , text)

class HomeForms(Tk):
    def __init__(self , master , fieldtext , Lx , Ly):
        self.loginframe = master
        self.FirstNameLabel = Label(self.loginframe , text =fieldtext ,font = ('CHARLESWORTH' , 20) , compound = LEFT , bg ="#fce4ec" )
        self.FirstNameLabel.place(x=Lx, y=Ly)

class AnyName(Tk):
    def __init__(self,master,path ,fieldtext , Lx , Ly):
        self.loginframe = master 
        self.username_image = ImageTk.PhotoImage(Image.open(path))
        self.UserNameLabel = Label(self.loginframe ,image =self.username_image , text =fieldtext ,font = ('CHARLESWORTH' , 35 ) , compound = LEFT , bg ="#fce4ec" )
        self.UserNameLabel.place(x=Lx , y=Ly)
        

#THis is a test version

d = HOMEPAGE(root)

root.mainloop()