# Flight booking Application

## Overview
This flight booking application allow customers to create their accounts and search flights based on date and time and book a seat.

## Installation
1. Clone the repository  
`git clone https://github.com/Shantanu3438/Flight-Booking`

2. Install all the required packages using `pip`  
`pip install -r requirements.txt`

3. Make all the necessary migrations and then migrate  
`python3 manage.py makemigrations`  
`python3 manage.py migrate`

5. Run the development server  
`python3 manage.py runserver`

## API endpoints
1. Signup  `/signup/`
2. Login `/login/`
3. Logout `/logout/`
4. Flights `/flights/`
5. Search flights `/flights/filter/`
6. Book a seat `/flights/booking/<str:flight_number>`
7. See all booking `/flights/booked/`
