from django.shortcuts import render
from .models import Follower


# Create your views here.
def register(request):
    if request.POST:
        print(request.POST['email'])
    return render(request, 'register.html')


def main(request):
    if request.POST:
        model = Follower()
        model.name = request.POST.get('name', '')
        model.email = request.POST.get('email', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.password = request.POST.get('password', '')
        model.save()
        print(request.POST)
    return render(request, 'index.html')
