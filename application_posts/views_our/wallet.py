from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
from django.template import loader
from django.views import View
from django.shortcuts import render, get_object_or_404
import json
from application_posts.models import Wallettest


class Walletview(View):
    def post(self, request):
        name = request.POST.get('name')
        currency = request.POST.get('currency')
        balance = request.POST.get('balance')

        if not name or not currency:
            return HttpResponseBadRequest('Name or Currency is empty')

        wallet = Wallettest(name = name, currency = currency , balance = balance)
        wallet.save()
        return JsonResponse({'name': wallet.name, 'currency': wallet.currency, 'balance': wallet.balance})
    def get(self,request):
        wallets = Wallettest.objects.all()
        render_template = render(request, 'wallets/wallet_jinja.html', {'wallets': wallets})
        return HttpResponse(render_template)