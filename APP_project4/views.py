from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=46f5af82baae677bfc2c20387c07fcb2&countries=gb&categories=technology')  # noqa: E501
    res = r.json()
    print(res)
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description, image, url)
    return render(request, 'APP_project4/index.html', {'news': news})


def news1(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=46f5af82baae677bfc2c20387c07fcb2&countries=gb&categories=sports')  # noqa: E501
    res = r.json()
    print(res)
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description, image, url)
    return render(request, 'APP_project4/news1.html', {'news': news})


def news2(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=46f5af82baae677bfc2c20387c07fcb2&countries=gb&categories=science')  # noqa: E501
    res = r.json()
    print(res)
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description, image, url)
    return render(request, 'APP_project4/news2.html', {'news': news})

