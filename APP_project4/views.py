from django.shortcuts import render

# Create your views here.
def index(request):
    r = requests.get('https://api.mediastack.com/v1/news?
    access key = 
    res = r.json()
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
    return render(request, 'APP_project4/index.html', {'news':news} )

