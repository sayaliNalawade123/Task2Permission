from rest_framework import serializers
from.models import PostModel




class PostSerializers(serializers.ModelSerializer):
    name=serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'


    def create(self,validated_data):
        User =  self.context.get
        validated_data.update({'name':str(User)})
        return PostModel.objects.create(**validated_data)


    def update(self, instance, validated_data):
        isinstance.name  = validated_data.get('name',instance.name)
        isinstance.address  = validated_data.get('address',instance.address)
        isinstance.subject = validated_data.get('subject',instance.subject)
        return instance