from django import forms

from mcsmain.models import Mcsmain,Comment


class McsmainForm(forms.ModelForm):
    class Meta:
        model = Mcsmain
        fields = ('title', 'naiyo', 'hitokoto')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
