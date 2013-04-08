from django.db import models

#from django.forms import ModelForm

class ubicacion(models.Model):

    municipios = models.CharField(max_length=100)
    parroquia = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    #lat = models.CharField(max_length=50)
    #lng = models.CharField(max_length=50)


    def __unicode__(self):
        return "Municipio: " +self.municipios + " Parroquia: " + self.parroquia + " Localidades: " + self.localidade

#class UbicacionForm(ModelForm):
#    class Meta:

#        model = ubicacion

