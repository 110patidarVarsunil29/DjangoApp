from django.http import HttpResponse


def started(request):
    return HttpResponse("Hello Everyone!!, This is a Django framework!!")
