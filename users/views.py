from django.shortcuts import render
from django.contrib import messages
from .models import User


def csv_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = User.objects.all()
