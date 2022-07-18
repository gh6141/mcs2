from django.conf import settings
from django.db import models


class Mcsmain(models.Model):
    title = models.CharField('タイトル', max_length=128)
    naiyo = models.TextField('内容', blank=True)
    hitokoto = models.TextField('ひとことメッセージ', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField('本文',blank=False)
    commented_at=models.DateTimeField('投稿日',auto_now_add=True)
    commented_to=models.ForeignKey(Mcsmain,verbose_name="メッセージ", 
                                    on_delete=models.CASCADE)
    commented_by=models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name="投稿者",
                                    on_delete=models.CASCADE)
                                    
    def __str__(self):
        return self.text

class DirectMessage(models.Model):
    created_at = models.DateTimeField("登録日時", auto_now_add=True)

    sender=models.ForeignKey(
        settings.AUTH_USER_MODEL,related_name='sender',
        on_delete=models.CASCADE
    )

    receiver=models.ForeignKey(
        settings.AUTH_USER_MODEL,related_name='receiver',
        on_delete=models.CASCADE
    )

    message=models.CharField(verbose_name="メッセージ",max_length=200)

    def __str__(self):
        return str(self.sender)+'--- send to --->'+str(self.receiver)
