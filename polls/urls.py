from django.urls import path
from . import views

#app_name = 'employee_register'
app_name = 'polls'

urlpatterns = [
    # ex: /employee_register/
    # path('', views.index, name='index'),
    # ex: /employee_register/5/
    # path('<int:question_id>', views.detail, name='detail'),
    # ex: /employee_register/5/results/
    # path('<int:question_id>/results/',views.results, name='results'),
    # ex: /employee_register/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]