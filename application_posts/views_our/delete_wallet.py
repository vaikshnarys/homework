from django.http import HttpResponse
from django.views import View

from application_posts.models import Wallettest


class DeleteWallet(View):
    def get(self, request, _id):
        wallet = Wallettest.objects.get(id=_id)
        wallet.delete()
        return HttpResponse('Wallet deleted')