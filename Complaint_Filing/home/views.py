from django.http import HttpResponse
from django.shortcuts import render
from . import abcd
from . import sentiment
from home.models import Product

# def index(request):
#     return HttpResponse('<H1> Hello </H1> <a href = "https://www.facebook.com/"> Facebook </a>')
# def about(request):
#     return HttpResponse("About me checking the page")

# def read(request):
#     d1 = open("1.txt", 'r')
#     data = d1.read()
#     d1.close()
#     return HttpResponse(data)


def index(request):
    query1="scam fraud misleading online"
    query2="scam shopping product"
    query3="online fraud transaction"
    query4="services fake bad"
    query5 = "experience poor support"
    lists=abcd.fun(query1)
    params = {"data" : lists}
    # for i in lists:
        # print(i[0])
        # print(i[1])
        # print()
    return render(request, 'home.html', params)

def priority(request):
    query1="scam fraud misleading online"
    lists=abcd.fun(query1)
    score = []
    for i in range(len(lists)):
        lists[i].append(sentiment.fun([lists[i][1]]))
    lists.sort(key=lambda x: x[2])
    params = {"data" : lists}
    return render(request, 'Priority.html', params)

def complaint(request):
    return render(request, 'complaint.html')

def contact(request):
    return render(request, 'contact.html')

def submit_complaint(request):
    if request.method=="POST":
        product_name=request.POST.get('product_name')
        email=request.POST.get('email')
        product_availed=request.POST.get('product_availed')
        service_provider=request.POST.get('service_provider')
        desc=request.POST.get('desc')
  
        z=Product(product_name=product_name,email=email,product_availed=product_availed,service_provider=service_provider,desc=desc)
        z.save()

    return render(request,'home.html')