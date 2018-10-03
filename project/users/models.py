from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from PIL import Image


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_('Nome de usuário:'), blank=True, max_length=255)

    # Profile Models
    image = models.ImageField(verbose_name='Foto de Perfil:',
                              default='default.jpg', upload_to='profile_pics')
    birth_date = models.DateField(_('Data de Nascimento:'), null=True, blank=True)
    cpf = models.CharField(_('CPF:'), max_length=50, blank=True)
    cnpj = models.CharField(_('CNPJ:'), max_length=50, blank=True)
    bio = models.TextField(_('Descrição:'), blank=True, default='')
    cep = models.CharField(_('CEP:'), max_length=50, blank=True)
    street = models.CharField(_('Rua:'), max_length=100, blank=True)
    number_home = models.CharField(_('Número:'), max_length=10, blank=True)
    neighborhood = models.CharField(_('Bairro:'), max_length=100, blank=True)
    city = models.CharField(_('Cidade:'), max_length=50, blank=True)
    state = models.CharField(_('Estado:'), max_length=50, blank=True)
    phone = models.CharField(_('Telefone:'), max_length=50, blank=True)
    cel_phone = models.CharField(_('Celular:'), max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    """def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)"""
