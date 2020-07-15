#!"c:\users\barhama-niass\3d objects\memoire de fin d'etude m2\programmation\virtuelqg\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'servicer==0.11.14','console_scripts','servicer'
__requires__ = 'servicer==0.11.14'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('servicer==0.11.14', 'console_scripts', 'servicer')()
    )
