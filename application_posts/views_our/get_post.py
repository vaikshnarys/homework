from django.views import View
from django.http import JsonResponse, HttpResponse
from application_posts.models import Post


class Get_post(View):
    def get(self, request, *args, **kwargs):
        list_posts = []
        all_posts = Post.objects.all()
        for post in all_posts:
            list_posts.append([post.id, post.title, post.content])
        return JsonResponse({'all_posts': list_posts})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title = title, content = content)
        post.save()
        return HttpResponse(f"title: {title} , content {content}")