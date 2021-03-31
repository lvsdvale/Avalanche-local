from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField
from phonenumber_field.modelfields import PhoneNumberField

# classes de login
class UserManager(BaseUserManager):
    def Create_User(self, email, name, CPF, Curso,Data,Genero,Registro_Academico,Telefone,password=None, active=True, staff=False,
                    Socio=False):
        if not email:
            raise ValueError('Usuário deve ter um email')
        if not password:
            raise ValueError('Usuário deve ter uma Senha')
        user_obj = self.model(
            email=self.normalize_email(email)

        )

        user_obj.name = name
        user_obj.CPF = CPF
        user_obj.Curso = Curso
        user_obj.Data = Data,
        user_obj.Genero = Genero,
        user_obj.Registro_Academico = Registro_Academico
        user_obj.Telefone = Telefone
        user_obj.is_staff = staff
        user_obj.Socio = Socio
        user_obj.is_active = active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, name, CPF, Curso, Registro_Academico,Telefone, password=None):
        user_obj = self.Create_User(
            email,
            name = name,
            CPF=CPF,
            Curso=Curso,
            Registro_Academico=Registro_Academico,
            Telefone = Telefone,
            password=password,
            staff=True,
            Socio=True
        )
        user_obj.save
        return user_obj

    def create_superuser(self, email, name, CPF, Curso,Data,Genero,Registro_Academico,Telefone, password=None):
        user_obj = self.Create_User(
            email=email,
            name=name,
            CPF=CPF,
            Curso=Curso,
            Data=Data,
            Genero=Genero,
            Registro_Academico=Registro_Academico,
            Telefone=Telefone,
            password=password,
            staff=True,
            Socio=True
        )
        user_obj.is_staff = True
        user_obj.is_superuser = True
        user_obj.save()
        return user_obj


class user(AbstractBaseUser, PermissionsMixin):
    Cursos = (
    ('Nenhum', 'Nenhum'), ('Administração', 'Administração'), ('Arquitetura e Urbanismo', 'Arquitetura e Urbanismo'),
    ('Bacharelado em Química', 'Bacharelado em Química'),
    ('Comunicação Organizacional', 'Comunicação Organizacional'),
    ('Design', 'Design'),
    ('Educação Física', 'Educação Física'),
    ('Engenharia Ambiental e Sanitária', 'Engenharia Ambiental e Sanitária'),
    ('Engenharia Civil', 'Engenharia Civil'),
    ('Engenharia de Computação', 'Engenharia de Computação'),
    ('Engenharia de Controle e Automação', 'Engenharia de Controle e Automação'),
    ('Engenharia Elétrica', 'Engenharia Elétrica'),
    ('Engenharia Eletrônica', 'Engenharia Eletrônica'),
    ('Engenharia Mecânica', 'Engenharia Mecânica'),
    ('Engenharia Mecatrônica', 'Engenharia Mecatrônica'),
    ('Licenciatura em Física', 'Licenciatura em Física'),
    ('Licenciatura em Letras Inglês', 'Licenciatura em Letras Inglês'),
    ('Licenciatura em Letras Português', 'Licenciatura em Letras Português'),
    ('Licenciatura em Matemática', 'Licenciatura em Matemática'),
    ('Licenciatura em Química', 'Licenciatura em Química'),
    ('Sistemas da Informação', 'Sistemas da Informação'),
    ('Tecnologia em Automação Industrial', 'Tecnologia em Automação Industrial'),
    ('Tecnologia em Design Gráfico', 'Tecnologia em Design Gráfico'),
    ('Tecnologia em Radiologia', 'Tecnologia em Radiologia'),
    ('Tecnologia em Sistemas de Telecomunicação', 'Tecnologia em sistemas de Telecomunicação')
    )
    sexo =(
        ("Masculino","Masculino"),
        ("Feminino", "Feminino"),
        ("Não-Binario", "Não-Binario")
    )


    name = models.CharField(max_length=255, null=True,unique=True,help_text="Digite o seu nome COMPLETO",verbose_name="Nome")
    email = models.EmailField(max_length=255, unique=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_staff = models.BooleanField(default=False, null=True,verbose_name='Diretor')
    Socio = models.BooleanField(default=False, null=True,choices=((True,"Sim"),(False,"Não")))
    CPF = BRCPFField(max_length=14,unique=True,blank=False,null=False)
    Data = models.DateField(auto_now_add=False,blank=True,null=True,verbose_name="Data de nascimento")
    Genero = models.CharField(max_length=255, choices=sexo, null=True,verbose_name="Sexo")
    Curso = models.CharField(max_length=255, choices=Cursos, null=True)
    Registro_Academico = models.IntegerField(blank=True,unique=True,null=True,help_text="Caso não é aluno da utfpr,deixar em Branco")
    Telefone = PhoneNumberField(null=False,blank=False,region='BR')
    termos = models.BooleanField(default=True, null=False,verbose_name="Termo de Aceite",choices=((True,"Aceito"),(False,"Recusado")))
    date_joined = models.DateTimeField(auto_now_add=True, null=True,verbose_name="Data de inscrição")
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','Registro_Academico', 'CPF','Genero', 'Curso','Telefone']

    def __str__(self):
        return self.name

    def get_nome_completo(self):
        return self.name

    def get_email(self):
        return self.email

    def get_CPF(self):
        return self.CPF

    def get_Curso(self):
        return self.Curso

    def get_Registro_Academico(self):
        return self.Registro_Academico

    def get_Telefone(self):
        return self.Telefone

    @property
    def get_staff(self):
        return self.is_staff

    def get_socio(self):
        return self.Socio

    def set_senha(self,senha):
        self.set_password(raw_password=senha)
        self.save()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']