from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        pass
    else:
        form=LoginForm()
        context={'form':form}
        return render(request,'accounts/index.html',context)