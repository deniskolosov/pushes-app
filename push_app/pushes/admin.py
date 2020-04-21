from django.contrib import admin
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path

from .forms import PushForm
from .models import Push, Option


@admin.register(Push)
class PushAdmin(admin.ModelAdmin):

    search_fields = ["name"]
    exclude = ['send_at', 'times_sent', 'is_sent']
    form = PushForm

    change_form_template = 'admin/add_push.html'


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):

    fields = ["name"]






