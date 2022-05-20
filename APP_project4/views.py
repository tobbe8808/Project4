from django.shortcuts import render
from .models import Post, Like
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

def post_view(request):
    qs = Post.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user': user,
    }

    return render(request, 'app_project4/main.html', context)


def like_post(request):
    user = request.user
    if request.metod == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.linked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get-or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('post:post-list')



    return redirect('post:post-list')
