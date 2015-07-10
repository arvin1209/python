#Should open files and websites depenting on input#
#only works with Python 3
c=str(input("Enter work:"))
b="homework"#if you input homework a list of homework will come out
a="Youtube"
d="excel"
e="word"
f="powerpoint"
g="google"
h="netflix"
if c==b:
    print("""5 words,Python,Writing,250 words,Piano,Math,Read""")
    import webbrowser
    webbrowser.open('www.khanacademy.org/')
if c==a:
    import webbrowser
    webbrowser.open('www.youtube.com')
if c==g:
    import webbrowser
    webbrowser.open('www.google.com')
if c==d:
    import os
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Excel 2010.lnk")
if c==e:
    import os
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.lnk")
if c==f:
    import os
    os.startfile("C:\Program Files (x86)\Microsoft Office\Office14\POWERPNT.EXE")
if c==h:
    import webbrowser
    webbrowser.open('www.netflix.com')
