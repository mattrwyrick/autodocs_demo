from django.shortcuts import render
from advanced_views.JSON2Word import json2word_view
from advanced_views.CSV2Word import csv2word_view
from advanced_views.TSV2Word import tsv2word_view
from advanced_views.JSON2PDF import json2pdf_view
from advanced_views.auth_views import login, logout


def index(request):
    response = render(request, "index.html")
    return response
