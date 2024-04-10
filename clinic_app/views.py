from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView  
from .models import HomePage, AboutUs
from django.contrib.auth.forms import UserCreationForm


# Define app's name
app_name = 'clinic_app'

class HomePageView(ListView):
    template_name = 'index.html'  # Specify the template name

    def get_queryset(self):
        return HomePage.objects.all()

class AboutUsView(ListView):
    template_name = 'about.html'  

    def get_queryset(self):
        return AboutUs.objects.all()

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the homepage or a success page
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})