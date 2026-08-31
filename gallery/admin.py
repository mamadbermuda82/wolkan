from django.contrib import admin
from django.utils.html import format_html
from .models import Prompt


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "views",
        "created_at",
        "delete_button",
    )

    search_fields = (
        "title",
        "prompt_text",
        "category",
    )

    list_filter = (
        "category",
    )

    readonly_fields = (
        "views",
        "image_preview",
    )

    fields = (
        "title",
        "image",
        "image_preview",
        "prompt_text",
        "category",
        "views",
    )

    @admin.display(description="Preview")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:300px; max-width:300px; border-radius:10px;" />',
                obj.image.url
            )
        return "No image"

    @admin.display(description="Actions")
    def delete_button(self, obj):
        from django.urls import reverse

        url = reverse(
            "admin:gallery_prompt_delete",
            args=[obj.pk]
        )

        return format_html(
            '<a href="{}" style="color:#dc3545;font-weight:bold;">'
            '🗑️ Delete'
            '</a>',
            url
        )