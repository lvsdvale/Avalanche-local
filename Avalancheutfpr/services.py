import uuid
from django.core.mail.message import EmailMessage
from django.conf import settings
def get_file_path(_instance,filename):
    ext = filename.split(',')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
'''
def Send_Esportes_Mail(usuario,modalidade):
    email = EmailMessage(
        subject=f'Inscrição {modalidade.name}',
        body=f'{usuario.Nome_completo} recebemos sua inscrição logo entraremos em contato \n qualquer dúvida entrar em contato',
        from_email= 'lucas.vinicius@atleticautfpr.com.br',
        to=(usuario.email,),
        headers={'Reply_To':f'{usuario.email}'},
    )
    email.send(fail_silently=False)
'''