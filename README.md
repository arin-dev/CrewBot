# Film Crew Selection API

This project is a Django-based API designed to manage and select crew members for film projects. It uses a combination of Django models and a custom-built graph-based workflow to process project details and select the appropriate crew members.

## Key Components

### Django Models

Defined in [API/crew/models.py](file:///c%3A/Users/arind/Desktop/CrewBot/API/crew/models.py#1%2C1-1%2C1), these models represent a `CrewMember` and a `Project`. They store information such as the name, user ID, job title, services, expertise, and location of a crew member, as well as project details and selected crews.

### CrewGraph

Defined in [API/Crew_Bot/CrewGraph.py](file:///c%3A/Users/arind/Desktop/CrewBot/API/Crew_Bot/CrewGraph.py#1%2C1-1%2C1), this is a state graph that processes project details and selects crew members. It uses several helper functions to get detailed descriptions, unique roles, crew requirements, and queries. It also includes a function for crew selection based on the requirements.

### CrewFunctions

Defined in [API/Crew_Bot/CrewFunctions.py](file:///c%3A/Users/arind/Desktop/CrewBot/API/Crew_Bot/CrewFunctions.py#1%2C1-1%2C1), these are helper functions used by the CrewGraph. They include functions to filter crew members, get unique roles, and get selected crew details.

### API Endpoint

Defined in [API/crew/views.py](file:///c%3A/Users/arind/Desktop/CrewBot/API/crew/views.py#1%2C1-1%2C1), this is a POST endpoint that takes project details as input and returns the selected crews as a response.

### Crew_Bot

Defined in [API/Crew_Bot/Crew_Bot.py](file:///c%3A/Users/arind/Desktop/CrewBot/API/Crew_Bot/Crew_Bot.py#1%2C1-1%2C1), this script uses the CrewGraph to process a project detail and print the selected crews. It also includes a function to get crew member details from a database.

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Set up your environment variables in a `.env` file.
4. Run the Django server using `python manage.py runserver`.

## Usage

Send a POST request to the API endpoint with the project details. The response will be a JSON object containing the selected crews for the project.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)