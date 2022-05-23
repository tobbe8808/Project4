from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Like
import requests
# Create your views here.

class home(ListView):
    model = Post
    template_name = 'index.html'

class Articledetails(DetailView):
    model = Post
    template_name = 'article_details.html'


def news1(request):
    return render(request, 'news1.html', {})


def news2(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=46f5af82baae677bfc2c20387c07fcb2&countries=gb&categories=general')  # noqa: E501
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
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('posts:post-list')

