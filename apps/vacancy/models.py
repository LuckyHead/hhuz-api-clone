from django.db.models import *

from apps.employer.models import Employer
from apps.employee.models import EmployeeSkill

class Vacancy(Model):
    company=OneToOneField(
        Employer,
        verbose_name='Company',
        on_delete=CASCADE
    )

    title=CharField(
        'Title of the vacancy',
        max_length=256
    )

    salary_from=PositiveIntegerField(
        'Salary starts from (USD)'
    )

    salary_to=PositiveIntegerField(
        'Salary ends in (USD)'
    )

    description=TextField(
        'Descrption of vacancy'
    )

    required_skills=ManyToManyField(
        EmployeeSkill,
        verbose_name='Required skills'
    )

    created_date=DateTimeField(
        auto_now_add=True,
        verbose_name='Vacancy publication date'
    )

    class Meta:
        verbose_name='Vacancy'
        verbose_name_plural='Vacancies'
