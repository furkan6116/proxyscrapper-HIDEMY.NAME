from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
#chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-logging')
print("İşlem Başlatılıyor")
chrome = webdriver.Chrome(options=chrome_options)
sehir = input("Hangi Ülkeler Olsun (boş bırakırsan tüm ülkeler olur) (Ülke kodlarını büyük harfle yanyana yazman gerek) (TRENAU GİBİ) :")
ping = input("Maksimum kaç ms olsun (örn 600) (ayarlamak istemiyorsan boş bırak) :")
print("Evet için 1 Hayır için 0 gönder.")
http = input("Http proxyleri eklensinmi :")
https = input("Https proxyleri eklensinmi :")
socks4 = input("Socks4 proxyleri eklensinmi :")
socks5 = input("Socks5 proxyleri eklensinmi :")
types = ""
if(http == "1"):
    types += "h"
if(https == "1"):
    types += "s"
if(socks4 == "1"):
    types += "4"
if(socks5 == "1"):
    types += "5"
if sehir == "":
    sehir = "AFALARAMAUAZBDBEBABRBGKHCACLCNCOHRCZDKDOECEGSVEEFRGEDEGHGRHNHKHUINIDIRIQILITJPKZKEKRLBLYLTLUMWMYMXMDMENPNLNGNOPKPSPAPEPLPTRORURSSGSKSIZAESSETWTJTZTHTRUGUAGBUSVNZW"
if ping == "":
    ping = "999999"

def getlisted(listvalue = 0):
    global types
    chrome.get("https://hidemy.name/en/proxy-list/?country=" + sehir +"&maxtime=" + str(ping) + "&start=" + str(listvalue) + "&type=" + types)
    print("Lütfen Bekle")
    def bekle():
        try:
            chrome.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[4]/table/tbody")
        except:
            time.sleep(2)
            bekle()
    bekle()
    for tr in chrome.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[4]/table/tbody").find_elements_by_tag_name("tr"):
        open("proxyler.txt", "a").write(tr.find_elements_by_tag_name("td")[0].text + ":" + tr.find_elements_by_tag_name("td")[1].text + "\n")
        print(tr.find_elements_by_tag_name("td")[0].text + ":" + tr.find_elements_by_tag_name("td")[1].text)
    if len(chrome.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[4]/table/tbody").find_elements_by_tag_name("tr")) == 0:
        print("İşlem Tamam")
        chrome.quit()
        chrome.close()
    else:
        getlisted(listvalue + 64)
getlisted()

