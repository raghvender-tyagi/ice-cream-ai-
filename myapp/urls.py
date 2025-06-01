from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('learndynamic/', views.learndynamic, name='learndynamic'),
    path('about/',views.About,name='About'),
    path('Login/',views.Login,name='Login'),
     path('loogin/', views.Login, name='login'),
      path('signup/', views.signup, name='signup'),
      path('AI/', views.AI, name='AI')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)