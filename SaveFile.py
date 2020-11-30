import docx
import os
import easygui
def SaveFileMain(fname,text):
    try:
        if fname is not None:
            if os.path.splitext(fname)[1]=='.docx':
                SaveDocFile(fname,text)
            elif os.path.splitext(fname)[1]=='.txt' or os.path.splitext(fname)[1]=='.odt':
                SaveTxt(fname,text)
            else:
                pass
    except:
        pass

def SaveDocFile(fname,text):
    doc = docx.Document()
    for i in text:
        doc.add_paragraph(i)
    doc.save(fname)
    easygui.msgbox('Файл сохранен %s' % fname)



def SaveTxt(fname,text):
    f = open(fname, 'w')
    
    for i in text:
        f.write(f"{i}\n")
    f.close()
    easygui.msgbox('Файл сохранен %s' % fname)