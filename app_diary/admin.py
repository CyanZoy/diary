from django.contrib import admin
from .models import Diary, Log, AdminDiary


admin.site.site_header = "日记管理"
admin.site.index_title = "站点管理"
admin.site.site_title = '管理'


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['user', 'header', 'text', 'images', 'date', 'date_time', 'order_num']
    search_fields = ('date', 'date_time')
    ordering = ('date', 'order_num')

    list_filter = ('date', 'user')

    fieldsets = (
        ('HeadLine', {'fields': (('header', ),)}),
        ('Content', {'fields': (('text', ), )}),
    )


@admin.register(AdminDiary)
class AdminDiaryAdmin(admin.ModelAdmin):
    list_display = ['header', 'texts', 'date', 'date_time', 'share']
    ordering = ('-date', )
    readonly_fields = ['header', 'text', 'date', 'date_time', 'identification_id']

    def texts(self, obj):
        if len(obj.text) > 10:
            return obj.text[:10]+'...'
        else:
            return obj.text
    texts.short_description = 'TEXT'


