from django.shortcuts import render
from .models import User

def home(request):
    names = User.objects.all()
    context = {'message': names}
    return render(request, 'index.html', context)