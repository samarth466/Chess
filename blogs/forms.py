from django import forms

# Create your forms here


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    publication_date = forms.DateTimeField()


class CommentForm(forms.Form):
    content = forms.CharField()
