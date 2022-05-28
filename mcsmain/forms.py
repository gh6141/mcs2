from django import forms

from mcsmain.models import Mcsmain


class McsmainForm(forms.ModelForm):
    class Meta:
        model = Mcsmain
        fields = ('title', 'naiyo', 'hitokoto')
