from django.shortcuts import render


def profiles(request):
    return render(request, 'user/index.html')