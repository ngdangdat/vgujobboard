from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from user.models import Profile

USERNAME_FIELD = get_user_model().USERNAME_FIELD

REQUIRED_FIELDS = (USERNAME_FIELD, ) + tuple(get_user_model().REQUIRED_FIELDS)

BASE_FIELDS = (_('Basic Information'), {
  'fields': REQUIRED_FIELDS + ('first_name', 'last_name', 'password', 'is_active')
})

PERMISSION_FIELDS = (_('Permission Fields'), {
  'fields': ('is_staff', 'is_superuser', 'groups')
})

DATE_FIELDS = (_('Important Dates'), {
  'fields': ('last_login', 'date_joined')
})

PROFILE_FIELDS = (_('Profile'), {
  'fields': (
      'birthday', 'phone_number', 'gender', 'city', 'country',
      'organization', 'title', 'status', 'avatar',
  )
})

class UserProfileInline(admin.StackedInline):
  model = Profile
  verbose_name_plural = 'Profile'
  max_num = 1
  can_delete = False

  def get_fieldsets(self, request, obj=None):
    return PROFILE_FIELDS,

class UserAdmin(DjangoUserAdmin):
  inlines = [UserProfileInline]
  list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('id', )
  fieldsets = (
    BASE_FIELDS,
    PERMISSION_FIELDS,
    DATE_FIELDS,
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'password1', 'password2'),
      }),
  )

