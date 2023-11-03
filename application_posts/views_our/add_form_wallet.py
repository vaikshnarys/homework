from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from application_posts.forms import AddWalletForm
from application_posts.models import Wallettest


class AddPageFormWallet(View):
    def get(self, request):
        form = AddWalletForm()
        render_template = render(request, 'wallets/add_page_form.html', {'form': form, 'title': 'Add post'})
        return HttpResponse(render_template)

    def post(self, request):
        form = AddWalletForm(request.POST)
        if form.is_valid():
            try:
                Wallettest.objects.create(**form.cleaned_data)
                return redirect('/wallets/')
            except:
                form.add_error(None,'Error add wallet')


        render_template = render(request, 'wallets/add_page_form.html', {'form': form, 'title': 'Add post'})
        return HttpResponse(render_template)