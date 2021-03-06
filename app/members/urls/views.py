from django.urls import path

from .. import views
from .. apis import UserList

app_name = 'members'

urlpatterns = [
   path('', UserList.as_view()),
   path('login', views.login_view, name='login'),
   path('logout', views.logout_view, name='logout'),
   path('signup2', views.signup, name='signup2'),
   path('withdraw', views.withdraw, name='withdraw'),
]
