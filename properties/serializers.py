from rest_framework import serializers
from .models import Property, Appointment


class PropertySerializer(serializers.ModelSerializer):
    agent_email = serializers.SerializerMethodField("get_agent_email")
    property_url = serializers.HyperlinkedIdentityField(
        view_name="property-detail",
        lookup_field = "slug"
    )
    class Meta:
        model = Property
        fields = ["title", "slug", "price", "property_url", "location", "bedrooms", "bathrooms", "square_feet", "status", "agent_email"]

    def get_agent_email(self, obj:Property):
        return obj.agent.email
    

class PropertyDetailSerializer(serializers.ModelSerializer):
    agent_email = serializers.SerializerMethodField("get_agent_email")
    class Meta:
        model = Property
        fields = ["title", "slug", "location", "photo_main", "bedrooms", "bathrooms", "square_feet", "status", "agent_email"]

    def get_agent_email(self, obj:Property):
        return obj.agent.email

    def update(self, instance, validated_data):
        print('this - here')
        demo = Property.objects.get(slug=instance.slug)
        Property.objects.filter(slug=instance.slug).update(**validated_data)
        return demo
    



class PropertyAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["name", "phone_number", "message"]