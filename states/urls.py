from django.urls import path
from .views import *
from django.conf.urls import url
app_name = 'states'

urlpatterns = [



    url(
        r'^assign/newstate/student/change/pwjhfskjdfhkhkd/(?P<id>[0-9]+)/(?P<s>[0-9]+)/$', assignstate,  name='assign'),
    url(r'^learn/state/$', showcontent,  name='show-content'),
    url(r'^problem/sdfd232323sfi3232e232423244nhc234udhd2323e4fuhdsufn2342ed/$',
        problem,  name='problem'),

    url(r'^illustrations/$', show_illustrations,  name='illustrations'),
    url(r'^questions/$', show_questions,  name='questions'),
    url(r'^student/redirect/correctly/state/learn/$',
        active_part_redirect,  name='active'),

    url(r'^report/this/state/$', report,  name='report'),



    url(r'^details/chapter/$', change_chapter,  name='details-chapter'),
    url(r'^switch/udfhsdufihsdfhksifu/sdfsdfjhksdjfh/chapter/(?P<id>[0-9]+)/(?P<s>[0-9]+)$',
        switch_chapter,  name='switch-chapter'),
    url(r'^go/$', dashboard,  name='dashboard'),

    url(r'^previous/$', previous_content,  name='previous-content'),




]
