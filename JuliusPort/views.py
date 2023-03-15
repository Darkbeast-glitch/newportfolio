from django.shortcuts import render
from .models import ContactMe, Blog
from django.contrib import messages

# Create your views here.



def HomePage(request):
    blogpost = Blog.objects.all()
    
    
    if request.method == "POST":
        
        fullname = request.POST['fullname']
        email = request.POST['email']
        message  = request.POST['comment']
        
        contactMe_form  = ContactMe(fullname=fullname, email=email, message=message)
        contactMe_form.save()
        

        messages.success(request, "Thank you for contacting me. I will get back to you as soon as I receive your message. I appreciate your interest and look forward to connecting with you soon.")
        
        
    context = {
        
        'blogpost':blogpost
    }
    
    return render(request, 'index.html', context)