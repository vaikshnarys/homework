import json
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views import View

from application_posts.models import Wallettest


class EditWalletView(View):

    def post(self, request, _id):
        wallet = Wallettest.objects.get(id=_id)
        name = request.POST.get('name')
        currency = request.POST.get('currency')
        balance = request.POST.get('balance')

        if not name or not currency or not balance:
            return HttpResponseBadRequest('Name or Currency is empty')

        wallet.name = name
        wallet.currency = currency
        wallet.balance = balance
        wallet.save()

        return JsonResponse({'name': wallet.name, 'currency': wallet.currency, 'balance': wallet.balance})