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
        global UserImage
        global myimage
        global AdminImage

        #This is a simple function used to display images .
        def ImageDisplay(imgpath):
            theimage = ImageTk.PhotoImage (Image.open(imgpath))
            return theimage
        
        #calling the above func to display an image
        myimage =ImageDisplay("./IMAGE/realhotelbg.jpg")  
        self.background_label = Label(master, image=myimage)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.myLabel = Label(master , text = ("HOTEL MANAGEMENT SYSTEM") , justify = CENTER ,font = "Helvetica 30 bold italic" , bg= "#ffffff" ).pack()

        UserImage = ImageDisplay("./IMAGE/UserButtonImage.png")
        self.button = Button(master , image =UserImage  , border = 0 ,command =self.thelogin)
        self.button.place(relx = 0.35, rely = 0.75, anchor = CENTER )

        AdminImage = ImageDisplay("./IMAGE/AdminButtonimage.png")
        self.button = Button(master , image =AdminImage  , border = 0 ,command = self.thelogin) 
        self.button.place(relx = 0.65, rely = 0.75, anchor = CENTER )

    def thelogin(self):
        self.newWindow = Toplevel(self.master)
        self.app = loginWindow(self.newWindow)

class loginWindow(HOMEPAGE):
    def __init__(self , master):
        self.master = master
        self.master.title("Hotel Management-LOGIN")
        self.master.iconbitmap("./IMAGE/Graphicloads-Polygon-Files.ico")
        self.master.geometry("1366x768")
        self.master.config(bg = "#f8bbd0")
        

        self.loginlabel = Label(self.master , text = "LOGIN" , font = ('arial' , 35 , 'italic') , bg = "#f8bbd0" , fg ="black" )
        self.loginlabel.pack(side = TOP )

        self.loginframe = Frame(self.master , width = 1000 , bg = "#f8bbd0",  height = 1000 , relief = 'ridge' , bd = 2)
        self.loginframe.place(x=150 , y=120)

        self.username_image = ImageTk.PhotoImage(Image.open("./IMAGE/username-icon.jpg"))

        self.UserNameLabel = Label(self.loginframe ,image =self.username_image , text = "Username : ",font = ('CHARLESWORTH' , 35 ) , compound = LEFT , bg ="#f8bbd0" )
        self.UserNameLabel.place(x=50 , y=50)


d = HOMEPAGE(root)

root.mainloop()