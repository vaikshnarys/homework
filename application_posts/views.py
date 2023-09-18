from django.http import HttpResponse, JsonResponse

NEW_POST = [
    {
        'title': 'First title',
        'text': 'Firsttext.'

    },
    {
        'title': 'Second title',
        'text': 'Second text.'
    },
    {
        'title': 'Third title',
        'text': 'Third text.'
    },
    {
        'title': 'Fourth title',
        'text': 'Fourth text.'
    }
]

def new_post(request):
    return JsonResponse(NEW_POST, safe = False)