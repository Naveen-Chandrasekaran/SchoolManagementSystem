from tkinter import*
import random
import os

def __marksheet__():
       filename = 'School_Search_Page.py'
       os.system(filename)
       os.system('notepad'+filename)

def __Library__():
       filename = 'School_Library_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)

def __information__():
       filename = 'School_Std_info_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

    
       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'navajo white')
       
       Menu_title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'raise', bd = 13)
       Menu_title_Frame.grid(row = 0, column = 0, pady = 50)
       
       Menu_title_Label = Label(Menu_title_Frame, text = 'MENU', font = ('arial',30,'bold'), bg = 'navajo white')
       Menu_title_Label.grid(row = 0, column = 0, padx = 150)


       #========================================================FRAMES===================================================================
       Menu_Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Menu_Frame_1.grid(row = 1, column = 0, padx = 280)
       Menu_Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Menu_Frame_2.grid(row = 2, column = 0, pady = 7)
       Menu_Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Menu_Frame_3.grid(row = 3, column = 0, pady = 7)
       


       #========================================================LABELS===================================================================
       Label_1_STUDENTINFO = Label(Menu_Frame_1, text = 'STUDENT PROFILE', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_1_STUDENTINFO.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2_LIBRARYSYSTEM = Label(Menu_Frame_2, text = 'LIBRARY SYSTEM', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_2_LIBRARYSYSTEM.grid(row = 0, column = 0, padx = 60, pady = 5)
       Label_3_MARKSHEET = Label(Menu_Frame_3, text = 'MARKSHEET', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_3_MARKSHEET.grid(row = 0, column = 0, padx = 101, pady = 5)
       


       #========================================================BUTTONS===================================================================
       Button_1_VIEWINFO = Button(Menu_Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __information__)
       Button_1_VIEWINFO.grid(row = 0, column = 3, padx = 50)
       Button_2_VIEWLIBRARY = Button(Menu_Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Library__)
       Button_2_VIEWLIBRARY.grid(row = 0, column = 3, padx = 50)
       Button_3_VIEWMARKSHEET = Button(Menu_Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __marksheet__)
       Button_3_VIEWMARKSHEET.grid(row = 0, column = 3, padx = 50)
       
       

       root.mainloop()


       
       
if __name__ == '__main__':
       menu()
