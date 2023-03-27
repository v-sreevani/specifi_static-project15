from django.shortcuts import render

# Create your views here.

def second_specific_static(request):
    return render(request,'second_specific_static.html')