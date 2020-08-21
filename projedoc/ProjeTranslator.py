import time
import pyperclip
from googletrans import Translator
from win10toast import ToastNotifier



print("""
CiscoPython5 Grup
    Hüseyin Saçılık
""")

time.sleep(3)

yeni_deger = ""
while True:
    time.sleep(0.3)
    translates = Translator()
    ilk_deger = pyperclip.paste()
    if ilk_deger != yeni_deger:
        yeni_deger = ilk_deger
        print ("Değer Değişikliği: %s" % str(yeni_deger))
        c = translates.translate(yeni_deger,dest="tr").text
        print("""
         [>] {0} == {1}
        ----------------------------------------------------
        """.format(yeni_deger.upper(),c.upper()))
                
        toast = ToastNotifier()
        toast.show_toast("TRANSLATE {0}".format(pyperclip.paste()).lower(),msg=c)


