from django.shortcuts import render

def sample(request):
    print(request)
    if request.method=='GET':
        print(type(request.GET))
        user=request.GET.get('username')
        pass1=request.GET.get('password')
        email=request.GET.get('email')
        phone=request.GET.get('phone')
        print(user,pass1,email,phone)
    return render(request,'sample.html')

def register(request):
    print(request)
    if request.method=='POST':
        print(type(request.POST))
        print(request.POST)
        user=request.POST['username'] #  user=request.POST.get('username')
        pass1=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        print(user,pass1,email,phone)
    return render(request,'register.html')

