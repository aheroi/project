from django.contrib import admin
from myfinpages.models import Income, Outcome, Balance

# Register your models here.

# admin.site.register(Income)
# admin.site.register(Outcome)
# admin.site.register(Balance)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    search_fields = ('date', 'type', 'value', 'notes', 'created_at')

    list_display = ('pk', 'date', 'type', 'value', 'notes', 'created_at')
    list_display_links = ('pk', 'value', 'date', 'type', 'notes')
    list_filter = ('type', 'user', 'created_at')

    ordering = ('pk', 'value', 'date', 'type', 'notes', 'created_at')

    readonly_fields = ('created_at', 'updated_at')


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    search_fields = ('date', 'type', 'value', 'notes', 'created_at')

    list_display = ('pk', 'date', 'type', 'value', 'notes', 'created_at')
    list_display_links = ('pk', 'value', 'date', 'type', 'notes',)
    list_filter = ('type', 'user', 'created_at')

    ordering = ('pk', 'value', 'date', 'type', 'notes', 'created_at')

    readonly_fields = ('created_at', 'updated_at')


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    search_fields = ('date', 'type', 'value', 'notes', 'created_at')

    list_display = ('pk', 'date', 'type', 'value', 'notes', 'created_at')
    list_display_links = ('pk', 'value', 'date', 'type', 'notes', )
    list_filter = ('type', 'user', 'created_at')

    ordering = ('pk', 'value', 'date', 'type', 'notes', 'created_at')

    readonly_fields = ('created_at', 'updated_at')
