from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)        # Поле для имени
    text = models.TextField()                      # Поле для текста сообщения
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания

    def __str__(self):
        return f"{self.name}: {self.text[:20]}"
