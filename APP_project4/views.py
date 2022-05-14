from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=9736ce03a738243b550151174c7a437f&countries=gb')  # noqa: E501
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

