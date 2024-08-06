from rest_framework import serializers
from .models import Job, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'description', 'contactEmail', 'contactPhone']

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Job
        fields = ['id', 'title', 'type', 'description', 'location', 'salary', 'company']

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        company, _ = Company.objects.get_or_create(**company_data)
        job = Job.objects.create(company=company, **validated_data)
        return job

    def update(self, instance, validated_data):
        company_data = validated_data.pop('company', None)
        if company_data:
            company, _ = Company.objects.get_or_create(**company_data)
            instance.company = company
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance