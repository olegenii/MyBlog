from datetime import datetime

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings

from web.models import Publication, Comment, Feedback

def index(request):
    return render(request, "index.html")

def contacts(request):
    if request.method == "GET":
        return render(request, "contacts.html",{"feedbacks": Feedback.objects.all()})
    else:
        name = request.POST["name"]
        email = request.POST["email"]
        text = request.POST["text"]

        if (len(name)==0) or (len(email)==0):
            return render(request, "contacts.html", {
                "error": "Error name or email"
            })
        if len(text)==0:
            return render(request, "contacts.html", {
                "error": "Error text"
            })
        Feedback(name=name, email=email, date=datetime.now(),text=text.replace("\n", "<br />")).save()
        return redirect("/contacts")


def publication(request,number):
    pubs = Publication.objects.filter(id=number)
    comments = Comment.objects.filter(publication_id=number)
    if len(pubs) == 1:
        pub = model_to_dict(pubs[0])
        if request.method == "GET":
            return render(request, "publication.html", {"comments": comments, "number": pub})
        else:
            name = request.POST["name"]
            email = request.POST["email"]
            text = request.POST["text"]
            if (len(name) == 0) or (len(email) == 0) or (len(text) == 0):
                return render(request, "publication.html", {
                    "error": "Error name or email or text",
                    "comments": comments,
                    "number": pub
                })
            else:
                Comment(publication_id=number, name=name, email=email, date=datetime.now(),text=text.replace("\n", "<br />")).save()
                return render(request, "publication.html", {"comments": comments, "number": pub})
    else:
        return redirect("/")


def publications(request):
    return render(request, "publications.html", {
        "publications": Publication.objects.all()
    })

def publish(request):
    if request.method == "GET":
        return render(request, "publish.html")
    else:
        secret = request.POST["secret"]
        name = request.POST["name"]
        text = request.POST["text"]

        if secret != settings.SECRET_KEY:
            return render(request, "publish.html", {
                "error": "Error secret key"
            })
        if len(name)==0:
            return render(request, "publish.html", {
                "error": "Error name"
            })
        if len(text)==0:
            return render(request, "publish.html", {
                "error": "Error text"
            })
        Publication(name=name, date=datetime.now(), text=text.replace("\n","<br />")).save()
        return redirect("/publications")


