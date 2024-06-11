from rest_framework import serializers

from .models import CrewMember, Project, CrewRequirement, SelectedCrew

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = ['name', 'userid', 'crewType', 'roleJobTitle', 'services', 'tags', 'expertise', 'yoe', 'minRatePerDay', 'maxRatePerDay', 'location']

class CrewRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewRequirement
        fields = ['project', 'role', 'location', 'number_needed']

class SelectedCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedCrew
        fields = ['project', 'crew_member', 'crew_requirements']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'project_detail_from_customer', 'detailed_desc', 'roleJobTitles', 'crew_requirements', 'queries', 'selected_crews']