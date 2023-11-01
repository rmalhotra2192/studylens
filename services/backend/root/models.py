from django.db import models
from django.utils.text import slugify

class Tags(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_name = models.CharField(max_length=128, null=True)
    tag_value = models.CharField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.tag_value:
            self.tag_value = slugify(self.tag_display)
        super(Tags, self).save(*args, **kwargs)