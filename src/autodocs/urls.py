from django.conf.urls import include, url
from django.contrib import admin
import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'$^', views.index, name="home"),
    url(r'^index/$', views.index, name="index"),

    url(r'^json2word/$', views.json2word_view, name="json2word"),
    url(r'^csv2word/$', views.csv2word_view, name="csv2word"),
    url(r'^tsv2word/$', views.tsv2word_view, name="tsv2word"),

    url(r'^json2pdf/$', views.json2pdf_view, name="json2pdf"),
]
