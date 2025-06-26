from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('fullName')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})    
        
        return render(request, 'register_success.html', {'username': username})
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

