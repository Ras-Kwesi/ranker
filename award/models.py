from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=100, blank=True)
    profilepic = models.ImageField(upload_to='picture/',blank=True)
    contact = models.CharField(max_length=15,blank=True)

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username


    @classmethod
    def search_by_username(cls,search_query):
        profiles = cls.objects.filter(user__username__icontains=search_query)
        return profiles

    @classmethod
    def updateimage(cls, id):
        image = cls.objects.get(id=id)
        return image


class Project(models.Model):
    projectname = models.CharField(max_length=40)
    overview = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='picture/', blank=True)
    image2 = models.ImageField(upload_to='picture/', blank=True)
    image3 = models.ImageField(upload_to='picture/', blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)



    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_project(cls,id):
        project = cls.objects.get(id=id)
        return project

    @classmethod
    def getProjects(cls):
        project = cls.objects.all()
        return project

    @classmethod
    def image_comments(cls,id):
        comments = cls.objects.filter(imagecomments__comment_id=id)
        posters = cls.objects.filter(imagecomments__commnetator__id=id)
        return comments,posters


class Design(models.Model):
    designvote = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
     )
    design_voter = models.ForeignKey(User, on_delete=models.CASCADE)
    design_project = models.ForeignKey(Project,related_name='designvote')


class Usability(models.Model):
    usabilityvote = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
     )
    usability_voter = models.ForeignKey(User, on_delete=models.CASCADE)
    userbility_project = models.ForeignKey(Project, related_name='usabilityvote')

class Creativity(models.Model):
    creativityvote = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
     )
    creativity_voter = models.ForeignKey(User, on_delete=models.CASCADE)
    creativity_project = models.ForeignKey(Project, related_name='creativityvote')

class Content(models.Model):
    contentvote = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
     )
    content_voter = models.ForeignKey(User, on_delete=models.CASCADE)
    content_project = models.ForeignKey(Project, related_name='contentvote')