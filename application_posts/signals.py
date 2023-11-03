from django.dispatch import receiver
from django.db.models.signals import post_save
from application_posts.models import Orm


@receiver(post_save,sender = Orm)
def post_save_user(sender,instance,**kwargs):
    if Orm.objects.filter(category = instance.category).count() <= CATEGORY.get(instance.category,DEFAULT['default']):
        print("User created")
    else:
        if Orm.objects.filter(category = instance.category).order_by('time_crete').first().delete():
            print("User deleted")


CATEGORY = {
    'actors' : 8,
    'singers' : 5
}
DEFAULT ={
    'default' : 1
}