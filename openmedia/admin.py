from django.contrib import admin
from .models import SearchHistory

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'timestamp')
    search_fields = ('user__username', 'query')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
