from .CrewFunctions import *
from langgraph.graph import END, StateGraph
from typing import TypedDict, List, Annotated
from crew.models import CrewMember, Project, CrewRequirement, SelectedCrew
from .apikey import OPENAI_API_KEY


def unique_roles_getter(State):
    unique_roles = get_unique_roles()
    return {"unique_roles" : unique_roles}

def crew_requirement_getter(State):
    project_name = State["project_name"]
    content_type = State["content_type"]
    description = State["description"]
    additional_details = State["additional_details"]
    locations = State["locations"]
    ai_suggestions = State["ai_suggestions"]
    budget = State["budget"]
    unique_roles = State["unique_roles"]
    user_crew_requirements = State["user_crew_requirements"]


    crew_requirements = get_crew_requirements(project_name, description, unique_roles, content_type, additional_details, locations, ai_suggestions, budget, user_crew_requirements)
    return {"crew_requirements" : crew_requirements}


# def queries_getter(State):
#     crew_requirements = State["crew_requirements"]

#     queries = get_queries(crew_requirements)
#     return {"queries" : queries}


def crew_selection(State):
    project_name = State["project_name"]
    content_type = State["content_type"]
    description = State["description"]
    additional_details = State["additional_details"]
    budget = State["budget"]
    crew_requirements = State["crew_requirements"]

    selected_crews = []
    for crew in crew_requirements:
        filtered_crew = filter_crew_members(crew["role"], 'Dubai')
        number_needed = crew["number_needed"]
        hiring_role = crew["role"]

        selected_crews_for_task = get_selected_crews(filtered_crew, number_needed, hiring_role, project_name, content_type, description, additional_details, budget)
        selected_crews.append({hiring_role:selected_crews_for_task})
    # print("\n\n\n ############# \n\n\n")
    # print("selected_crews:", selected_crews)


    ## selected_crews = get_selected_crew_details(selected_crews_filtering)
    return {"selected_crews" : selected_crews}

    
def state_printer(state):
    print("Project is finished!")
    return


def CrewGraph(State: dict, state):

    workflow = StateGraph(State)

    # workflow.add_node("detailed_desc_getter", detailed_desc_getter)
    workflow.add_node("unique_roles_getter", unique_roles_getter)
    workflow.add_node("crew_requirement_getter", crew_requirement_getter)
    # workflow.add_node("queries_getter", queries_getter)
    workflow.add_node("crew_selection", crew_selection)
    workflow.add_node("state_printer", state_printer)

    # workflow.add_edge("detailed_desc_getter", "unique_roles_getter")
    workflow.add_edge("unique_roles_getter", "crew_requirement_getter")
    # workflow.add_edge("crew_requirement_getter", "queries_getter")
    workflow.add_edge("crew_requirement_getter", "crew_selection")
    workflow.add_edge("crew_selection", "state_printer")

    workflow.set_entry_point("unique_roles_getter")
    workflow.add_edge("state_printer", END)

    app = workflow.compile()

    # inputs = {"project_detail_from_customer": project_detail_from_customer,"num_steps":0}

    var = app.invoke(state)
    return var
