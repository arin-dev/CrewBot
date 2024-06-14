from . import views
from django.urls import path

urlpatterns = [
    path('list-projects/', views.list_projects, name='list_projects'),
    path('project-details/', views.project_details, name='project_details'),
    path('create-project/', views.create_project),
    path('view-crew-requirement/', views.crew_requirement, name='crew_requirement'),
    path('view-selected-crew/', views.selected_crew, name='selected_crew'),
    path('view-crew-member/', views.crew_member, name='crew_member'),
    path('add-crew-member/', views.CrewMemberCreateView.as_view(), name='crewmember-create'),
    # path('push_dummy_data/', views.push_dummy_data),
]
