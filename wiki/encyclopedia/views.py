from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

from . import util


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    page_text = forms.CharField(label="Page text")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def add_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = "# " + title + "\n" + form.cleaned_data["page_text"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, "encyclopedia/add_page.html", {
                "form": NewPageForm()})
    return render(request, "encyclopedia/add_page.html", {
        "form": NewPageForm()
    })


def random_page(request):
    return render(request, "encyclopedia/random_page.html")


def get_page(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/get_page.html", {
        "content": content,
    })
