# import necessary packages
import email.message
from email import charset
import smtplib

#create message object instance
def send():
    try:
        html = open('libs/assets/email.html', 'r')

        charset.add_charset('utf-8', charset.QP, charset.QP, 'utf-8')
        msg = email.message.Message()

        #configurar os parâmetros da mensagem

        password = "your password"
        msg['From'] = "your mail"
        msg['To'] = "mail to send"
        msg['Subject'] = "Aviso de instabilidade"
        msg.add_header('content-type', 'text/html')
        msg.set_charset('utf8')
        msg.get_content_charset()
        msg.set_payload(html.read().encode('utf8'))

        #create server
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()

        #Credenciais de login para enviar o e-mail
        server.login(msg['from'], password)

        # send the message via the server.
        server.sendmail(msg['from'], msg['To'], msg.as_string()) 

        server.quit()
        print("successfully sent email to "+msg['To']+":") 
    except:
        send()
