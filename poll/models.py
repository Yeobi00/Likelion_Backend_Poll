from django.db import models

class Poll(models.Model):
    title = models.CharField(blank=False, max_length=255)
    description = models.TextField(max_length=255)
    agree = models.PositiveIntegerField(default=0)
    disagree = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def get_agreeRate(self):
        total = self.agree + self.disagree
        if total == 0:
            return 0
        return self.agree / total
    
    def get_disagreeRate(self):
        total = self.agree + self.disagree
        if total == 0:
            return 0
        return self.disagree / total

    def __str__(self):
        return self.title