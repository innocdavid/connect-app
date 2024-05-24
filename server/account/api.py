from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(resquest):
    data = resquest.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })

    if form.is_valid():
        form.save()

        #send verification error later
    else:
        message = 'error in creating a user'

    return JsonResponse({'status': message})
