from django.http import JsonResponse
from django.views import View
from application_posts.models import Wallet
from django.db import transaction
class Transaction(View):
    @transaction.atomic
    def post(self, request):
        p_wallet = request.POST.get('p_wallet')
        b_wallet = request.POST.get('b_wallet')
        wallets_1 = Wallet(privat_wallet = int(p_wallet) + 100)
        wallets_2 = Wallet(business_wallet = int(b_wallet) - 100)
        wallets_1.save()
        wallets_2.save()
        return JsonResponse({'transaction' : 'successful' ,'p_wallet' : wallets_1.privat_wallet ,'b_wallet': wallets_2.business_wallet })
