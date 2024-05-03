from django.db import models


class Document(models.Model):
    pdf_file = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.pdf_file)

class STEP(models.TextChoices):
    SOLICITUD_EN_LINEA = 'SOLICITUD_EN_LINEA'
    AUTENTICACION_DEL_CLIENTE = 'AUTENTICACION_DEL_CLIENTE'
    INFORMACION_BASICA = 'INFORMACION_BASICA'
    PRESENTACION_Y_ACEPTACION_DE_LA_OFERTA = 'PRESENTACION_Y_ACEPTACION_DE_LA_OFERTA'
    FIRMA_DE_DOCUMENTOS = 'FIRMA_DE_DOCUMENTOS'
    CARGUE_DE_DOCUMENTOS = 'CARGUE_DE_DOCUMENTOS'
    CONFIRMACION_Y_ACTIVACION = 'CONFIRMACION_Y_ACTIVACION'

class Request(models.Model):
    step = models.CharField(choices=STEP.choices, max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.id)
