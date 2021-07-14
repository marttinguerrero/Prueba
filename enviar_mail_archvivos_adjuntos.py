import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

correo_personal = "marttinguerreroo@gmail.com"
contraseña = ""
destinatario = "@gmail.com"



msg = MIMEMultipart()


msg['From'] = correo_personal
msg['To'] = destinatario
msg['Subject'] = "Asunto"


body = "cuerpo del mail"


msg.attach(MIMEText(body, 'plain'))


filename = "leer_mails.py"
attachment = open(filename, "rb")


p = MIMEBase('application', 'octet-stream')


p.set_payload((attachment).read())



encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)


msg.attach(p)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(correo_personal,contraseña)


text = msg.as_string()

server.send_message(msg)

server.quit()











































# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders

# fromaddr = input("Ingrese su mail: ")
# password = input("Ingrese su contraseña: ")
# toaddr = input("A quien se lo quiere mandar: ")


# # instance of MIMEMultipart
# msg = MIMEMultipart()

# # storing the senders email address
# msg['De'] = fromaddr
# msg['Para'] = toaddr
# msg['Asunto'] = input("Escriba el asunto: ")

# # string to store the body of the mail
# body = input("Escriba el mail")

# # attach the body with the msg instance
# msg.attach(MIMEText(body, 'plain'))

# # open the file to be sent
# filename = "enviar_mail"
# attachment = open(filename, "rb")

# # instance of MIMEBase and named as p
# p = MIMEBase('application', 'octet-stream')

# # To change the payload into encoded form
# p.set_payload((attachment).read())


# # encode into base64
# encoders.encode_base64(p)

# p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# # attach the instance 'p' to instance 'msg'
# msg.attach(p)

# # creates SMTP session
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(fromaddr,password)

# # Converts the Multipart msg into a string
# text = msg.as_string()

# server.send_message(msg)

# server.quit()