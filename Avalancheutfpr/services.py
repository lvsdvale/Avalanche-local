import uuid
import smtplib
from email.message import EmailMessage
from django.conf import settings

def get_file_path(_instance,filename):
    ext = filename.split(',')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

def Send_Esportes_Mail(usuario,modalidade):
    msg = EmailMessage()
    subject=f'Inscrição {modalidade.name} avalanche'
    body=f'{usuario.Nome_completo} recebemos sua inscrição logo entraremos em contato \nqualquer dúvida entrar em contato com a direção da A.A.A.E.A'
    to = f'{usuario.email}'
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = to
    mail = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
    mail.ehlo()
    mail.starttls()
    mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
    mail.send_message(msg)
    mail.quit()
