from django.shortcuts import render

# Create your views here.
from .models import Place,Team





def demo(request):
    obj=Place.objects.all()
    res=Team.objects.all()
    return render(request,"index.html",{'result':obj,'object':res})