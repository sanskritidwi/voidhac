from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm
from .models import User, Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # form = UserAdminChangeForm
    # Will override default password checks (like password too common)
    # and validations with those specified in this form.
    # Also 'desig' field won't work without this.
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name','phone', 'auth')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ('user_permissions', 'groups')
    list_filter = ('name','phone', 'auth', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','phone')}),
        ('Permissions', {'fields': ('is_active', 'auth', 'is_staff', 'is_superuser')}),
        ('Permissions and Groups', {'fields': ('user_permissions', 'groups')}),
        ('Others', {'fields': ('date_joined', 'last_login')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'phone')}
        ),
    )

    ordering = ('email',)

admin.site.register(Profile)