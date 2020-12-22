from django.urls import path
from account import views
from account.views import (
	account_view,
   register_view_Applicant,
  register_view_Company,

)

app_name = 'account'

urlpatterns = [
path('register_account/', register_view_Applicant, name='register_account'),
path('register_company/', register_view_Company, name='register_company'),
path('<user_id>/', account_view, name="view"),
    ]