from django.urls import path

from account.views import (
	account_view,
)

app_name = 'account'

urlpatterns = [
path('register_account/', views.register_view_Applicant, name='register_account'),
path('register_company/', viewa.register_view_Company, name='register_company'),
path('<user_id>/', account_view, name="view"),
    ]