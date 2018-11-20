from django.shortcuts import get_object_or_404, render

from .models import Folder, Bookmark

# Create your views here.
def index(request):
    folders = Folder.objects.all()
    context = { 'folders': folders }
    return render(request, 'bookmarks/index.html', context)

def contents(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    context = { 'folder': folder  }
    return render(request, 'bookmarks/contents.html', context)