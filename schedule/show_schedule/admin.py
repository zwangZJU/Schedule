# coding = utf-8
from django.contrib import admin

# Register your models here.
from .models import Week, Plan

# add four plans when create a new Week object
class PlanInfo(admin.TabularInline):# anothor style : admin.StackedInline
    model = Plan
    extra = 4

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    inlines = [PlanInfo]
    # List page properties
    list_display = ['id', 'number', 'start_date', 'end_date']
    list_filter = []
    search_fields = ['number']
    list_per_page = 6

    # Add, modify page properties
    # fields = []
    # fieldsets = []


# admin.site.register(Week, WeekAdmin)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):

    list_display = ['id', 'member_name', 'work_content', 'week', 'is_achievement']
    list_per_page = 16
    # 1actions_on_top = False


# admin.site.register(Plan, PlanAdmin)


