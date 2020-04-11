import os
ins="""
84 90 91 04 90 91 01 90 91 12 90 99 79 09 115
90 91 15 90 91 19 90 91 11 90 91 14 90 91 00
90 91 05 90 91 15 90 91 00 90 91 01 90 99 99 09 99
90 91 11 90 91 10 90 91 18 90 91 01 90 91 14 90 91 16"""

inss=ins.split()
print(inss)
st=""
for ascii in inss:
    st+=chr(int(ascii))
# print(st)
print(os.getcwd())
os.removedirs("test_of_vscode")