from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from personal.views import (home_screen_view)
from account.views import register_view_Applicant,present_companies_view
from chat.views import (index)
from chat.views import (index)

from django.contrib.auth import views as auth_views
from django.conf.urls import include

from personal.views import (
	home_screen_view
)

from account.views import (
    register_view_Applicant,
    register_view_Company,
    register_view,
    login_view,
    logout_view,
    # company_view,
    userprofile_view,
    companyprofile_view,
)

urlpatterns = [

    path('', home_screen_view, name='home'),
    path('', index, name='index'),
    #path('account/', include('account.urls', namespace='account')),
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
    path('present_companies/', present_companies_view, name='companies'),
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

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
