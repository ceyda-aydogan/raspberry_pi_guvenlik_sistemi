import RPi.GPIO as GPIO
import time
import PyV4L2Camera
from PyV4L2Camera.camera import Camera
import PIL
from PIL import Image
import smtplib
from gpiozero import LED

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

toaddr= 'ceyda.aydogan567@gmail.com'
me= 'ceyda.aydogan567@gmail.com'
Subject= 'güvenlik ihlali'
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
ledPin= LED(14)

while True:
    if GPIO.input(24):
        print("Hareket algılandı")
        
        GPIO.output(18,1)
        time.sleep(1)
        GPIO.output(18,0)
        time.sleep(1)
        
        ledPin.on()
        
        camera= Camera("/dev/video0")
        frame= camera.get_frame()
        img= Image.frombytes("RGB", (camera.width, camera.height), frame, "raw")
        img.save("image.jpg")
        camera.close()

        subject= 'Güvenlik ihlali'
        msg= MIMEMultipart()
        msg['Subject']= subject
        msg['From']= me
        msg['To']= toaddr
        fp= open('image.jpg','rb')
        img= MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
        server= smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user= 'ceyda.aydogan567@gmail.com', password= 'raspberrypi')
        server.sendmail.(me, toaddr, msg.as_string())
        server.quit()
        ledPin.off()
        time.sleep(2)                       

        
        
        
