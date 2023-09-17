from django.contrib import admin
from .models import Post
from .models import Question, Choice

# Register your models here.
admin.site.register(Post)

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"
 
 
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
 
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]
 
 
admin.site.register(Question, QuestionAdmin)