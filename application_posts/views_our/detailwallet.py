from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
import json
from django.template import loader
from application_posts.models import Wallettest

class DetailWallet(View):
    def get(self, request, _id):
        wallet = Wallettest.objects.get(id=_id)
        template = loader.get_template("wallets/wallet_detail.html")
        context = {
            "wallet": wallet,
        }
        return HttpResponse(template.render(context, request))

