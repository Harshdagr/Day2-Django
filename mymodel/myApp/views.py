from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def start(request):
    return HttpResponse("Hello world")

def create_data(request):
    if request.method=='POST':
        form = Post_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
 
            # d = form.cleaned_data
            # print(d)
            # t = d['title']
            # m = d['message']
            # p = Post(title=t,text=m)
            # p.save()
            return redirect('index')

    else:
        form = Post_form()
    return render(request,'home.html',{'form':form})
 

def del_record(request,d):
    d= Post.objects.get(id=d)
    d=d.delete()
    return redirect('index')


# def index(request):
    # create data
    # Post.object.create(title='Ml',text='about making predections')


    # Post.object.create(title='pyhton',text='multipurpose lang')  
    #or
    # p=Post(title='Ml',text='about making predections')
    # p.save()

    #filter records:
    # data=Post.object.filter(title='django')

    # data=Post.objects.filter(title__contains='javascript')
 
    #fetch single record:
    # s = Post.objects.get(title="ML")
    # s = Post.object.get(id=2)

    #fetch:
    # data = Post.obq = Post.object.get(id=3)
    # q.title='DS'
    # q.save()create_datjects.all()
    # return render(request,'index.html',{'d':data})

    #update record :
    #for single
    # q = Post.object.get(id=3)
    # q.title='reate_data' is not defined

    # q.save()

    #for multiple
    # Post.object.filter(title='sample title').update(text='new value')

    #delete:
    #d = Post.object.get(id=1)
    #d.delete()

    #ordering objects :
    # data =Post.object.all().order_by('id')  -->for ascending
    # data =Post.object.all().order_by('-id')  --> for descending




def index(request):
    data = Post.objects.all()
    return render(request,'index.html',{'d':data})
 
