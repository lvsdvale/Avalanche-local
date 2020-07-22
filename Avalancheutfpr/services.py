import uuid
from mailer import send_mail
from django.conf import settings

def get_file_path(_instance,filename):
    ext = filename.split(',')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

def Send_Esportes_Mail(usuario,modalidade):
    subject=f'Inscrição {modalidade.name}'
    body=f'{usuario.Nome_completo} recebemos sua inscrição logo entraremos em contato \n qualquer dúvida entrar em contato'
    to=(usuario.email,)
    send_mail(subject=subject, message = body, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=to,fail_silently=False)
