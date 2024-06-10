from rest_framework import serializers

from .models import CrewMember, Project

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = ['name', 'userid', 'crewType', 'roleJobTitle', 'services', 'tags', 'expertise', 'yoe', 'minRatePerDay', 'maxRatePerDay', 'location']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'project_detail_from_customer', 'detailed_desc', 'roleJobTitles', 'crew_requirements', 'queries', 'selected_crews']
        