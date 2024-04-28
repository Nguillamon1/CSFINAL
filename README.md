# Art Prompt Generator

## Project Overview
The Art Prompt Generator is a web application designed to inspire artists by providing random artistic prompts and a display of various color palettes. The application aims to facilitate creativity by offering unique art prompts alongside inspiring color combinations fetched from the CSS Colors API.

## Usage Guidelines
- **Homepage**: Users are greeted with a "Generate Art Prompt" button and an initial display of color palettes.
- **Generate Prompt**: By clicking the "Generate Art Prompt" button, users will receive a new art prompt and a fresh set of colors.
- **Navigation**: Users can return to the homepage or generate another prompt directly from the prompt display page.

## Dependencies
- **Flask**: A micro web framework written in Python.
- **Python**: Programming language used.
- **CSS Colors API**: External API used for fetching color data.
- **Requests**: Python HTTP library used for API calls, https://csscolorsapi.com/api/colors. 

## Project Structure
- **app.py**: Contains the Flask application setup, routes, and API call functions.
- **templates/**: Directory for HTML templates.
  - `index.html`: Base template displaying the initial interface.
  - `prompt.html`: Extends `index.html` and includes the art prompt and colors.
- **static/**: Directory for static files like CSS.
  - `styles.css`: Contains styling for the application.

## Collaboration Information
- **Solo Project**: This project was developed by [Your Name]. All planning, development, and testing were carried out independently.

## Acknowledgments
- **Flask**: For providing the web framework used in this project.
- **CSS Colors API**: For supplying the dynamic color data showcased in the app.

## Reflection

### Process Reflection
- **What Went Well**: The use of Flask allowed for rapid development and easy setup of the web application. Integrating the CSS Colors API was straightforward and enhanced the user experience by providing dynamic content.
- **Challenges Faced**: Handling API responses and ensuring robust error checking was initially challenging. Designing a user-friendly UI that was also aesthetically pleasing required multiple iterations.
- **Improvements**: Future versions could include user customization features, such as allowing users to select the type of art prompts or color schemes they prefer.

### Learning Reflection
- **Project Learnings**: Gained deeper insights into Flask application structuring, API integration, and dynamic content management in web applications.
- **Use of Learnings**: The skills acquired will be instrumental in future projects that require integration of external APIs and user interaction.
- **Role of ChatGPT**: ChatGPT was invaluable for providing initial code snippets, debugging help, and guidance on best practices for documentation.
- **Wish List**: Knowledge of advanced CSS techniques and JavaScript could have enhanced the project further, especially for creating more interactive and responsive designs.

*Developed by Natalie Guillamon, Junior*