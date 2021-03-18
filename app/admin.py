from django.contrib import admin
from . import models

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 1

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'file', 'pub_date')
    list_filter = ('text', 'file', 'pub_date')
    fieldsets = (
        ('Information:',{
            'fields':('text', 'file')
        }),
        ('Release:',{
            'fields':('pub_date',)
        }),
    )
    inlines = [ChoiceInline]

@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'vote')
    list_filter = ('text', 'question', 'vote')
    fieldsets = (
        ('Question Information:',{
            'fields':('question',)
        }),
        ('Choice Information:',{
            'fields':('text', 'vote')
        }),
    )

