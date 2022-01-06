from django.db import models
from django.contrib.auth.models import User
 

class Post(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    firstname = models.CharField(max_length=100, default='chisom')
    lastname = models.CharField(max_length=100, default='chima')
    # arts = models.BooleanField('arts', default=False)
    # science = models.BooleanField('science', default=False)
    # IT = models.BooleanField('IT', default=False)
    # commercial = models.BooleanField('commercial', default=False)
    # female = models.BooleanField('female', default=False)
    # male = models.BooleanField('male', default=False)
    # birthdate = models.DateField(blank=True, null=True)
    # christianity = models.BooleanField('christianity', default=False)
    # muslim = models.BooleanField('muslim', default=False)
    # other = models.BooleanField('other', default=False)
    # AB = models.BooleanField('AB', default=False)
    # AD = models.BooleanField('AD', default=False)
    # AI = models.BooleanField('AI', default=False)
    # AN = models.BooleanField('AN', default=False)
    # BA = models.BooleanField('BA', default=False)
    # BY = models.BooleanField('BY', default=False)
    # BN = models.BooleanField('BN', default=False)
    # BR = models.BooleanField('BR', default=False)
    # CR = models.BooleanField('CR', default=False)
    # DL = models.BooleanField('DL', default=False)
    # EB = models.BooleanField('EB', default=False)
    # ED = models.BooleanField('ED', default=False)
    # EK = models.BooleanField('EK', default=False)
    # EN = models.BooleanField('EN', default=False)
    # GM = models.BooleanField('GM', default=False)
    # IM = models.BooleanField('IM', default=False)
    # JI = models.BooleanField('JI', default=False)
    # KA = models.BooleanField('KA', default=False)
    # KN = models.BooleanField('KN', default=False)
    # KS = models.BooleanField('KS', default=False)
    # KB = models.BooleanField('KB', default=False)
    # KG = models.BooleanField('KG', default=False)
    # KW = models.BooleanField('KW', default=False)
    # LA = models.BooleanField('LA', default=False)
    # NA = models.BooleanField('NA', default=False)
    # NI = models.BooleanField('NI', default=False)
    # OG = models.BooleanField('OG', default=False)
    # ON = models.BooleanField('ON', default=False)
    # OS = models.BooleanField('OS', default=False)
    # OY = models.BooleanField('OY', default=False)
    # PT = models.BooleanField('PT', default=False)
    # RV = models.BooleanField('RV', default=False)
    # ST = models.BooleanField('ST', default=False)
    # TB = models.BooleanField('TB', default=False)
    # YB = models.BooleanField('YB', default=False)
    # ZF = models.BooleanField('ZF', default=False)
    # FC = models.BooleanField('FC', default=False)
    # loudchewing = models.BooleanField('loudchewing', default=False)
    # beinglate = models.BooleanField('beinglate', default=False)
    # talkingduringamovie = models.BooleanField('talkingduringamovie', default=False)
    # talkingwhenyourmouthisfull = models.BooleanField('talkingwhenyourmouthisfull', default=False)
    # leavingthewaterrunning = models.BooleanField('leavingthewaterrunning', default=False)
    # smoking = models.BooleanField('smoking', default=False)
    # leavingdirtydishesinthesink = models.BooleanField('leavingdirtydishesinthesink', default=False)
    # sneezingwithoutcoveringyourmouth = models.BooleanField('sneezingwithoutcoveringyourmouth', default=False)
    # littering = models.BooleanField('littering', default=False)
    # bitingnails = models.BooleanField('bitingnails', default=False)
    # snoring = models.BooleanField('snoring', default=False)
    # leavingthetoiletseatup = models.BooleanField('leavingthetoiletseatup', default=False)


    def __str__(self):
        return self.username.username


from django.db.models.signals import post_save

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        Post.objects.create(username=instance)

post_save.connect(post_user_created_signal, sender=User)
