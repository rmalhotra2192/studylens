from django.db import models
from django.utils.text import slugify
from backend import settings

class LearningGoals(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    goal_name = models.CharField(max_length=128, null=True)
    goal_value = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.goal_name

    def save(self, *args, **kwargs):
        if not self.goal_value:
            self.goal_value = slugify(self.goal_name)
        super(LearningGoals, self).save(*args, **kwargs)

class LearningTopics(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic_name = models.CharField(max_length=128, null=True)
    topic_value = models.CharField(max_length=128, null=True, blank=True)
    goal = models.ForeignKey(LearningGoals, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name

    def save(self, *args, **kwargs):
        if not self.topic_value:
            self.topic_value = slugify(self.topic_name)
        super(LearningTopics, self).save(*args, **kwargs)
    
class Tags(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_name = models.CharField(max_length=128, null=True)
    tag_value = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.tag_name

    def save(self, *args, **kwargs):
        if not self.tag_value:
            self.tag_value = slugify(self.tag_display)
        super(Tags, self).save(*args, **kwargs)