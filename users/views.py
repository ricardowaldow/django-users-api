""" Users App Views """
import json
from rest_framework import viewsets
from django.http import JsonResponse
from users.models import User
from users.serializer import UserSerializer
class UsersViewSet(viewsets.ModelViewSet):
    """
    Exibir todos os usuários
    """

    queryset = User.objects.all()

    serializer_class = UserSerializer

def user_login(request):
    """ User Login"""

    if request.method == 'GET':
        try:
            json_data = json.loads(request.body)
            client_email = json_data['email']
            client_password = json_data['password']

        except KeyError:
            response = {'message' : 'Invalid Arguments'}

        except BaseException:
            response = {'message' : 'Error Unknown'}

    user = User.objects.get(email = client_email)

    response = user.authenticate(client_email,client_password)

    return JsonResponse(response)
