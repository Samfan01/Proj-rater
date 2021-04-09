from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name = 'home'),
    path('new_project/',views.new_project,name = 'new_project'),
    path('search/',views.search_project, name = 'search_project'),
    path('profile',views.profile,name = 'profile'),
    path('update_profile',views.update_profile,name = 'update_profile'),
    path('rate/<int:project_id>/',views.rate,name='rate_project')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)