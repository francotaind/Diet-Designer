# DietDesigner

NutriPlanner is a web application designed to help users create personalized meal plans, get recipe ideas, and access nutritional facts based on various ingredients. Built using Django for the backend and HTML/CSS/JavaScript for the frontend, NutriPlanner aims to promote healthy eating and simplify meal planning.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- User registration and authentication
- Personalized meal plan generation
- Recipe suggestions based on meal plans
- Display of nutritional information for each recipe
- Responsive design for both mobile and desktop

## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **External API**: Spoonacular/ Edamam

## Installation

### Prerequisites
- Python 3.8.10
- Django 3.

### Backend Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/francotaind/DietDesigner.git
    cd DietDesigner
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations and run the server:
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend Setup
- Ensure all static files are collected (Django will handle this if configured properly).
- You can add custom CSS and JavaScript files in the `static` directory of your Django app.

## Usage
1. Navigate to `http://localhost:8000` in your web browser.
2. Register a new user account or log in with existing credentials.
3. Generate a personalized meal plan.
4. Browse through the suggested recipes.
5. View detailed nutritional information for each recipe.

## API Integration
DietDesigner integrates with the Spoonacular API/ Edamam API to fetch recipe details and nutritional information.

### Configuration
- You need to obtain an API key from Spoonacular.
- Add the API key to your Django settings file:
    ```python
    SPOONACULAR_API_KEY = 'your_api_key_here'
    ```

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License
This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any inquiries or suggestions, please contact:
- **Name**: Frank Otieno
- **Email**: francotaind00@gmail.com
- **GitHub**: [francotaind](https://github.com/francotaind)

---

Thank you for using DietDesigner! We hope it helps you achieve your nutritional goals.

