from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from . models import *

class BlogAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Blog
		fields = '__all__'

class BlogAdmin(admin.ModelAdmin):
	form = BlogAdminForm
	list_display = ('title', 'date_added', 'date_published', 'date_unpublished', 'published')
	list_filter = ('date_added', 'date_published', 'date_unpublished', 'published')
	list_editable = ('published',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)