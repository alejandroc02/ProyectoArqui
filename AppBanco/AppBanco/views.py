from django.http import HttpResponse
from django.shortcuts import render

from  Document.models import Document

def home(request):
    return render(request, 'home.html')

def validate_otp(request):
    return render(request, 'validate_otp.html')

def upload_document(request):
    return render(request, 'upload_document.html')

def validate_otp(request):
    if request.method == 'POST':
        # Obtener el valor del campo 'otp' del formulario POST
        otp_entered = request.POST.get('otp')
        # Verificar si el OTP ingresado es igual a '123456'
        if otp_entered == '123456':
            return HttpResponse("OTP is valid")
        else:
            return HttpResponse("OTP is invalid")
    else:
        return render(request, 'validate_otp.html')

def upload_document(request):
    if request.method == 'POST':
        # Obtener el enlace del PDF del campo de texto del formulario POST
        pdf_link = request.POST.get('pdf_link')
        
        # Crear un nuevo objeto Document con el enlace del PDF
        new_document = Document.objects.create(pdf_file=pdf_link)
        new_document.save()
        
        return HttpResponse("Document uploaded successfully")
    else:
        return render(request, 'upload_document.html')