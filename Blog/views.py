from django.shortcuts import render
from Blog.models import Blogs,USER_Data,Message
# Create your views here.
def home(request):
    latest_data =Blogs.objects.last()
    all_data =Blogs.objects.all()
    context ={
        "latest_data":latest_data,
        "all_data":all_data
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def serch_bar(request):
    # show data by serch bar catogery
    if request.method =="GET":
        serch_value =request.GET.get("serch")    
        all_data =Blogs.objects.all().filter(Blog_catogery=serch_value)
        context ={
            "Data":all_data
        }
        return render(request,'show_data.html',context)
def blog_page(request,serch_value):
    all_data =Blogs.objects.all().filter(Id=serch_value)
    context ={
        "Data":all_data
    }
    return render(request,'blog_page.html',context)

def show_data(request,serch_catogery):
    # show data by menu bar catogery
    all_data =Blogs.objects.all().filter(Blog_catogery=serch_catogery)
    context ={
        "Data":all_data
    }
    return render(request,'show_data.html',context)

def login(request):
    if request.method =='POST':
        username =request.POST.get("username")
        password =request.POST.get("password")
        login_data= USER_Data.objects.all().filter(Username=username,Password =password)
        for i in login_data:
            if (i.Username ==username and i.Password ==password): 
                return render (request,'index.html')   

    return render (request,'login.html')

def signup(request):
    if request.method =='POST':
        username =request.POST.get("username")
        email =request.POST.get("email")
        password =request.POST.get("password")
        remember =request.POST.get("remember-me")
        # if (remember =='on'):   
        user_data= USER_Data(Username= username,Email =email,Password =password)
        user_data.save()
        return render (request,'index.html')
    return render (request,'signup.html')

def contact(request):
    if request.method =='POST':
        firstname =request.POST.get("firstname")
        lastname =request.POST.get("lastname")
        Country =request.POST.get("country")
        message =request.POST.get("subject")
        message= Message(firstname= firstname,lastname=lastname,Country =Country,message=message)
        message.save()
        return render (request,'index.html')
    return render(request,'contact.html')            
