from dictionary import mest2
from dictionary import menmest2
from dictionary import wommest2
from dictionary import mest
from dictionary import menmest
from dictionary import wommest
from dictionary import mestob
from dictionary import mestob2
from dictionary import verb1
from dictionary import verb2

def ciclemen(text_input):
    
    string_str = " " + text_input
    for index in range(152):
        string_str = string_str.replace(mestob[index], mestob2[index])
    for index in range(256):
        string_str = string_str.replace(verb1[index], verb2[index])
    for index in range(200):
        string_str = string_str.replace(mest2[index], menmest2[index])
    for index in range(111):
        string_str = string_str.replace(mest[index], menmest[index])
    return string_str






def ciclewomen(text_input):
    string_str = " " + text_input
    for index in range(152):
        string_str = string_str.replace(mestob[index], mestob2[index])
    for index in range(256):
        string_str = string_str.replace(verb1[index], verb2[index])
    for index in range(200):
        string_str = string_str.replace(mest2[index], wommest2[index])
    for index in range(111):
       string_str = string_str.replace(mest[index], wommest[index])
    return string_str




