## #1 DÜNYANIN EN KALİTELİ PROXY SCRAPPERİ
![enter image description here](https://media.giphy.com/media/Swg0grPl3LwlS38MCM/giphy.gif)

Diğer proxy scrapperlere nazaran **Hızlı, Kaliteli Ve Filtreli**  bir scripttir. **Ülke, Ping Ve Protokol Filtreleride Mevcut**
## Nasıl Çalışır
Geçenlerde kaliteli proxyler sağlayan bir web sitesi buldum. Fakat
bunları toplu bir txt dosyası halinde indirmenin paralı olduğunu gördüm. bende bunu **selenium** kullanarak otomatik hale getirdim. fakat **headless** parametresini kullandığım zaman sitedeki ddos koruması bizi ddos saldırısı zannedip isteği bloke ediyordu. bende headless parametresini kaldırmak zorunda kaldım. yani script çalıştıktan sonra bir chrome penceresi açılırsa sakın içeriğine dokunmayın script çalışmayabilir.(alta alma boyut değiştirme gibi işlemler yapabilirsiniz.)

 1. `python scrapper.py`
 2.  Açılacak chrome sekmesini alta alın o zaten işlem sonunda otomatik kapanacaktır.
 3. Varsa istediğiniz ülke kodlarını yanyana büyük harfle yazın (TRENAU Gibi) yada bir şey yazmadan entera basın .
 4. Maksimum ms miktarını yazın (600 gibi), veya yazmayın direk entera basın
 5. Sonrasında herbir Http,Https,Socks4,Socks5 Protokolünü isteyip istemediğini tek tek soracaktır. İstiyorsan 1 İstemiyorsan 0 a basarak devam et
 6. Şimdi İşlem tamamlandı demesini bekle. proxyler **proxyler.txt** adlı dosyaya kaydedilecektir.
