from django.urls import path
from .import views
from .auth import auth_middleware
urlpatterns = [
	path('',views.home,name="home"),
	path('predict',auth_middleware(views.predict),name="predict"),
	path('statistics',auth_middleware(views.statistics),name="statistics"),
	path('selectlabel',views.selectlabel,name="selectlabel"),
	path('average',auth_middleware(views.average),name="average"),
	path('selectaverage',views.selectaverage,name="selectaverage"),
	path('climat',auth_middleware(views.climat),name="climat"),
	path('above',views.above,name="above"),
	path('season',auth_middleware(views.season),name="season"),
    path('signup',views.signup, name="signup"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
]