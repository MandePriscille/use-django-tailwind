from django.shortcuts import render
from .models import Video

def home(request):
    video = Video.objects.all()
    context={
        'video':video
    }
    return render(request, 'pages/home.html', context)
