#!"c:\users\babaev\desktop\����� ����� (2)\env\scripts\pythonw.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'tkintertable==1.3.2','gui_scripts','tablesapp'
__requires__ = 'tkintertable==1.3.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tkintertable==1.3.2', 'gui_scripts', 'tablesapp')()
    )
