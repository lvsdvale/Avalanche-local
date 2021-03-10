import uuid
import smtplib
from email.message import EmailMessage
from django.conf import settings
import ssl
from Contas.models import user

def get_file_path(_instance,filename):
    ext = filename.split(',')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

def Send_Esportes_Mail(usuario,modalidade):
    context = ssl.create_default_context()
    server = None
    try:
        server = smtplib.SMTP("smtp.gmail.com",settings.EMAIL_PORT)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        msg = EmailMessage()
        subject = f'Inscrição {modalidade.name} avalanche'
        body = f'Eaii, {usuario.name}\n Sua inscrição foi confirmada, seja bem vindo ao time de {modalidade.name}. Mal vejo a hora de ver sua garra vestindo a nossa camisa, qualquer dúvida entre em contato com o coordenador de {modalidade.name}\nTe espero nos treinos!\nAbaços\nPaul Lar.'
        to = f'{usuario.email}'
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = to
        server.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()


def Send_E_sports_Mail(usuario,game):
    context = ssl.create_default_context()
    server = None
    try:
        server = smtplib.SMTP("smtp.gmail.com", settings.EMAIL_PORT)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        msg = EmailMessage()
        subject = f'Inscrição {game.name} avalanche'
        body = f'Seja bem vindx ao E-sports do ursão !!! \n{usuario.name},recebemos sua inscrição logo entraremos em contato \nqualquer dúvida entrar em contato com a direção da A.A.A.E.A UTFPR-CT.'
        to = f'{usuario.email}'
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = to
        server.send_message(msg)
    except:
        pass
    finally:
        server.quit()




def Send_Acao_Mail(usuario,campanha):
    context = ssl.create_default_context()
    server = None
    try:
        server = smtplib.SMTP("smtp.gmail.com", settings.EMAIL_PORT)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        msg = EmailMessage()
        subject=f'Inscrição na ação Social:{campanha.name}'
        body=f'Olá {usuario.name}\nQue alegria ver você inscrito na ação {campanha.name}. Logo o time de social entrará em contato, pode ir preparando o coração!\nCarinhosamente,\nPaul Lar'
        to = f'{usuario.email}'
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = to
        server.send_message(msg)
    except:
        pass
    finally:
        server.quit()

def Send_Sign_Mail(Email,Nome):
    context = ssl.create_default_context()
    server = None
    try:
        server = smtplib.SMTP("smtp.gmail.com", settings.EMAIL_PORT)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        msg = EmailMessage()
        subject=f'Cadastro Concluido'
        body=f'Olaaaar {Nome}, seja bem vindo à plataforma oficial da AVALANCHE, \nAqui você vai poder se inscrever nas modalidades, adquirir produtos avalanche,  acompanhar informações sobre os eventos, acessar conteúdos exclusivos e muito mais!\nP.S. Fique ligado no nosso instagram para receber as atualizações do site\nCarinhosamente,\nPaul Lar'
        to = f'{Email}'
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = to
        server.send_message(msg)
    except:
        pass

    finally:
        server.quit()


def Send_Reset_Mail(Email,Senha):
    context = ssl.create_default_context()
    server = None
    usuario = user.objects.get(email=Email)
    try:
        server = smtplib.SMTP("smtp.gmail.com", settings.EMAIL_PORT)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        msg = EmailMessage()
        subject=f'Recuperação de senha'
        body=f'Fala tu,{usuario.name}\nEsquecer a senha até vale, só não vale esquecer de participar do parceladão!\nP.S. Tá ai sua cerveja, ops senha:{Senha}\nCarinhosamente,\nPaul Lar'
        to = f'{Email}'
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = to
        server.send_message(msg)
    except:
        pass

    finally:
        server.quit()


def Send_compra_mail(usuario,pedido):
    msg = EmailMessage()
    subject = f'Pedido: #{pedido.pk}'
    body = f'{usuario.name},Seu pedido número {pedido.pk} no valor de {pedido.total()*1.05:.2f} com pagamento via {pedido.pagamento} foi recebido! \n para mais informações entre em meus pedidos na sua conta'
    to = f'{usuario.email}'
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = to
    mail = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    mail.ehlo()
    mail.starttls()
    mail.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    mail.send_message(msg)
    mail.quit()

def Send_compra_update_mail(usuario,pedido):
    msg = EmailMessage()
    subject = f'Pedido: #{pedido.pk}'
    body = f'{usuario.name},Seu pedido número {pedido.pk} no valor de {(pedido.total()*1.05):.2f} com pagamento via {pedido.pagamento} atualizou o status para {pedido.status}'
    to = f'{usuario.email}'
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = to
    mail = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    mail.ehlo()
    mail.starttls()
    mail.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    mail.send_message(msg)
    mail.quit()