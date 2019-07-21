from django import forms
from django.core.exceptions import ValidationError

def valida_codigo_postal(value):

   if value < 10000 or value > 99999:
    raise ValidationError('%s no parece ser un código postal' % value)


class RestauranteForm(forms.Form):
   name    = forms.CharField(label='Nombre', max_length=60, strip=True,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                      })
                            )

   cuisine = forms.CharField(label='Tipo de cocina', max_length=80, required=False)

   zipcode = forms.IntegerField(label='Código Postal',
                                validators=[valida_codigo_postal])