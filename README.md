# TopoConsultingAssignment
Brief introduction
Web application designed using HTML for the frontend, and Python & Flask framework for the backend to display data visualization diagrams for the different datasets merged into a single unified_data.csv

Tast1.py
A script or application that:

- Reads and ingests data from all the provided formats.

- Cleans the data to handle missing values and inconsistencies.

- Merges the data into a unified structure for further use (e.g., a table, array, or object).

Task2app.py
Data Visualization using plotly, unified_data.csv created from Task1.py and setting up of REST API endpoints using Flask framework

templates/index.html
Frontend designed to display the data visualization graphs/charts and table using html

The other files are designed to reorganize and refactor the code using OOP principles and add corresponding unit and integration testing
for the different classes

Application.py
Application is launched from Application.py

##Flask-Based Data Visualization Application
1. Clone this repository using `git clone https://github.com/RiyaMehta2211/TopoConsultingAssignment.git`
2. Verify that you have python installed using `python --version`
3. If you do not have python installed, you can download it from this url here http://python.org/downloads/
4. Navigate to the `TopoConsultingAssignment` folder in terminal using `cd ~/your/path/to/the/folder`
5. Install the requirements using `pip install -r requirements.txt`
6. Run the application using `python app.py` in the terminal. Alternatively, you may also run app.py through your preferred
IDE such as Visual Studio Code. If both approaches do not work, please try the following approach in command line:
`flask run --host=0.0.0.0 --port=8000` If current port is busy, please try another port.

7. You will see a link with a message similar to the one below:
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.10.225:8000 
8. Click and copy the link to your preferred browser (for eg. http://127.0.0.1:8000) to access the web application