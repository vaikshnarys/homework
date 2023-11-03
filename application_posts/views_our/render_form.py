from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class FormRender(View):
    def get(self, request):
        form_created = render(request, 'wallets/wallet_create_form.html')
        return HttpResponse(form_created)