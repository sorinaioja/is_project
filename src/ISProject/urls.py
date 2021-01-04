from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from job.views import job_create_view, present_job_view, delete_jobs, user_job_view, job_application_view, search
from personal.views import (home_screen_view)
from account.views import register_view_Applicant,present_companies_view
from chat.views import (index)
from chat.views import (index)
from account import views

from django.contrib.auth import views as auth_views
from django.conf.urls import include

from personal.views import (
	home_screen_view
)

from question.views import (questions_view, question_create_view)
from quiz.views import (quiz_create_view,quiz_question_create_view,present_quizzes_view,take_quiz_view,finish_view)
from forum.views import add_in_forum, present_forum_view

from account.views import (
    register_view_Applicant,
    register_view_Company,
    register_view,
    login_view,
    logout_view,
    # company_view,
    userprofile_view,
    companyprofile_view,
    edit_user_profile_view,
    company_profile_update,
    user_profile_update,
    one_company_detail,
)


urlpatterns = [

    path('', home_screen_view, name='home'),
    path('', index, name='index'),

    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('login/', login_view, name="login"),  # TODO: ADD THIS LINE.
    path('logout/', logout_view, name="logout"),  # TODO: ADD THIS LINE.
    path('register/', register_view, name='register'),
    path('register_account/', register_view_Applicant, name='register_account'),
    path('register_company/', register_view_Company, name='register_company'),
    path('companies/',register_view_Applicant, name = 'companies'),
    path('compprofile/', companyprofile_view, name='compprofile'),
    path('userprofile/', userprofile_view, name='userprofile'),
    path('update_user', edit_user_profile_view, name='update_user'),
    path('user_update', user_profile_update, name='user_update'),
    path('company_profile/', companyprofile_view, name='compprofile'),
    path('company_update/', company_profile_update, name='update_company'),
    path('present_companies/', present_companies_view, name='companies'),
    path('job_detail/', job_create_view, name="job_detail"),
    path('job_application/<int:pk>', job_application_view, name='job_application'),
    path('question_create/', question_create_view, name='question_create'),
    path('job_presentation/', present_job_view, name='job_presentation'),
    path('job_presentation_user/', user_job_view, name='job_presentation_user'),
    path('job_delete/<int:pk>', delete_jobs, name='job_delete'),
    path('addInForum/', add_in_forum, name='add_in_forum'),
    path('viewDiscussions/', present_forum_view, name='present_forum_view'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),

    path('company/<int:pk>/', views.one_company_detail, name='company_detail'),
    path('questions/', questions_view, name='questions'),

    path('createQuiz/', quiz_create_view, name='createQuiz'),
    path('createQuiz/<int:pk>/createQuestion/', quiz_question_create_view, name='createQuestion'),
    path('viewQuizzez/',present_quizzes_view, name = 'tests'),
    path('quiz/<int:pk>/', take_quiz_view, name='quiz'),
    path('finish/<int:score>/<int:total>', finish_view, name='finish'),

    path('job_filter', search, name='job_filter'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
