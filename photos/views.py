from django.shortcuts import render

def post_list(request):
    return render(request, 'photos/photos_list.html', {})

# Create your views here.
