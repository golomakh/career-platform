from django.contrib import admin

# Register models here.

from django.contrib import admin
from .models import UserProfile, Topic, TestResult, LearningPlan, Recommendation

admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(TestResult)
admin.site.register(LearningPlan)
admin.site.register(Recommendation)

