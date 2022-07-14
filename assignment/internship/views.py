from django.shortcuts import render
from numpy import record
import requests
# Create your views here.


def homepageview(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def sports(request):
    records={}
    url='https://inshortsapi.vercel.app/news?category=sports'
    response=requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata']=inshorts_data
    return render(request,'sports.html',records)

def entertainment(request):
    records={}
    url='https://inshortsapi.vercel.app/news?category=entertainment'
    response=requests.get(url=url)
    inshorts_data = response.json()
    records['entertainmentdata']=inshorts_data
    return render(request,'entertainment.html',records)



def business(request):
    records={}
    url='https://inshortsapi.vercel.app/news?category=business'
    response=requests.get(url=url)
    inshorts_data = response.json()
    records['businessdata']=inshorts_data
    return render(request,'business.html',records)


def index(request):
    records={}
    url='https://inshortsapi.vercel.app/news?category='''
    response=requests.get(url=url)
    inshorts_data = response.json()
    records['indexdata']=inshorts_data
    return render(request,'bootstrap.html',records)
#records={"sportsdata":E}