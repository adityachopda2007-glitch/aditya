Simple Flask Resume Generator

This is a lightweight web application built with Python and Flask that allows users to input their professional details via a simple web form and instantly generate a formatted, single-page resume.

Features

Dynamic Resume Generation: Converts structured form input (Name, Contact, Summary, Education, Experience, Skills, Projects) into a single-page HTML resume.

Structured Data Handling: The Flask backend correctly processes multi-line inputs for sections like Education and Experience, and comma-separated inputs for Skills.

Easy Deployment: Minimal dependencies, making it simple to run locally or deploy to a standard Python environment.

Prerequisites

To run this application, you need the following installed:

Python 3.x

The Flask framework

Installation and Setup

Clone the repository (or create the files):
First, ensure you have the core application file (app.py) and the necessary template files in the correct structure.


Install Flask:
Open your terminal or command prompt and use pip to install the required library.

pip install Flask


Place Template Files:
The application requires two HTML templates to be placed inside a folder named templates/ in the same directory as app.py:

index.html: Contains the HTML form for data entry.

resume.html: Contains the design and structure for the final generated resume, utilizing the data dictionary passed from app.py.

Running the Application

Execute the Python file:
In your project's root directory, run the application using Python:

python app.py


Access the application:
Once the server starts, you will see a message similar to:

 * Running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (Press CTRL+C to quit)


Open your web browser and navigate to the provided address (usually http://127.0.0.1:5000/) to access the resume input form.

Generate the Resume:
Fill out the form and click the submit button. The application will render the content using resume.html.

Key Code Logic

The main logic resides in the index() function in app.py:

GET Request: Simply renders the input form (index.html).

POST Request:

It collects basic single-line fields (name, title, email, etc.).

It handles the education and projects fields by splitting the raw text by newlines (\n) to create a list of entries.

It handles the experience field by splitting by double newlines (\n\n) for complex entries, or single newlines otherwise.

It handles the skills field by splitting the input by commas (,).

Finally, it passes the organized data dictionary to the resume.html template for display.
