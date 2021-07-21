from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sheet(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    charm = models.SmallIntegerField()
    cool = models.SmallIntegerField()
    sharp = models.SmallIntegerField()
    tough = models.SmallIntegerField()
    weird = models.SmallIntegerField()

    

    def __str__(self):
        return self.name

# class Topic(models.Model):
#     subject = models.CharField(max_length=255)
#     last_updated = models.DateTimeField(auto_now_add=True)
#     board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)   # related_name: reverse relationship, board has access to a list of topic instances that belong to it
#     starter = models.ForeignKey(User, related_name='topics', on_delete=models.PROTECT)

#     def __str__(self):
#         return self.subject

# class Post(models.Model):
#     message = models.TextField(max_length=4000)
#     topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(null=True)
#     created_by = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
#     updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.PROTECT)   # + means don't need reverse relationship
    
# python manage.py shell
# from boards.models import Board

# board = Board()
# board.save()
# Board.objects.create(name='...', description='...')
# Board.objects.all()
# Board.objects.get(id=1)
