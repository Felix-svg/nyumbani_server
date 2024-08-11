# Nyumbani App Server

This repository contains the backend server for the Nyumbani Web App, a modern real estate platform designed to provide users with comprehensive property listings, reviews, and detailed property information. The server provides a RESTful API for interacting with the frontend application.

[Nyumbani App - Live Demo](https://nyumbani-app.vercel.app/)

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Property Listings**: Retrieve and manage property listings with detailed information such as price, location, features, and contact details.
- **Reviews**: Users can view and add reviews for specific properties.
- **RESTful API**: A fully documented RESTful API for seamless integration with the Nyumbani frontend.
- **Error Handling**: Comprehensive error handling and validation to ensure a smooth user experience.
- **Database Migrations**: Use of Alembic for managing database migrations.

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Database**: PostgreSQL (or SQLite for development/testing)
- **Environment Management**: Python-dotenv
- **Database Migrations**: Alembic

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL (for production) or SQLite (for development/testing)
- Git

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/nyumbani_app_server.git
   cd nyumbani_app_server

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables:**
Create a .env file in the root directory and configure the necessary environment variables:

   ```bash
   FLASK_APP=run.py
   FLASK_ENV=development
   DATABASE_URL=postgresql://username:password@localhost/nyumbani_db

5. **Initialize Database:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

6. **Run the Server:**

   ```bash
   python3 app.py

   The server will be running at http://127.0.0.1:5000/.

## API Endpoints
- **GET /listings**: Retrieve all property listings.
- **GET /listings/<id>**: Retrieve a specific property by its ID.
- **GET /reviews?houseId=<house_id>**: Retrieve all reviews for a specific house.
- **POST /reviews**: Add a new review for a house.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch (git checkout -b feature-branch-name).
3. Commit your changes (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature-branch-name).
5. Open a pull request.

## License
This project is licensed under the MIT License - See the <a href="/LICENSE">LICENSE</a> file for details.