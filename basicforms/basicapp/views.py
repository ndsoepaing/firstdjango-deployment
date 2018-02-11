from django.shortcuts import render
from basicapp.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def Users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('error from invalid')

    return render(request,'basicapp/form_Page.html',{'form':form})
