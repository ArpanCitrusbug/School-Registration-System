from gettext import install
from ..models import Profile
from django import forms

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # user = forms.CharField(read_only=True)
        model = Profile

        fields = "__all__"

    def  clean(self):
        print(self.instance)

    def save(self,commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance