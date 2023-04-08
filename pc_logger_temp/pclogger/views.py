# pclogger/views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PC

@csrf_exempt
def add_pc_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pc = PC(os=data['os'], version=data['version'], ram=data['ram'], hdd=data['hdd'], ip_address=data['ip_address'])
        pc.save()
        return HttpResponse('Success!')
    else:
        return HttpResponse('Invalid request method.')
