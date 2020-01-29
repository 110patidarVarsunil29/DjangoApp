from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Everyone!!, This is a Django framework!!")
