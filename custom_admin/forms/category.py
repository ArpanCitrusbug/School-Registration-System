from django import forms
from ..models import Category

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        return super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(CategoryCreationForm,self).clean()
        # print(cleaned_data)
        title = cleaned_data.get('name')


    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(CategoryUpdateForm,self).clean()
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance