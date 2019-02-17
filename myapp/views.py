from django.shortcuts import render
from .forms import DownVoteForm




# Create your views here.

def downvote(request):
    form = DownVoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DownVoteForm()
    
    context = {
        'form': form
        
    }
    return render(request, "myapp/form_input.html", context)
