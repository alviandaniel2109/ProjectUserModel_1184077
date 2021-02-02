from django.shortcuts import render
#from django.http import HttpResponse
#from .models import User
from UserModel_1184077.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, './index.html')

def users(request):
	form =NewUserForm()

#jika user menekan tombol
	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR FORM INVALID")
	return render(request,'./users.html',{'form':form})