from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['POST'])
def signup(resquest):
    data = resquest.data
    message = 'success'

    return JsonResponse({'status': message})
