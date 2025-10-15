from django.contrib import admin
from django.contrib import messages
from django.template.defaultfilters import slugify

from .models import Equipment, Category


# Register your models here.

class PriceRangeFilter(admin.SimpleListFilter):
    title = "Диапазон цен"
    parameter_name = 'price_filter'

    def lookups(self, request, model_admin):
        return [
            ('1000000-5000000', '1_000_000 - 5_000_000 руб'),
            ('5000000+', 'Более 5_000_000 руб'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '1000000-5000000':
            return queryset.filter(price__range=(1000000, 5000000))
        if self.value() == '5000000+':
            return queryset.filter(price__gte=5000000)
        return queryset


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):

    fields = ['title', 'slug', 'content', 'cat', 'tags']
    # exclude = ['tags', 'is_published']
    prepopulated_fields = {"slug": ("title",)}

    filter_vertical = ['tags']

    list_display = ('id', 'title', 'time_create',
                    'is_published', 'price')
    list_display_links = ('id', 'title')
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draft']

    search_fields = ['title__startswith', 'cat__name']

    list_filter = [PriceRangeFilter, 'cat__name', 'is_published']

    @admin.display(description="Краткое описание")
    def brief_info(self, women: Equipment):
        return f"Описание {len(women.content)} символов."

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Equipment.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Equipment.Status.DRAFT)
        self.message_user(request, f"{count} записи(ей) сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
