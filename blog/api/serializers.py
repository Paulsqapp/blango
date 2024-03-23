from rest_framework import serializers
from blog.models import Post, Tag
from blango_auth.models import User

from versatileimagefield.serializers import VersatileImageFieldSerializer


#PostDetailSerializer, is missing
class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="value", many=True, queryset=Tag.objects.all()
    )

    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(), view_name="api_user_detail", lookup_field="email"
    )
    
    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
        ],
        read_only=True,
    )
    
    class Meta:
        model = Post
        #fields = "__all__"
        exclude = ["ppoi"]
        readonly = ["modified_at", "created_at"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"