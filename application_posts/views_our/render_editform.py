from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

from application_posts.models import Wallettest


class EditFormRender(View):
    def get(self, request, _id):
        wallet = Wallettest.objects.get(id=_id)
        form_created = render(request, 'wallets/wallet_update_form.html', {'wallet': wallet})
        return HttpResponse(form_created)