from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
menu = ['About','Add post','Return','Input']
from application_posts.models import Post
from django.views.decorators.csrf import csrf_exempt

def index(request):
    posts = Post.objects.all()
    return render(request,'application_post/index.html',{'posts': posts,'menu':menu,'title' : 'Mean page news'})
def about(request):
    return render(request,'application_post/about.html',{'menu':menu,'title' : 'Mean page about website news'})
NEW_POST = [
    {
        'title': 'First title',
        'text': 'Firsttext.'

    },
    {
        'title': 'Second title',
        'text': 'Second text.'
    },
    {
        'title': 'Third title',
        'text': 'Third text.'
    },
    {
        'title': 'Fourth title',
        'text': 'Fourth text.'
    }
]

def new_post(request):
    return JsonResponse(NEW_POST, safe = False)

@csrf_exempt
def create_new_post(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    post = Post(title = title,content = content)
    post.save()
    return HttpResponse(f"<h2>title: {title}  content {content}</h2>")

def get_one_post(request,post_id):
    post = Post.objects.get(id = post_id)
    return HttpResponse(f"<h2>'id':{post.id} , title:{post.title}, content {post.content}</h2>")

def posts(request):
    list_posts = []
    all_posts = Post.objects.all()
    for post in all_posts:
        list_posts.append([post.id, post.title, post.content])
    return JsonResponse({'all_posts': list_posts})