from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'Ras_Kwesi', email = 'ras@ras.com', password = 'passwadd')
        self.ras = Profile(bio = 'A python Programmer',contact = '054234444', user = self.user)

    def tearDown(self):
        self.user.delete()
        self.ras.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ras,Profile))
        self.assertTrue(isinstance(self.user,User))

    def test_save(self):
        self.ras.create_user_profile()
        self.ras.save_user_profile(self.user)
        users = Profile.objects.all()
        self.assertTrue(len(users)>0)


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.gram = Project(projectname = 'igclone', overview = 'A clone of Instagram',
                            profile = self.user, url='westalk.com')

    def tearDown(self):
        self.user.delete()
        self.ras.delete()
        self.gram.delete()

    def test_save(self):
        self.gram.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 1)


class VoteTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.gram = Project(projectname='igclone', overview='A clone of Instagram',
                            profile=self.user, url='westalk.com')
        self.vetting = Vote(designvote =1, usabilityvote = 6, creativityvote = 7, contentvote = 8,)

    def tearDown(self):
        self.user.delete()
        self.ras.delete()
        self.gram.delete()
        self.vetting.delete()


    def test_save_vote(self):
        self.vetting.save_vote()
        votes = Vote.objects.all()
        self.assertTrue(len(votes) == 1)