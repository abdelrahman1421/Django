from django.contrib import admin
from .models import Student, Track


# Register your models here.
class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Information', {'fields': ['fname', 'lname', 'age']}],
        # we have two panels so we should have two lists
        ['Scholarship Information', {'fields': ['student_track']}],
        # ['Student Exams',{'fields': ['student_exam']}]
    )
    list_display = ('fname', 'lname', 'age', 'student_track', 'graduate')
    list_filter = ['fname', 'age', 'student_track']
    search_fields = ['fname', 'age', 'student_track__name']
    # the main tuple of page


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 2


class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]


admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)
