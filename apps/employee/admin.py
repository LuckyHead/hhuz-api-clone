from django.contrib.admin import *

from .models import (
    EmployeeSkill,
    Employee
)
@register(EmployeeSkill)
class EmployeeSkillAdmin(ModelAdmin):
    list_display=('id','name')
    list_display_links=('id', 'name')
    ordering=('name',)

@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display=('id', 'fullname', 'email')
    list_display_links=('id', 'fullname', 'email')
    ordering=('fullname',)