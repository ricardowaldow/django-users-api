from operator import imod
from rest_framework import viewsets
from users.models import User
from users.serializer import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """ 
    Exibir todos os usuários 
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer