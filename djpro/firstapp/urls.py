from django.urls import path,include

from firstapp import views

app_name = 'firstapp'
 
urlpatterns = [
    path('', views.index, name = 'index'),
    # path('notblank/', views.index2, name = 'index'),
    # path('next/', views.index3, name = 'index'),
    path('formpage/', views.form_name_view, name = 'form_name_view'), 
    # path('formpage3/',views.form_name_viewe,name='form_name_viewe'),
    # path('formpage2/',views.form_name_viewer,name='form_name_viewer'),
    # path('formpage2/', views.form_name_view2, name = 'form_name_view2'),     
]
