from django.contrib import admin

# Register your models here.
# ここにmodelsのtaskを登録する！
from.models import Task

admin.site.register(Task)