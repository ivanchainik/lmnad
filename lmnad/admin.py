from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.forms import ModelForm
from lmnad.models import *
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from django import forms
from django.contrib.admin import ModelAdmin
from suit_ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget
from mptt.admin import MPTTModelAdmin
from suit.admin import SortableModelAdmin

class TextFullEditForm(ModelForm):
    class Meta:
        widgets = {
            'message': CKEditorWidget(editor_options={'startupFocus': True}),
            'text': CKEditorWidget(editor_options={'startupFocus': True}),
            'short_text': CKEditorWidget(editor_options={'startupFocus': True})
        }


class TextEditForm(ModelForm):
    class Meta:
        widgets = {
            'text': RedactorWidget(editor_options={'lang': 'en'}),
            'abstract': RedactorWidget(editor_options={'lang': 'en'}),
            'science_index': RedactorWidget(editor_options={'lang': 'en'}),
            'elibrary': RedactorWidget(editor_options={'lang': 'en'})
        }


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = True
    form = TextEditForm
    verbose_name_plural = 'accounts'


class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ProtectionAdmin(ModelAdmin):
    list_display = ['author', 'title', 'message', 'date']
    form = TextFullEditForm

admin.site.register(Protection, ProtectionAdmin)


class PageAdmin(ModelAdmin):
    list_display = ['name', 'title', 'text']
    form = TextFullEditForm

admin.site.register(Page, PageAdmin)


class EventAdmin(ModelAdmin):
    list_display = ['title', 'text', 'date']
    form = TextEditForm

admin.site.register(Event, EventAdmin)

class SeminarAdmin(ModelAdmin):
    list_display = ['title', 'text', 'date']
    form = TextEditForm

admin.site.register(Seminar, SeminarAdmin)


class PeopleAdmin(SortableModelAdmin):
    list_display = ['fullname', 'degree', 'rank', 'position', 'order_by']
    search_fields = ['fullname']
    form = TextEditForm
    sortable = 'order_by'

admin.site.register(People, PeopleAdmin)


class ArticleAdmin(ModelAdmin):
    list_display = ['authors', 'title', 'source', 'year']
    search_fields = ['authors', 'title', 'year']
    form = TextEditForm

admin.site.register(Article, ArticleAdmin)


class GrantAdmin(ModelAdmin):
    list_display = ['type', 'number', 'name', 'head']
    search_fields = ['name', 'number', 'head']
    form = TextEditForm

admin.site.register(Grant, GrantAdmin)


class ProjectAdmin(ModelAdmin):
    list_display = ['title', 'short_text']
    form = TextFullEditForm

admin.site.register(Project, ProjectAdmin)