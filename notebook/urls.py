from __future__ import unicode_literals

from django.conf.urls import *

urlpatterns = patterns('',

    # filebrowser urls
    url(r'^browse/$', 'notebook.views.browse', name="nb_browse"),
    url(r'^mkdir/', 'notebook.views.mkdir', name="nb_mkdir"),
    url(r'^upload/', 'notebook.views.upload', name="nb_upload"),
    url(r'^rename/$', 'notebook.views.rename', name="nb_rename"),
    url(r'^delete/$', 'notebook.views.delete', name="nb_delete"),
    url(r'^create/$', 'notebook.views.create', name="nb_create"),
    url(r'^edit/$', 'notebook.views.edit', name="nb_edit"),
    url(r'^check_file/$', 'notebook.views._check_file', name="nb_check"),
    url(r'^upload_file/$', 'notebook.views._upload_file', name="nb_do_upload"),
)
