from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    resolutions = [
        '704x480',
        '720x480',
        '480x576',
        '544x576',
        '704x576',
        '720x576',
        '1280x720',
        '1920x1080',
        '3840x2160',
        '7680x4320',
    ]
    context = {
        'resolutions': resolutions
    }
    return render(request, 'home.html', context)