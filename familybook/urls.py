from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('json/', views.json_func, name='json'),
    path('', views.index, name='index'),
    path('home/', views.EntryListView.as_view(), name='entry-list'),
    path('home/detail/<int:id>/', views.entry_detail_view, name='entry-detail'),
    path('home/create/', views.EntryCreateView.as_view(), name='entry-create'),
    path('home/update/<int:pk>/', views.EntryUpdateView.as_view(), name='entry-update'),
    path('accounts/profile/', views.profile_detail_view, name='profile-detail'),
    path('accounts/profile/create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('accounts/profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('accounts/register', views.register, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
