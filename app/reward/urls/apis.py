from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.RewardList.as_view()),

]
