# Taxi Reservation System

## Developer
**Nitin Pravin Singh**  
Student of Amrutvahini College of Engineering  
T.E Computer Engineering Department  
(Under Zensar Python and SQL Training)

---

## Project Description
The Taxi Reservation System is a Python-based developed using Flask and integrated with an Oracle Database. It allows efficient management of taxis, customer reservations, and fare calculations while ensuring real-time updates on taxi availability.

This system is designed to demonstrate the integration of Python with Oracle Database using `cx_Oracle`.

---

## Features

### Taxi Management:
- Add new taxis to the system with driver details.
- Maintain the status of taxi availability.

### Reservation Management:
- Create customer reservations with pickup and drop locations.
- Automatically assign available taxis to reservations.
- Update taxi availability upon reservation completion.

### Fare Calculation:
- Calculate ride fares dynamically based on distance and predefined rates.

### Real-Time Updates:
- Track and update taxi availability and reservation statuses in real-time.

---

## Technologies Used

- **Python (Flask)**: Backend web framework.
- **cx_Oracle**: Library for Oracle database connectivity.
- **Oracle Database**: For data storage and management.

---

## Installation and Setup

### Prerequisites:
- Python 3.7 or later
- Oracle Database (or Oracle XE)
- Required Python packages:
  - `Flask`
  - `cx_Oracle`
    

## Code Explanation

### `Taxi` Class
Represents a taxi with attributes such as ID, driver details, and availability status.  

**Methods**:
1. `assign_taxi()`: Marks the taxi as unavailable.  
2. `release_taxi()`: Marks the taxi as available.  

---

### `Reservation` Class
Represents a reservation with attributes for customer details, pickup/drop locations, taxi assignment, fare, and status.  

**Methods**:
1. `assign_taxi()`: Links a taxi to the reservation and calculates the fare.  
2. `complete_reservation()`: Releases the assigned taxi and marks the reservation as completed.  

---

### `TaxiReservationSystem` Class
Manages the collection of taxis and reservations.  

**Methods**:
1. `add_taxi()`: Adds a new taxi to the system and database.  
2. `create_reservation()`: Creates a new reservation and assigns an available taxi.  
3. `calculate_fare()`: Calculates the fare based on the distance.  

---

### Flask Routes
1. `/add_taxi`: Adds a new taxi to the system.  
2. `/book_taxi`: Books a taxi for a customer.  
3. `/available_taxis`: Returns a list of all available taxis.  
4. `/reservations`: Returns a list of all reservations.  

---

## Guidance
This project was developed under the guidance of **Sir Aniruddh Gaikwad**.  
Special thanks for the mentorship and support throughout the project development.

---

## Acknowledgments
- **Amrutvahini College of Engineering** for providing the platform to develop this project.  
- **Zensar Python and SQL Training Program** for enhancing technical skills.  
- **Mentor and Faculty** for their continuous guidance and encouragement.  

---

## License
This project is developed for academic purposes and is not intended for commercial use.
   
