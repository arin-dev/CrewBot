import os
import uuid
# import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import CrewMember
from Crew_Bot.CrewGraph import CrewGraph
from crew.models import CrewMember, Project, CrewRequirement, SelectedCrew
from .serializers import CrewMemberSerializer, CrewRequirementSerializer, SelectedCrewSerializer, ProjectsSerializer, ProjectDetailsSerializer

from .APIFunctions import *



@api_view(['POST'])
def create_project(request):

    project_state = get_form_data(request)
    print("project_state", project_state)
    result = CrewGraph(State=State, state=project_state)

    new_project = Project(
    project_name=result["project_name"],
    content_type=result["content_type"],
    budget=result["budget"],
    description=result["description"],
    additional_details=result["additional_details"],
    locations=result["locations"],
    ai_suggestions=result["ai_suggestions"],)
    new_project.save()
    
    crew_req = result["crew_requirements"]
    # print("\n\n\n ########### crew_req ########### ")
    # print("crew_req", crew_req)
    for crew in crew_req:
        new_crew = CrewRequirement(
            project=new_project,
            role=crew["role"], 
            number_needed=crew["number_needed"],
            location=crew["location"],
        )
        new_crew.save()

    selected_crews = result["selected_crews"]
    # print("\n\n\n ###########  \n\n\n")
    # print("\n\nselected_crews", type(selected_crews), selected_crews)
    for role_dict in selected_crews:
        # print("\n\n\n ########### role_dict.items() #######  \n\n\n")
        # print("\n\n role_dict", type(role_dict), role_dict.items())
        for role, crews in role_dict.items():
            # print("\n\n\n ########### role and crews ########### ")
            # print("role", role, "crews", crews, "type", type(crews))
            # print("length", len(crews))
            if isinstance(crews, list):
                for crew in crews:
                    # print("\n\n\n ########### crew ########### ")
                    # print("crew[userid]", crew["userid"])
                    new_selected_crew = SelectedCrew(
                    project=new_project,
                    crew_member=CrewMember.objects.get(userid=crew["userid"]),
                    crew_requirements=CrewRequirement.objects.get(project=new_project, role=role, location=crew["location"]),
                    )
                    new_selected_crew.save()
            else:
                # print("\n\n\n ########### crews ########### ")
                # print("crews[userid]", crews["userid"])
                new_selected_crew = SelectedCrew(
                project=new_project,
                crew_member=CrewMember.objects.get(userid=crews["userid"]),
                crew_requirements=CrewRequirement.objects.get(project=new_project, role=role, location=crews["location"]),
                )
                new_selected_crew.save()
                
    new_project_id = new_project.project_id
    return Response({"message": "Request successful", "project_id": new_project_id})
    # return Response({"message": "Request successful"})

    

@api_view(['GET'])
def crew_requirement(request):
    project_id = request.GET.get('project_id')
    if project_id is None:
        return Response("Project id is required", status=400)
    crew_requirement = CrewRequirement.objects.filter(project_id=project_id)
    serializer = CrewRequirementSerializer(crew_requirement, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def selected_crew(request):
    project_id = request.GET.get('project_id')
    if project_id is None:
        return Response("Project id is required", status=400)
    selected_crew = SelectedCrew.objects.filter(project_id=project_id)
    serializer = SelectedCrewSerializer(selected_crew, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def crew_member(request):
    userid = request.GET.get('userid')
    if userid is None:
        return Response("userid is required", status=400)
    crew_member = CrewMember.objects.filter(userid=userid)
    serializer = CrewMemberSerializer(crew_member, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def list_projects(request):
    projects = Project.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data, status=200)


def transform_crew_data(input_data):
    transformed_data = []

    for crew in input_data['selected_crews_set']:
        member = crew['crew_member']
        role = member['role']
        user_details = {
            "name": member["name"],
            "userid": member["userid"],
            "crew_type": member["crewType"],
            "roleJobTitle": member["role"],
            "services": member["services"].split(","),
            "tags": member["tags"].split(","),
            "expertise": member["expertise"].split(","),
            "yoe": member["yoe"],
            "minRatePerDay": float(member["minRatePerDay"]),
            "maxRatePerDay": float(member["maxRatePerDay"]),
            "location": member["location"]
        }
        
        preferred_because = f"{member['name']} has extensive experience in {', '.join(user_details['expertise'])}. They are based in {member['location']} and their rate fits within the budget."
        
        transformed_data.append({
            role: {
                "UserId": member["userid"],
                "Preferred_because": preferred_because,
                "user_details": user_details
            }
        })

    return transformed_data

@api_view(['GET'])
def project_details(request):
    project_id = request.GET.get('project_id')
    project = Project.objects.get(project_id=uuid.UUID(project_id))
    serializer = ProjectDetailsSerializer(project)
    response = transform_crew_data(serializer.data)
    return Response(response, status=200)


class CrewMemberCreateView(APIView):
    def post(self, request):
        serializer = CrewMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def push_dummy_data(request):
#     print("Testing if dummy data present")

#     print("Starting pushing dummy data")
#     with open('crew/crewdata.json') as f:
#         data = json.load(f)

#     crew_members = []
#     for crew_member in data:
#         # Check if a CrewMember with the same userid already exists
#         if not CrewMember.objects.filter(userid=crew_member["userid"]).exists():
#             crew_members.append(CrewMember(
#                 name=crew_member["name"], 
#                 userid=crew_member["userid"], 
#                 crewType=crew_member["crewType"], 
#                 role=crew_member["roleJobTitle"], 
#                 services=','.join(crew_member["services"]), 
#                 tags=','.join(crew_member["tags"]), 
#                 expertise=','.join(crew_member["expertise"]), 
#                 yoe=crew_member["yoe"], 
#                 minRatePerDay=crew_member["minRatePerDay"], 
#                 maxRatePerDay=crew_member["maxRatePerDay"], 
#                 location=crew_member["location"]
#             ))
#     CrewMember.objects.bulk_create(crew_members)

#     return Response({"message": "Data pushed successfully"}, status=200)