from django import forms
from .models import Post # import our Post model

# Creating a form for the Post model.

class PostForm(forms.ModelForm): # PostForm is a kind of ModelForm

    class Meta: # Tells Django what model to use to create this form
        model = Post # see import; this is a model we've created
        fields = ('title', 'text',)
