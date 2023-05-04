# pclogger/views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PC
from django.db.models import F

@csrf_exempt
def add_pc_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pc = PC(os=data['os'], version=data['version'], ram=data['ram'], hdd=data['hdd'], ip_address=data['ip_address'])
        pc.save()
        return HttpResponse('Success!')
    else:
        return HttpResponse('Invalid request method.')


def index(request):
    pcs = []

    # Get the latest record for each IP address
    latest_pcs = PC.objects.filter(id__in=PC.objects.values('ip_address').annotate(max_id=F('id')).values('max_id'))

    # Check if there are any changes in hdd, os version, or ram
    alerts = {}
    for latest_pc in latest_pcs:
        prev_pc = PC.objects.filter(ip_address=latest_pc.ip_address, timestamp__lt=latest_pc.timestamp).order_by('-timestamp').first()
        if prev_pc:
            if prev_pc.hdd != latest_pc.hdd:
                alerts[latest_pc.ip_address] = f'HDD capacity changed from {prev_pc.hdd} to {latest_pc.hdd}.'
            if prev_pc.os != latest_pc.os or prev_pc.version != latest_pc.version:
                alerts[latest_pc.ip_address] = f'OS version changed from {prev_pc.os} {prev_pc.version} to {latest_pc.os} {latest_pc.version}.'
            if prev_pc.ram != latest_pc.ram:
                alerts[latest_pc.ip_address] = f'RAM capacity changed from {prev_pc.ram} to {latest_pc.ram}.'

    return render(request, 'index.html', {'pcs': pcs, 'alerts': alerts})


def search_pc(request):
    pcs = []
    ip_address = request.GET.get('ip_address', '')
    if ip_address:
        pcs = PC.objects.filter(ip_address=ip_address)
    return render(request, 'index.html', {'pcs': pcs, 'ip_address': ip_address})
