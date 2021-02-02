from django.shortcuts import render
from .models import User

# Create your views here.
def users(request):
    users = User.objects.order_by('first_name')
    user_dict = {"users":users}
    return render(request, './users_challenge.html', context=user_dict)

