# raspberry_pi_guvenlik_sistemi

Projemde;

- Raspberry Pi 3 B+
- PIR Sensörü
- Kamera
- Buzzer
- Jumper Kablo 
- Yeşil Led Işık

kullanarak bir güvenlik sistemi devresi yaptım.

Yukarıda belirttiğim sensörleri ve malzemeleri kullanarak hareket algılandığında ekrana “Hareket Algılandı” iletisini belirterek bir ses uyarısı ve yeşil ışık uyarısı vermek istedim. Aynı zamanda hareket algılandıktan sonra kamera ile sensöre yakalanan kişinin fotoğrafı çekilecek ve e-posta adresine gönderilecek.



## UYGULAMA

İlk olarak kameranın bağlantısını yaptım ve PIR sensörün GND çıkışını Raspberry Pi’ nin 6.pinine, OUT çıkışını GPIO24 pinine ve VCC çıkışını 5V olan 2.pine bağladım. Böylece PIR Sensörün bağlantılarını tamamlamış oldum. Daha sonra Led Işığın uzun bacağını GPIO14 pinine ve kısa bacağını 9.pin olan GND’ ye bağladım. Son olarak Buzzer’ ın bağlantısını yaptım. Buzzer’ın artı ucunu GPIO18 pinine diğer ucunu da 14.pin olan GND’ ye taktım. Devremin bütün bağlantılarını bu şekilde tamamlamış oldum. 

![alt text](https://github.com/ceyda-aydogan/raspberry_pi_guvenlik_sistemi/blob/main/IMG_20220109_165938.jpg)

![alt text](https://github.com/ceyda-aydogan/raspberry_pi_guvenlik_sistemi/blob/main/IMG_20220109_170304.jpg)

Daha sonra Raspberry üzerinden kodları yazdım.

Kodları çalıştırdığımızda PIR sensör hareketi algılıyor ve bunun bilgisi ekranda yazdırılıyor. Hareket algılandığında kamera çalışmaya başlıyor ve fotoğrafı çekip e-posta adresine gönderiyor. Aynı zamanda Led ışığı yanıyor ve Buzzer’ dan ses çıkışı sağlanıyor.


Uygulamanın videosuna bu bağlantıdan ulaşabilirsiniz: https://drive.google.com/file/d/1-kpvHAn-14KSiC4GFecO5TUOz67x79es/view?usp=sharing
