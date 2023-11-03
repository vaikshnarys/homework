from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
from django.template import loader
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
import json

from application_posts.forms import Walletsform
from application_posts.models import Wallettest


class Walletsformview(View):
    def get(self, request):
        form = Walletsform()
        render_template = render(request, 'wallets/wallets_form_add.html', {'form': form, 'title': 'Add post'})
        return HttpResponse(render_template)

    def post(self, request):
        form = Walletsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/wallets/')

        render_template = render(request, 'wallets/wallets_form_add.html', {'form': form, 'title': 'Add post'})
        return HttpResponse(render_template)