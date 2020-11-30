import docx
import os


#.docx
#.txt
#.odt


#Чтение файлов и запись их в переменную для дальшейшей передачи в функции


def ConvertDocFile(path_file):

    doc = docx.Document(path_file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    #print('\n'.join(text))
    return ('\n'.join(text))


def ConvertTxtAndOdtfile(path_file):
    text=''
    f = open(path_file,'r',encoding='utf-8')
    for line in f:
        text+=str(line)
        
    
    return text










def ConvertFile(path_file):
    try:
        if os.path.splitext(path_file)[1]=='.docx':
            return ConvertDocFile(path_file)
        elif os.path.splitext(path_file)[1]=='.txt' or os.path.splitext(path_file)[1]=='.odt':
            return ConvertTxtAndOdtfile(path_file)
        else:
            return "Неподходящий формат"
    except:
        pass

