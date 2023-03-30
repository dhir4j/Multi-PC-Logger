# File name: pclogger/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PC
import json

@csrf_exempt
def log_pc_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pc_name = data['pc_name']
        os = data['os']
        version = data['version']
        ram = data['ram']
        hdd = data['hdd']
        ip_address = data['ip_address']

        # Create a new PC object and save it to the database
        pc = PC(pc_name=pc_name, os=os, version=version, ram=ram, hdd=hdd, ip_address=ip_address)
        pc.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failed'})
    
from django.http import HttpResponse

def log_pc_data(request):
    return HttpResponse('Hello, world!')
