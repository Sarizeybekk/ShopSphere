
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    metin="Btk kursiyerleri"
    context={"icerik1":metin}

    return render(request, 'index.html', context)
