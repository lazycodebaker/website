
import json
from django.shortcuts import render
from .models import Certificate
from django.http import HttpRequest, HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

def Home(request):
    return render(request, 'index.html')

@csrf_exempt
def VerifyCertificate(request):
    
    if request.method == 'POST':
        enrollment_id = json.loads(request.body)['enrollment_id']

        certificate = Certificate.objects.filter(enrollment_id=enrollment_id).first()

        if certificate:
            context = {
                'enrollment_id': certificate.enrollment_id,
                'username': certificate.username,
                'verified': certificate.verified,
                'certificate': certificate.certificate.url
            }

            return JsonResponse(context, safe=False)

        else:
            context = {
                'enrollment_id': None,
                'username': None,
                'verified': None,
                'certificate': None
            }

            return JsonResponse(context, safe=False)             

    return render(request, 'VerifyCertificate.html')