from django import forms
from .models import *
from django.core.validators import validate_image_file_extension

class Form_lance(forms.ModelForm):
    class Meta:
        model = lance
        fields = ['jogo','titulo','descricao']
class Form_contatos(forms.ModelForm):
    class Meta:
        model = contatos
        fields = ['name','email','assunto','mensagem']

class AlbumAdminForm(forms.ModelForm):
    class Meta:
        model = album
        fields = (
            "titulo",
            "capa",
        )

    fotos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=("Adicionar fotos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("fotos"):
            validate_image_file_extension(upload)

    def save_photos(self, album):
        """Process each uploaded image."""
        for upload in self.files.getlist("fotos"):
            foto = fotos(album=album, foto=upload)
            foto.save()


