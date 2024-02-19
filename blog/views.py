from django.shortcuts import render
from .models import post
from .forms import comment_form

# Create your views here.

def index(request):
    return render(request, "blog/index.html",{
        "posts": post.objects.all()
    })

names = []
comments = []

def single(request, post_id):
    if request.method == "POST":
        form = comment_form(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            body = form.cleaned_data['body']

            names.append(name)
            comments.append(body)
    else:
        return render(request, "blog/single.html",{
        "posts": post.objects.get(pk=post_id),
        "form": comment_form()
    })

    name = names[-1]
    comment = comments[-1]
    return render(request, "blog/single.html",{
        "posts": post.objects.get(pk=post_id),
        "form": comment_form(),
        "names": name,
        "comments": comment
    })

