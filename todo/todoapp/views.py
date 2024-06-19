from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import tododata
# Create your views here.
def home(request):
    abc=tododata.objects.all()
    return render(request,'todo.html',{'abc':abc})
   
def todo(request):
    if request.method=='POST':
        Name=request.POST['name']
        description=request.POST['description']
        todo=tododata(name=Name,description=description)
        todo.save()
        return redirect('/home')
        

def delete(request,id):
    delt=tododata.objects.get(id=id)
    delt.delete()
    return redirect('/home')

def edit(request,id):
    edit1=get_object_or_404(tododata,id=id)
    if request.method == 'POST':
        name=request.POST['name']
        description=request.POST['description']
        if name and description:
            return HttpResponse('fill')
        else:
            edit1.name=name
            edit1.description=description
            edit1.save()
            return redirect('/home')
    return render(request,'edit.html',{'edit1':edit1})