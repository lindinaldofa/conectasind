from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from location_field.models.spatial import LocationField
from django.utils.translation import gettext_lazy as _
import json

tel_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O número de telefone deve ser inserido no formato: '999999999'.")
estados = [('Acre', 'Acre'),('Alagoas', 'Alagoas'),('Amazonas', 'Amazonas'),('Amapá', 'Amapá'),('Bahia', 'Bahia'),('Ceará', 'Ceará'),('Distrito Federal', 'Distrito Federal'),('Espírito Santo', 'Espírito Santo'),('Goiás', 'Goiás'),('Maranhão', 'Maranhão'),('Minas Gerais', 'Minas Gerais'),('Mato Grosso do Sul', 'Mato Grosso do Sul'),('Mato Grosso', 'Mato Grosso'),('Pará', 'Pará'),('Paraíba', 'Paraíba'),('Pernambuco', 'Pernambuco'),('Piauí', 'Piauí'),('Paraná', 'Paraná'),('Rio de Janeiro', 'Rio de Janeiro'),('Rio Grande do Norte', 'Rio Grande do Norte'),('Rondônia', 'Rondônia'),('Roraima', 'Roraima'),('Rio Grande do Sul', 'Rio Grande do Sul'),('Santa Catarina', 'Santa Catarina'),('Sergipe', 'Sergipe'),('São Paulo', 'São Paulo'),('Tocantins', 'Tocantins'),]
cidades = json.load(open('/home/metropolitano/Apps/ConectaSind/conectasind/static/cidades.json'))

class UserDefault(AbstractUser):
    email = models.EmailField(_('e-mail'), unique=True)
    username = models.CharField('usuário', max_length=150, null=False, blank=False, default='')
    cpf = models.CharField('CPF', max_length=11, unique=True, null=True, blank=True)
    is_active = models.BooleanField('Ativo', default=True)
    avatar = models.ImageField("Selecionar Foto", upload_to='avatar/usuarios', null=True, blank=True)
    tel_user = models.CharField('Telefone', max_length=11, validators=[tel_regex], null=True, blank=True)
    data_nascimento = models.DateField("Data de Nascimento", auto_now=False, auto_now_add=False, null=True, blank=True)
    end_rua_user = models.CharField("Logradouro (rua, avenida...)", max_length=1024, null=True, blank=True)
    end_num_user = models.CharField('Nº', max_length=150, null=True, blank=True)
    end_cep_user = models.CharField("CEP", max_length=10, null=True, blank=True)
    end_bairro_user = models.CharField("Bairro", max_length=150, null=True, blank=True)
    end_comple_user = models.CharField("Complemento", max_length=1024, null=True, blank=True)
    estado_user = models.CharField('Estado', choices=estados, max_length=150, null=True, blank=True, default='Alagoas')
    cidade_user = models.CharField('Cidade', choices=cidades['Alagoas'], max_length=150, null=True, blank=True)
    localizacao = LocationField(based_fields=['end_rua_user','end_num_user','end_bairro_user','cidade_user','estado_user'], zoom=7, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name