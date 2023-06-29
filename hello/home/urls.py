from django.contrib import admin
from django.urls import path ,include
from home import views
urlpatterns =[

    path("", views.welcome, name="welcome"),
    path("welcome",views.welcome,name='welcome'),
    path("submit",views.submit,name='submit'),
    path("reel",views.reel,name='reel'),
    path("inventory",views.inventory,name='inventory'),
    path("use",views.use,name='use'),
    path("waste",views.waste,name='waste'),
    path("delete",views.delete,name='delete'),
    path("report",views.report,name='report'),
    path("report_all",views.report_all,name='report_all'),
    path("report_gsm",views.report_gsm,name='report_gsm'),
    path("undo",views.undo,name='undo'),
    path("edit",views.edit,name='edit'),
   
]