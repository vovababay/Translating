from parse import ciclemen
from parse import ciclewomen
from tkinter import *
from tkinter import messagebox
import tkinter
import easygui
import getpass
from ConvertText import ConvertFile
from SaveFile import SaveFileMain




 
root=Tk()
root.geometry("1000x500")
root.title("МВД")
root.resizable(width=False,height=False)

#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

def keys(event):
    
    if event.keycode==88 and event.keysym!='x': 
        event.widget.event_generate("<<Cut>>")
    if event.keycode==86 and event.keysym!='v':
        event.widget.event_generate("<<Paste>>")
    if event.keycode==67 and event.keysym!='c':
        event.widget.event_generate("<<Copy>>")
    if event.keycode==65 and event.keysym!='a':
        event.widget.event_generate("<<SelectAll>>")
            
root.bind("<Control-KeyPress>",keys)

class File():
    

    def __init__(self):
        self.path_file=''

    def findfile(self):
            input_file = easygui.fileopenbox(default=f"C:\\Users\\{getpass.getuser()}\\Documents\\",filetypes=["*.docx","*.txt","*.odt"])
            self.path_file=input_file


def createNewWindow():
    text_lesson1="""
    Ручной ввод: 

    1)Впишите текст в поле слева.

    2)Нажмите на кнопку 'М' если текст повествуется в мужском роде или 'Ж' если в женском.

    3)Справа вы увидите готовый преобразованный текст.

    4)Текст можно сохранить в документ через кнопку 'Сохранить файл'.

    5)Впишите название и тип файла (.txt, .docx, .odt).
    """
    text_lesson2="""
    Автоматическое форматирование:

    1)Нажмите кноку 'Выбрать файл'.

    2)Выберите файл одного из типов (.docx, .txt, .odt).

    3)Нажмите кнопку 'Загрузить файл', после этого слева появится текст,\n который можно редактировать.

    4)Нажмите на кнопку 'М' если текст повествуется в мужском роде или 'Ж' если в женском.

    5)Справа вы увидите готовый преобразованный текст.

    6)Текст можно сохранить в документ через кнопку 'Сохранить файл'.

    7)Впишите название и тип файла (.txt, .docx, .odt).

    8)Нажмите кнопку сохранить.
    """

    newWindow = tkinter.Toplevel(root)
    
    newWindow['bg']='gray'
    newWindow.geometry("1200x750")
    newWindow.resizable(width=False,height=False)
    newWindow.title("Кратное руководство по программе")
    
    text1=tkinter.Text(newWindow,state=tkinter.DISABLED,font = ('calibri', 25))
    text1.place(width=575, height=750)
    text1.configure(state=tkinter.NORMAL)
    text1.insert('end',text_lesson1)
    text1.configure(state=tkinter.DISABLED)
    
    text2=tkinter.Text(newWindow,state=tkinter.DISABLED,font = ('calibri', 25))
    
    text2.place(width=575, height=750,x=625, y=0)
    text2.configure(state=tkinter.NORMAL)
    text2.insert('end',text_lesson2)
    text2.configure(state=tkinter.DISABLED)



