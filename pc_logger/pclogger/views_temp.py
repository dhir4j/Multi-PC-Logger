# pclogger/views.py
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PC
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .models import Alert
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

@csrf_exempt
def add_pc_info(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pc = PC(os=data['os'], version=data['version'], ram=data['ram'], hdd=data['hdd'], ip_address=data['ip_address'])
        pc.save()
        return HttpResponse('Success!')
    else:
        return HttpResponse('Invalid request method.')


# # def search_pc_info(request):
# #     if request.method == 'GET':
# #         ip_address = request.GET.get('ip_address', '')
# #         if ip_address:
# #             pcs = PC.objects.filter(ip_address=ip_address)
# #             # Render the index.html template instead of search.html
# #             return render(request, 'index.html', {'pcs': pcs, 'ip_address': ip_address})
# #         else:
# #             # Render the index.html template instead of search.html
# #             return render(request, 'index.html')
# #     else:
# #         return HttpResponse('Invalid request method.')

# #final
# # def search_pc_info(request):
# #     ip_address = request.GET.get('ip_address', '')
# #     pcs = []
# #     alerts = {}
    
# #     if ip_address:
# #         pcs = PC.objects.filter(ip_address=ip_address)
# #         # get the latest record for the IP address
# #         latest_pc = pcs.order_by('-timestamp').first()
# #         if latest_pc:
# #             # check if there are any changes in hdd, os version, or ram
# #             prev_pc = PC.objects.filter(ip_address=ip_address, timestamp__lt=latest_pc.timestamp).order_by('-timestamp').first()
# #             if prev_pc:
# #                 if prev_pc.hdd != latest_pc.hdd:
# #                     alerts['hdd'] = f'HDD capacity changed from {prev_pc.hdd} to {latest_pc.hdd}.'
# #                 if prev_pc.os != latest_pc.os or prev_pc.version != latest_pc.version:
# #                     alerts['os'] = f'OS version changed from {prev_pc.os} {prev_pc.version} to {latest_pc.os} {latest_pc.version}.'
# #                 if prev_pc.ram != latest_pc.ram:
# #                     alerts['ram'] = f'RAM capacity changed from {prev_pc.ram} to {latest_pc.ram}.'
    
# #     return render(request, 'index.html', {'pcs': pcs, 'ip_address': ip_address, 'alerts': alerts})



# #new final
# def search_pc_info(request):
#     pcs = []
#     alerts = {}
    
#     # Get the latest record for each IP address
#     latest_pcs = PC.objects.filter(id__in=PC.objects.values('ip_address').annotate(max_id=F('id')).values('max_id'))
    
#     # Check if there are any changes in hdd, os version, or ram
#     for latest_pc in latest_pcs:
#         prev_pc = PC.objects.filter(ip_address=latest_pc.ip_address, timestamp__lt=latest_pc.timestamp).order_by('-timestamp').first()
#         if prev_pc:
#             if prev_pc.hdd != latest_pc.hdd:
#                 alerts[latest_pc.ip_address] = f'HDD capacity changed from {prev_pc.hdd} to {latest_pc.hdd}.'
#             if prev_pc.os != latest_pc.os or prev_pc.version != latest_pc.version:
#                 alerts[latest_pc.ip_address] = f'OS version changed from {prev_pc.os} {prev_pc.version} to {latest_pc.os} {latest_pc.version}.'
#             if prev_pc.ram != latest_pc.ram:
#                 alerts[latest_pc.ip_address] = f'RAM capacity changed from {prev_pc.ram} to {latest_pc.ram}.'
    
#     return render(request, 'index.html', {'pcs': pcs, 'alerts': alerts})


# #test code below

# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import PC


# def index(request):
#     pcs = []

#     # Get the latest record for each IP address
#     latest_pcs = PC.objects.filter(id__in=PC.objects.values('ip_address').annotate(max_id=F('id')).values('max_id'))

#     # Check if there are any changes in hdd, os version, or ram
#     alerts = {}
#     for latest_pc in latest_pcs:
#         prev_pc = PC.objects.filter(ip_address=latest_pc.ip_address, timestamp__lt=latest_pc.timestamp).order_by('-timestamp').first()
#         if prev_pc:
#             if prev_pc.hdd != latest_pc.hdd:
#                 alerts[latest_pc.ip_address] = f'HDD capacity changed from {prev_pc.hdd} to {latest_pc.hdd}.'
#             if prev_pc.os != latest_pc.os or prev_pc.version != latest_pc.version:
#                 alerts[latest_pc.ip_address] = f'OS version changed from {prev_pc.os} {prev_pc.version} to {latest_pc.os} {latest_pc.version}.'
#             if prev_pc.ram != latest_pc.ram:
#                 alerts[latest_pc.ip_address] = f'RAM capacity changed from {prev_pc.ram} to {latest_pc.ram}.'

#     return render(request, 'index.html', {'pcs': pcs, 'alerts': alerts})


def search_pc(request):
    pcs = []
    ip_address = request.GET.get('ip_address', '')
    if ip_address:
        pcs = PC.objects.filter(ip_address=ip_address)
    return render(request, 'index.html', {'pcs': pcs, 'ip_address': ip_address})



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

    approved_alerts = set()
    if request.user.is_authenticated:
        approved_alerts = set(request.user.alert_set.filter(is_approved=True).values_list('ip_address', flat=True))
    alerts = {ip_address: message for ip_address, message in alerts.items() if ip_address not in approved_alerts}

    return render(request, 'index.html', {'pcs': pcs, 'alerts': alerts})

@login_required
def approve_alert(request, alert_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    alert = get_object_or_404(Alert, pk=alert_id)
    alert.is_approved = True
    alert.save()

    return redirect('home')
