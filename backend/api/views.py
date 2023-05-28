# from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def serve_frontend(request):
    # return HttpResponse('The server has been reached!')
    return JsonResponse({
        'data': 'The server has been reached!'
    })