from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    username = serializers.SlugRelatedField(slug_field='username', required=True, queryset=User.objects.all())
    class Meta:
        # fields = ('id', 'username', 'arts', 'science', 'IT', 'commercial', 'female', 'male', 'birthdate', 'christianity', 'muslim', 'other', 'AB', 'AD','AI','AN','BA','BY','BN','BR','CR','DL','EB','ED','EK','EN','GM','IM','JI','KA','KN','KS','KB','KG','KW','LA', 'NA','NI','OG','ON','OS','OY','PT','RV','ST','TB','YB','ZF','FC', 'loudchewing', 'beinglate', 'talkingduringamovie', 'talkingwhenyourmouthisfull', 'leavingthewaterrunning', 'smoking', 'leavingdirtydishesinthesink', 'sneezingwithoutcoveringyourmouth', 'littering', 'bitingnails', 'snoring', 'leavingthetoiletseatup')
        fields = ('id', 'username', 'firstname', 'lastname')
        model = Post 