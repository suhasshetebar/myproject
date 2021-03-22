import re

from HelperVariables import MyVars
from Regexes import regexes

def ScanContent(content):
    ScanRes = {}
    try:
        for regex in MyVars.RegexData:
            result = re.findall(MyVars.RegexData[regex], content)
            if result:
                ScanRes[regex] = result
    finally:
        return ScanRes