from django import forms

class comment_form(forms.Form):
    name = forms.CharField(label="Name", max_length=64)
    body = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"Comment here!",
            "rows":4,
            "cols":30

        }
    ))