from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


from ipware import get_client_ip




# Order of precedence is (Public, Private, Loopback, None)
def home(request):
    ip = get_client_ip(request)
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward :
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip =""
    return HttpResponse(ip)
