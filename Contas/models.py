from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField

# classes de login
class UserManager(BaseUserManager):
    def Create_User(self, email, Nome_completo, CPF, Curso, Registro_Academico,Telefone,password=None, active=True, staff=False,
                    Socio=False):
        if not email:
            raise ValueError('Usuário deve ter um email')
        if not password:
            raise ValueError('Usuário deve ter uma Senha')
        user_obj = self.model(
            email=self.normalize_email(email)

        )

        user_obj.Nome_completo = Nome_completo
        user_obj.CPF = CPF
        user_obj.Curso = Curso
        user_obj.Registro_Academico = Registro_Academico
        user_obj.Telefone = Telefone
        user_obj.is_staff = staff
        user_obj.Socio = Socio
        user_obj.is_active = active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, Nome_completo, CPF, Curso, Registro_Academico,Telefone, password=None):
        user_obj = self.Create_User(
            email,
            Nome_completo=Nome_completo,
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

    def create_superuser(self, email, Nome_completo, CPF, Curso, Registro_Academico,Telefone, password=None):
        user_obj = self.Create_User(
            email=email,
            Nome_completo=Nome_completo,
            CPF=CPF,
            Curso=Curso,
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
    ('Tecnologia em Controle e Automação', 'Tecnologia em Controle e Automação'),
    ('Tecnologia em Design Gráfico', 'Tecnologia em Design Gráfico'),
    ('Tecnologia em Radiologia', 'Tecnologia em Radiologia'),
    ('Tecnologia em Sistemas de Telecomunicação', 'Tecnologia em sistemas de Telecomunicação')
    )
    Nome_completo = models.CharField(max_length=255, null=True,unique=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_staff = models.BooleanField(default=False, null=True,verbose_name='Diretor')
    Socio = models.BooleanField(default=False, null=True)
    CPF = BRCPFField(max_length=14,unique=True,blank=False,null=False)
    Curso = models.CharField(max_length=255, choices=Cursos, null=True)
    Registro_Academico = models.CharField(max_length=255, blank=True,unique=True)
    Telefone = models.CharField(max_length=13,null = False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Nome_completo', 'CPF', 'Curso', 'Registro_Academico','Telefone']

    def __str__(self):
        return self.Nome_completo

    def get_nome_completo(self):
        return self.Nome_completo

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

    @property
    def get_socio(self):
        return self.Socio

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['Nome_completo']