import json

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
menu = ['About','Add post','Return','Input']
from application_posts.models import Orm, Post , Comment
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
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


def get_one_post(request,post_id):
    post = Post.objects.get(id = post_id)
    return HttpResponse(f"<h2>'id':{post.id} , title:{post.title}, content {post.content}</h2>")

def posts(request):
    list_posts = []
    all_posts = Post.objects.all()
    for post in all_posts:
        list_posts.append([post.id, post.title, post.content])
    return JsonResponse({'all_posts': list_posts})
def parse_Orm(orm:Orm):
    return {'id':orm.id , 'title':orm.title, 'content':orm.content , 'counter':orm.counter}

@csrf_exempt
def create_new_post(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    counter = request.POST.get('counter')
    post = Orm(title = title,content = content,counter = counter)
    post.save()
    return HttpResponse(f"<h2>title: {title}  content {content} counter {counter}</h2>")
def get_orm_posts(request, _id):
    post = get_object_or_404(Orm, id = _id)
    return HttpResponse(f"<h2>'id':{post.id} , title:{post.title}, content:{post.content} , counter:{post.counter}</h2>")


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def get_all_posts(request):
    result = []
    posts = Orm.objects.filter(counter__lte=4)
    for post in posts:
        #result.append([post.id, post.title, post.content, post.counter])
        result.append({'id': post.id, 'title': post.title, 'content' : post.content, 'counter' : post.counter})
    return JsonResponse(result, safe= False)

def check_is_exists(request,counter):
    result = Orm.objects.filter(counter=counter).exists()
    return JsonResponse({'is_exists:': result})
def get_orm_post_or_create(request,counter):
    post, is_created = Orm.objects.get_or_create(id = 7, title = 'seventh post', content = 'This is my seventh post', counter = 3)
    return JsonResponse({'created post' : post})

@csrf_exempt
def update_orm_post_or_create(request,_id):
    data = json.loads(request.body.decode('utf-8'))
    title = data.get('title','')
    content = data.get('content','')
    counter = data.get('counter','')
    category = data.get('category', '')
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # counter = request.POST.get('counter')
    post, is_updated = Orm.objects.update_or_create(title = title,content = content,counter = counter,category = category, defaults={'id' : _id},)
    return JsonResponse({'id':post.id,'title' : post.title,'content' : post.content,'counter' : post.counter,'category' : post.category})

def delete_orm_post(request,_id):
    delete_post = Orm.objects.filter(id = _id).delete()
    return JsonResponse({'delete post': _id})
@csrf_exempt
def create_comment(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    post = Post(title = title,content = content)
    post.save()

    comment_1 = Comment(text = 'First comment', new = post)
    comment_2 = Comment(text = 'Second comment', new = post)
    Comment.objects.bulk_create([comment_1,comment_2])
    return HttpResponse(f"title: {post.title} , content : {post.content} , comment_1 : {comment_1.text} , comment_2: {comment_2.text}")


def get_comments(request,post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()
    result = []
    for comment in comments:
        result.append({'id': comment.id, 'text' : comment.text})
    return JsonResponse(result, safe= False)

def change_status_all_new(request,post_id,status):
    comment = Comment.objects.filter(new_id = post_id).update(status = status)
    return JsonResponse(comment, safe=False)