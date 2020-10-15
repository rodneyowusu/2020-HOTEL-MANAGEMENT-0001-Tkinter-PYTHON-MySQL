from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox

#cd desktop/PYTHONTEAM/PYTHON-PROJECT
global root
root = Tk()

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

        self.fieldsUsername = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Username : " ,50 , 50 , 350 , 70 , "NULL")


        self.fieldspassword = AnyName(self.loginframe ,"./IMAGE/passwordImage.png" , "Password  : " ,50 , 120 , 350 , 140 , "*")

        self.Submit_image = ImageTk.PhotoImage(Image.open("./IMAGE/Submit.jpg"))
        self.SubmitButton = Button(self.loginframe , image=self.Submit_image , border = 0  , command = self.thehompage)
        self.SubmitButton.place(x = 350 , y = 200)


    def thehompage(self):
        self.newWindow = Toplevel(self.master)
        self.app = HOMEPAGE(self.newWindow)

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

       
        self.fieldsUsername = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Username : " ,50 , 50 , 350 , 70 , "NULL")


        self.fieldsFirstName = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Firstname : " ,50 , 120 , 350 , 140 , "NULL")


        self.fieldsLastName = AnyName(self.loginframe ,"./IMAGE/username-icon.jpg" , "Lastname : " ,50 , 200 , 350 , 220 , "NULL")
        
        self.fieldsEmail = AnyName(self.loginframe ,"./IMAGE/email.jpg" , "Email : " ,50 , 280 , 350 , 300 , "NULL")
        
        self.fieldspassword = AnyName(self.loginframe ,"./IMAGE/passwordImage.png" , "Password : " ,50 , 360 , 350 , 380 , "*")
        

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
        self.year.set(months[0])
        self.DateDay = OptionMenu(self.loginframe , self.year,*years ).place(x=550 , y=460)

        def details_stored():
            messagebox.showinfo("SAVED!" , "Your Details Has Been Saved Successfully.")
            master.destroy()


        self.Submit_image = ImageTk.PhotoImage(Image.open("./IMAGE/Submit.jpg"))
        self.SubmitButton = Button(self.loginframe, image=self.Submit_image , border = 0  , command = details_stored)
        self.SubmitButton.place(x = 350 , y = 520)


    


         
# class MessageShowInfo(Tk):
#     def __init__(self ,master, title , text):
#         self.messagebox.showinfo(title , text)


class AnyName(Tk):
    def __init__(self,master,path ,fieldtext , Lx , Ly ,Ex , Ey , theshow):
        self.loginframe = master 
        global name_var
        name_var = StringVar()
        self.username_image = ImageTk.PhotoImage(Image.open(path))
        self.UserNameLabel = Label(self.loginframe ,image =self.username_image , text =fieldtext ,font = ('CHARLESWORTH' , 35 ) , compound = LEFT , bg ="#fce4ec" )
        self.UserNameLabel.place(x=Lx , y=Ly)
        self.UserNameEntry = Entry(self.loginframe ,textvariable = name_var , width = 50  , bd = 2 , font = ('Arial' , 14 , "italic" ) , show = theshow ,  )
        self.UserNameEntry.place(x = Ex , y = Ey)



d = HOMEPAGE(root)

root.mainloop()