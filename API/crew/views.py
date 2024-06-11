from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
import os
import json

from .serializers import CrewMemberSerializer, CrewRequirementSerializer, SelectedCrewSerializer, ProjectSerializer


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from Crew_Bot.CrewGraph import CrewGraph
from .models import CrewMember

from typing import TypedDict, List

@api_view(['POST'])
def crew_bot_endpoint(request):
    project_detail = request.GET.get('project_detail')
    if project_detail is None:
        return Response("Project detail is required", status=400)
    print(project_detail)

    class State(TypedDict):
        num_steps : int
        project_detail_from_customer : str
        detailed_desc : str
        roleJobTitles : List[str]
        crew_requirements : List[dict]
        queries : List[str]
        selected_crews : List[dict]

    result = CrewGraph(State=State, project_detail_from_customer=project_detail)

    print(result)
    # Return the result as a JSON response
    return Response(result)

# @api_view(['POST'])
# def push_dummy_data(request):
#     with open('crew/crewdata.json') as f:
#         data = json.load(f)

#     crew_members = []
#     for crew_member in data:
#         crew_members.append(CrewMember(
#             name=crew_member["name"], 
#             userid=crew_member["userid"], 
#             crewType=crew_member["crewType"], 
#             roleJobTitle=crew_member["roleJobTitle"], 
#             services=','.join(crew_member["services"]), 
#             tags=','.join(crew_member["tags"]), 
#             expertise=','.join(crew_member["expertise"]), 
#             yoe=crew_member["yoe"], 
#             minRatePerDay=crew_member["minRatePerDay"], 
#             maxRatePerDay=crew_member["maxRatePerDay"], 
#             location=crew_member["location"]
#         ))
#     CrewMember.objects.bulk_create(crew_members)

#     return Response("Data pushed successfully", status=200)