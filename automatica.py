import pyautogui
import os
import time


def setup():
    print("""
    Bilgilendirme
        Tarayıcıyı açın. PDF'lerini alacağınız dersi seçin ve alıştırımayı açın.
        Botu çalıştırın. Bot çalışırken sistemle etkileşimde bulunmayın.

        Tarayıcınızın ve internetinizin hızına bağlı olarak sayfanın kaç saniyede yenilendiğini hesaplayın. (varsayılan 7sn)
        'ÇÖZÜMLÜ PDF' butonunun konumunu not alın ve botun çalışabilmesi için girin.

        Konumu x y biçiminde girin.

        $ 'bilmem ne' butonunun konumu: 55 45
            55 x, 45 y olur

    """)
    if input('Ready?(go) ') == 'go':
        os.system('clear')

        input('ENTER')
        cpdf = None
        while not cpdf:
            os.system('clear')
            cpdf = input(str(pyautogui.position())+'\nYENİLEMEK İÇİN "ENTER"\n\n"ÇÖZÜMLÜ PDF" butonunun konumu: ').split()
            if cpdf:
                cpdf = [int(i) for i in cpdf]
                os.system('clear')
                n = int(input('Sayfa kaç sn de bir yenilensin: '))
                os.system('clear')
                print('10sn sonra bot aktif olacak. Tarayıcıyı açın (tıklayın) ve bekleyin.')
                time.sleep(10)

        return cpdf, n

def bot(cpdf, n=7):
    x, y = cpdf[0], cpdf[1]
    for i in range(100):
        os.system('clear')
        print(i)
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.press('f5')
        time.sleep(n)

cpdf, n = setup()
bot(cpdf, n)

# 1190 346
# 5005 342
# 3094 374