def run():
    
    
    createNewWindow()




    file_user=File()
    
    
    
    text_out=Text(state=tkinter.DISABLED,font = ('calibri', 14))
    
    text_in=Text(font = ('calibri', 14))
    
    



    btn_path=Button(text="Выбрать файл",command=lambda: file_user.findfile(),font = ('calibri', 20, 'bold'))
    btn_path.place(x=10, y=10, width=270, height=30)
    
    load_file_btn=Button(text="Загрузить файл",command=lambda: input_file(text_in),font = ('calibri', 20, 'bold'))
    load_file_btn.place(x=360, y=10, width=270, height=30)
    
    
    


    save_file_btn=Button(text="Сохранить файл",command=lambda: save_file(text_out),font = ('calibri', 20, 'bold'))
    save_file_btn.place(x=720, y=10, width=270, height=30)

    
    
    button_transformation_men=Button(text="М",command=lambda: transformation_men(text_in,text_out),font = ('calibri', 20, 'bold'))
    button_transformation_women=Button(text="Ж",command=lambda: transformation_women(text_in,text_out),font = ('calibri', 20, 'bold'))
    button_clear=Button(text="Очистить вывод",command=lambda: clear_method(text_out),font = ('calibri', 20, 'bold'))


    Weak_Eye_btn=Button(text="С.З.",command=lambda: Weak_Eye(text_in,text_out,btn_path,load_file_btn,save_file_btn,button_transformation_men, button_transformation_women,button_clear),font = ('calibri', 40, 'bold'))
    Weak_Eye_btn.place(x=820, y=70, width=100, height=100)
    
    #photo=tkinter.PhotoImage(file=r"C:\\Users\\Babaev\\Desktop\\Новая папка (2)\\env\\glaz.png")
    #photo = PhotoImage(file=r"C:\\Users\\Babaev\\Desktop\\Новая папка (2)\\env\\glaz.png")
    
    
    
    
    #text_in.pack(side=tkinter.LEFT)
    text_in.place(x=10, y=180, width=480, height=300)
    text_out.place(x=510, y=180, width=480, height=300)
    
    
    
    
    
    button_transformation_men.place(x=340, y=70, width=150, height=30)
    
    button_transformation_women.place(x=500, y=70, width=150, height=30)
    
    button_clear.place(x=340, y=110, width=310, height=30)
    
    #Button(root, image=photo, command=lambda: print('click'),height = 40, width = 40).pack()
    

    def Weak_Eye(text_in,text_out,btn_path,load_file_btn,save_file_btn,button_transformation_men, button_transformation_women,button_clear):
        text_in.place_forget()
        text_out.place_forget()
        btn_path.place_forget()
        load_file_btn.place_forget()
        save_file_btn.place_forget()
        button_transformation_men.place_forget()
        button_transformation_women.place_forget()
        button_clear.place_forget()


        text_out=Text(state=tkinter.DISABLED,font = ('calibri', 30))
    
        text_in=Text(font = ('calibri', 30))

        btn_path=Button(text="Выбрать файл",command=lambda: file_user.findfile(),font = ('calibri', 35, 'bold'))
        btn_path.place(x=4, y=10, width=320, height=50)
        
        load_file_btn=Button(text="Загрузить файл",command=lambda: input_file(text_in),font = ('calibri', 35, 'bold'))
        load_file_btn.place(x=332, y=10, width=320, height=50)
        
        save_file_btn=Button(text="Сохранить файл",command=lambda: save_file(text_out),font = ('calibri', 35, 'bold'))
        save_file_btn.place(x=657, y=10, width=340, height=50)

        button_transformation_men=Button(text="М",command=lambda: transformation_men(text_in,text_out),font = ('calibri', 35, 'bold'))
        button_transformation_women=Button(text="Ж",command=lambda: transformation_women(text_in,text_out),font = ('calibri', 35, 'bold'))
        button_clear=Button(text="Очистить вывод",command=lambda: clear_method(text_out),font = ('calibri', 35, 'bold'))
        text_in.place(x=10, y=180, width=480, height=300)
        text_out.place(x=510, y=180, width=480, height=300)
        
        button_transformation_men.place(x=340, y=70, width=150, height=50)
        
        button_transformation_women.place(x=500, y=70, width=150, height=50)
        
        button_clear.place(x=320, y=125, width=350, height=50)

    def input_file(text_in):
        if file_user.path_file!='':
            result=ConvertFile(file_user.path_file)
            if result=='Неподходящий формат':
                messagebox.showerror('Ошибка формата', 'Неподходящий формат файла')
            else:
                text_in.insert('end', result)
        

    def save_file(text_out):
        fname=easygui.filesavebox(default=f"C:\\Users\\{getpass.getuser()}\\Documents\\",filetypes=["*.doc","*.txt","*.odt"])
        print(fname)
        SaveFileMain(fname,str(text_out.get('1.0', END)).split('\n'))       
        
        



    def clear_method(text_out):
        text_out.configure(state=tkinter.NORMAL)
        text_out.delete("1.0", 'end')
        text_out.configure(state=tkinter.DISABLED)
        

    def transformation_men(text_in, text_out):
        
        text_out.configure(state=tkinter.NORMAL)
        text_out.delete("1.0", 'end')
        text_out.insert('end',ciclemen(text_in.get('1.0', END)))
        text_out.configure(state=tkinter.DISABLED)

        
            

    def transformation_women(text_in, text_out):
        text_out.configure(state=tkinter.NORMAL)
        text_out.delete("1.0", 'end')
        text_out.insert('end',ciclewomen(text_in.get('1.0', END)))
        text_out.configure(state=tkinter.DISABLED)


run()
root.mainloop()
