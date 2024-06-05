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
    print(form)

    if form.is_valid():
        print('saving data')
        form.save()
        print('saving', form.save())
        print('data saved')

        #send verification error later
    else:
        print('error data not saved')
        message = 'error in creating a user'

    return JsonResponse({'status': message})
