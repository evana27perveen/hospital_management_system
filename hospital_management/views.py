from django.shortcuts import render


def account_home(request):
    return render(request, 'App_login/account_home.html')
