import json
from django.http import JsonResponse
from django.views import View
from application_posts.models import Orm


class Update_delete_post(View):
    @staticmethod
    def parse_orm(orm: Orm):
        return {'id': orm.id, 'title': orm.title, 'content': orm.content, 'counter': orm.counter}

    def get(self, request, _id):
        post = Orm.objects.get(id=_id)
        return JsonResponse({'post' : self.parse_orm(post)})


    def put(self, request, _id):
        data = json.loads(request.body.decode('utf-8'))
        title = data.get('title', '')
        content = data.get('content', '')
        counter = data.get('counter', '')
        category = data.get('category', '')
        post, is_updated = Orm.objects.update_or_create(title=title, content=content, counter=counter,
                                                        category=category, defaults={'id': _id}, )
        return JsonResponse({'post' : self.parse_orm(post)})

    def delete(self , request, _id):
        post = Orm.objects.get(id=_id)
        post.delete()
        return JsonResponse({'delete_post': _id})