import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

from . import util


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title:")
    page_text = forms.CharField(label="Page text:")


class SearchPageForm(forms.Form):
    search_title = forms.CharField(label="Search:")


def index(request):
    if request.method == "POST":
        form_search = SearchPageForm(request.POST)
        if form_search.is_valid():
            list_of_title = util.list_entries()
            title = form_search.cleaned_data["search_title"]
            if title in list_of_title:
                content = util.get_entry(title)
                return render(request, "encyclopedia/get_page.html", {
                    "content": content,
                    "form_search": SearchPageForm(),
                })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                "form_search": SearchPageForm()
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form_search": SearchPageForm()
    })


# def search_page(request):
#     if request.method == "POST":
#         form_search = SearchPageForm(request.POST)
#         print(form_search)
#         if form_search.is_valid():
#             list_of_title = util.list_entries()
#             print(list_of_title)
#             print(form_search.cleaned_data["search_title"])
#             title = form_search.cleaned_data["search_title"]
#             if title in list_of_title:
#                 return HttpResponseRedirect(reverse("encyclopedia/get_page.html"), args=title)
#         else:
#             return render(request, "encyclopedia/index.html", {
#                 "form_search": SearchPageForm()
#             })
#     return render(request, "encyclopedia/index.html", {
#         "form_search": SearchPageForm()
#     })

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
                "form": NewPageForm(),
                "form_search": SearchPageForm(),})
    return render(request, "encyclopedia/add_page.html", {
        "form": NewPageForm(),
        "form_search": SearchPageForm(),
    })


def random_page(request):
    list_of_page = util.list_entries()
    page = random.choice(list_of_page)
    content = util.get_entry(page)
    return render(request, "encyclopedia/random_page.html", {
        "content": content,
        "form_search": SearchPageForm(),
    })


def get_page(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/get_page.html", {
        "content": content,
        "form_search": SearchPageForm(),
    })






