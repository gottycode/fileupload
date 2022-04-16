from rest_framework import serializers
from timestamp.models import TimestampRequest



class TimestampSerializer(serializers.Serializer):
    system_code  = serializers.IntegerField(required=False)
    file_id = serializers.IntegerField(required=False)
    pdf_file=serializers.CharField(required=False)
    status_cd = serializers.IntegerField(required=False)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # print(validated_data)

        return TimestampRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
