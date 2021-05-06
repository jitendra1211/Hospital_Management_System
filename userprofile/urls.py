from django.urls import path
from .views import *

urlpatterns = [
    path('profile', user_profile, name="profile"),
    path('profile/create', create_user_profile, name="create_profile"),
    path('profile/<int:pk>', update_user_profile_pk, name="update_profile_pk"),
    path('profile/<int:pk>/delete', delete_user_profile_pk, name="delete_profile_pk"),
    path('doc_profile', doc_profile_view, name="doc_profile"),
    path('doc_profile/<int:pk>', doc_profile_pk, name="update_doc_profile_pk"),
    path('doc_profile/<int:pk>/delete', delete_doc_profile_pk, name="delete_doc_profile_pk"),
]
