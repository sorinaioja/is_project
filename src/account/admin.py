
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .models import Company
from .models import Comment



class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff','is_applicant','is_company')
	search_fields = ('email','username',)
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()



admin.site.register(Account, AccountAdmin)
admin.site.register(Company)
admin.site.register(Comment)