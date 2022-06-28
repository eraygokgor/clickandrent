from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('register', views.register_user, name='register'),
    path('profile', views.signin, name='signin'),
    path('session', views.session, name='session'),
    path('existing', views.existing, name='existing'),
    path('logout', views.logout, name='logout'),
    path('profile/settings', views.settings, name='settings'),
    path('changes', views.changes, name='changes'),
    path('delete', views.delete, name='delete'),
    path('profile/ads', views.ads, name='ads'),
    path('profile/add', views.add, name='add'),
    path('adverts/<objectid>', views.adverts, name="adverts"),
    path('deletead', views.deletead, name="deletead"),
    path('search', views.search, name="search"),
    
]
