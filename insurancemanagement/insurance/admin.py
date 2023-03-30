from django.contrib import admin

# Register your models here.
from .models import Category
admin.site.register(Category)

from .models import Policy
admin.site.register(Policy)

from .models import PolicyRecord
admin.site.register(PolicyRecord)

from .models import Question
admin.site.register(Question)
