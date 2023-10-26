from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request, 'app.html')
def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
