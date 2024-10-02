# e-Railway Passenger Dashboard

## Overview
The **e-Railway Passenger Dashboard** is a web application designed for users to manage their train travel experiences with ease. It provides features for booking tickets, checking train schedules, and accessing customer support, along with various statistics and promotions.

## Features
- **User-Friendly Dashboard**: A welcoming interface that introduces users to their travel options and services.
- **Travel Statistics**: Visual representation of travel history and upcoming journeys using charts.
- **Ticket Booking**: Options to book, manage, and view ticket history.
- **Real-Time Train Schedule**: Access to up-to-date train schedules and notifications for delays.
- **Customer Support**: Direct access to support representatives for inquiries and assistance.
- **Profile Management**: Users can update personal information and manage payment methods.
- **Promotions**: Information on ongoing discounts and exclusive offers.
- **Railway Information**: Overview of railways in Cameroon with their operational status.
- **Google Maps Integration**: Display of the nearest railway locations.

## Technologies Used
- **Frontend**:
  - HTML5, CSS3
  - Bootstrap 4 for responsive design
  - jQuery for DOM manipulation
  - Chart.js for data visualization
  - AOS (Animate on Scroll) for animations
  - Google Maps API for location display

- **Backend**:
  - Django (assumed based on template language)
  - Database (assumed to be configured with Django ORM)

## Installation
To set up the e-Railway Passenger Dashboard locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/e-railway-dashboard.git
   cd e-railway-dashboard
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure to have Django and other necessary packages installed. You can use `requirements.txt` if available:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage
- **Login**: Users can log in using their credentials. 
- **Dashboard Navigation**: The sidebar provides links to different sections of the dashboard.
- **Interactive Elements**: Click on various cards to access more detailed functionalities like ticket booking and schedule checking.
- **Responsive Design**: The application adapts to various screen sizes, making it accessible on both mobile and desktop devices.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to report issues, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-YourFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Bootstrap](https://getbootstrap.com/) for responsive design.
- [Chart.js](https://www.chartjs.org/) for data visualization.
- [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview) for the mapping functionality.
- [Animate.css](https://animate.style/) and [AOS](https://michalsnik.github.io/aos/) for animations.

## Contact
For any inquiries, please contact:
- **Your Name**: [your.email@example.com](mailto:your.email@example.com)

---

Feel free to modify this README to better suit your project's specific needs!



all the default login are  in the folder management/command