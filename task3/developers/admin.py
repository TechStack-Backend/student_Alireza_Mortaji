from django.contrib import admin
from .models import Developer, Skill

# Register your models here.


class Skill_inline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(Developer)
class DevelopersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age")
    inlines = [Skill_inline]
    list_filter = ("first_name", "last_name")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "developer")
    list_filter = ["developer"]


class Developer_Inline(admin.TabularInline):
    model = Developer
    extra = 0
