# Multi PC Logger

This project involves setting up a network of PCs that periodically collect system information and send it to a central Django server. The server stores the data in a database and provides a web interface for viewing the information.

## Functionality

The project consists of the following components:

1. Python script: A script that runs on each PC and collects system information using standard Python libraries. The information is compiled into a JSON file and sent to the Django server via HTTP.
2. Django server: A server that receives the JSON files and stores the information in a database.
3. Django app: A web interface that displays the system information stored in the database. The app includes a search feature that allows users to retrieve information for a specific PC.
4. Dashboard: An admin dashboard that displays critical alerts such as changes in physical RAM, HDD, and OS version.

## Requirements

The project requires the following skills and technologies:

- Python programming
- Network programming
- System administration
- Database management
- Django web framework

## Installation

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python libraries by running `pip install -r requirements.txt`.
3. Configure the Django settings in `pc_logger/settings.py`.
4. Set up the database by running `python manage.py migrate`.
5. Deploy the Python script to each PC.
6. Run the Django server using `python manage.py runserver`.

## Usage

To use the project, follow these steps:

1. Run the Python script on each PC.
2. Open the web interface at `http://127.0.0.1:8000/` to view the system information.
3. Use the search feature to retrieve information for a specific PC.


## Credits

This project was created by [Dhiraj Kapse](https://github.com/dhir4j), [Vaibahv Gangurde](https://github.com/Vaibhavsg17) & [Mahek Mulla](https://github.com/mash786) as a mini-project during their second year of Information Technology Engineering.

## License

[MIT License](https://github.com/dhir4j/Multi-PC-Logger/blob/Main/MIT%20License.txt)

Copyright (c) 2023 Dhiraj Kapse & others