from django.forms import ModelForm
from .models import DownVote

class DownVoteForm(ModelForm):
    class Meta:
        model = DownVote
        fields = ['post_id', 'user_profile',]