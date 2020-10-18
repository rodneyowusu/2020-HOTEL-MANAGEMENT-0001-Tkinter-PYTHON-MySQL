from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox
import mysql.connector

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
# my_cursor.close()


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
        self.master.config(bg = "#f8bbd0")
        

        self.loginlabel = Label(self.master , text = "LOGIN" , font = ('arial' , 35 , 'italic') , bg = "#f8bbd0" , fg ="black" )
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
                    messagebox.showinfo("CORRECT" , "LOGIN SUCCESSFUL")
                    break

            else:
                messagebox.showwarning("ERROR!" , "INCORRECT USERNAME OR PASSWORD")
                

            mb.commit()
            mb.close()
            master.destroy()



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





class signupWindow(HOMEPAGE):
    def __init__(self , master):
        self.master = master
        self.master.title("Hotel Management-SIGNUP")
        self.master.iconbitmap("./IMAGE/Graphicloads-Polygon-Files.ico")
        self.master.geometry("1366x768")
        self.master.config(bg = "#f8bbd0")
        
        global loginframe
        self.loginlabel = Label(self.master , text = "SIGNUP" , font = ('arial' , 35 , 'italic') , bg = "#f8bbd0" , fg ="black" )
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
                messagebox.showwarning("ERROR!" , "Fill all spaces....")
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

                messagebox.showinfo("SAVED!" , "Your Details Has Been Saved Successfully.")

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


class AnyName(Tk):
    def __init__(self,master,path ,fieldtext , Lx , Ly):
        self.loginframe = master 
        self.username_image = ImageTk.PhotoImage(Image.open(path))
        self.UserNameLabel = Label(self.loginframe ,image =self.username_image , text =fieldtext ,font = ('CHARLESWORTH' , 35 ) , compound = LEFT , bg ="#fce4ec" )
        self.UserNameLabel.place(x=Lx , y=Ly)
        

#THis is a test version

d = HOMEPAGE(root)

root.mainloop()