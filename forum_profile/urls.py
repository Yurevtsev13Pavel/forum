from django.urls import path, include

from forum_profile.views import ProfileCreateView

app_name = 'forum_profile'

urlpatterns =[
    path('profile/create/', ProfileCreateView.as_view(), name='create'),

]