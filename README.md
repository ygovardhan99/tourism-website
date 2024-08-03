# Kanyarasi Travels

Welcome to the Kanyarasi Travels project! This application is designed to provide users with an efficient and user-friendly experience for booking travel services.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

Kanyarasi Travels is a comprehensive travel booking platform that allows users to search for and book flights, hotels, and other travel-related services. The platform is built with a focus on usability, and scalability.

## Features

- Book tour packages
- Admin control center
- View booking history
- Responsive design for mobile and desktop users

## Installation

To get a local copy up and running, follow these simple steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/ygovardhan99/tourism-website.git
    cd tourism-website
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the database:**
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

4. **Run the application:**
    ```sh
    python app.py
    ```

## Usage

Once the application is up and running, you can access it in your web browser at `http://127.0.0.1:5000/`.

### Booking

- Proceed to book your selected tour package.
- Fill in the necessary details and confirm your booking.

### Admin Dashboard

- Admin can click on the Admin Dashboard option available at the bottom of the page and should be able to login using the default username(admin) & password (admin123).
- Access the booking history from your user profile.
