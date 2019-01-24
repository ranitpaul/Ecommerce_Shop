from django.shortcuts import render


def home_page(request):
    context = {
        
    }
    return render(request, 'home_page.html')

def about_page(request):
    return render(request, 'about_page.html')

def contact_page(request):
    return render(request, 'contacts/contact_page.html')