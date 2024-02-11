# Dietary Requirements

Dietary Requirements is a Django web application designed to manage and display party invitations, including customized information for guests about the party's dietary accommodations. This application allows guests to specify their dietary preferences, allergies, and any other dietary restrictions they may have.

## Live Demo

The application is live at [dietarypreferences.pythonanywhere.com](https://dietarypreferences.pythonanywhere.com/).

## Screenshots

![image](https://github.com/divyesh1099/dietaryRequirements/assets/65925922/8ae0c38a-e9ae-4082-b859-3f5e55e99047)

![image](https://github.com/divyesh1099/dietaryRequirements/assets/65925922/913fa473-3cf0-45fc-a10d-52bbfd00625c)

![image](https://github.com/divyesh1099/dietaryRequirements/assets/65925922/2b8e6ff9-78c5-4bdb-bf3f-5c51d81c12b9)

![image](https://github.com/divyesh1099/dietaryRequirements/assets/65925922/1b926923-f670-483c-aaf0-39665578953f)

## Features

- **Guest Invitations**: Send out party invitations with a unique twist by including dietary preferences.
- **Dietary Preferences Management**: Guests can specify their dietary needs, ensuring the party menu can accommodate everyone.
- **Static Pages**: Includes several static pages like "Let's Celebrate Together!", "Details", "Dress Code", and "Gift for You" with animated elements for a more engaging user experience.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript with GSAP for animations
- **Hosting**: Hosted on PythonAnywhere

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or later
- pip
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/divyesh1099/dietaryRequirements.git
   ```
2. Navigate to the project directory:
   ```
   cd dietaryRequirements
   ```
3. Create a virtual environment (optional):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
4. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Collect static files:
   ```
   python manage.py collectstatic
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```
8. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Deployment

This project is deployed on PythonAnywhere. Follow the PythonAnywhere documentation for deploying a Django app for specific instructions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- GSAP for the smooth animations
- PythonAnywhere for hosting the Django app
- Django community for the comprehensive documentation and support
- Moti❤️
