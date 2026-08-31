from django.db import models


class Prompt(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="prompts/")
    prompt_text = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
