from django.conf.urls import include, url
from rest_framework import routers

from quiz import views
from quiz.views import QuizQuestionViewset, QuizViewset, QuestionViewset


router = routers.DefaultRouter()
router.register(r'question',QuestionViewset)
router.register(r'quiz',QuizViewset)

urlpatterns = [
    url(r'^api/',include(router.urls)),
    url(r'^$',views.welcome,name="welcome"),
    url(r'^create/',views.create_user,name="create_user"),
    url(r'^validate_login/',views.log_in,name="log_user"),
    url(r'^test',views.get_data,name="getdata"),
    url(r'^logout',views.log_out,name="log_out"),
]