from flask import Flask, request, jsonify
import datetime
import cx_Oracle

# Flask app
app = Flask(__name__)

# Oracle database connection
def get_db_connection():
    try:
        connection = cx_Oracle.connect(
            user="system",
            password="Nitin55",
            dsn="Taxi"
        )
        return connection
    except cx_Oracle.Error as error:
        print("Error connecting to Oracle database", error)
        return None

class Taxi:
    def __init__(self, taxi_id, driver_name, driver_contact):
        self.taxi_id = taxi_id
        self.driver_name = driver_name
        self.driver_contact = driver_contact
        self.is_available = True

    def assign_taxi(self):
        self.is_available = False

    def release_taxi(self):
        self.is_available = True

class Reservation:
    def __init__(self, customer_name, customer_contact, pickup_location, drop_location, pickup_time):
        self.customer_name = customer_name
        self.customer_contact = customer_contact
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.pickup_time = pickup_time
        self.taxi = None
        self.fare = 0
        self.status = "Pending"

    def assign_taxi(self, taxi, fare):
        self.taxi = taxi
        self.fare = fare
        self.status = "Confirmed"
        taxi.assign_taxi()

    def complete_reservation(self):
        if self.taxi:
            self.taxi.release_taxi()
        self.status = "Completed"

class TaxiReservationSystem:
    def __init__(self):
        self.taxis = []
        self.reservations = []

    def add_taxi(self, taxi_id, driver_name, driver_contact):
        taxi = Taxi(taxi_id, driver_name, driver_contact)
        self.taxis.append(taxi)
        # Save to database
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                """INSERT INTO taxis (taxi_id, driver_name, driver_contact, is_available) 
                VALUES (:1, :2, :3, :4)""",
                (taxi_id, driver_name, driver_contact, 1)
            )
            connection.commit()
            cursor.close()
            connection.close()

    def create_reservation(self, customer_name, customer_contact, pickup_location, drop_location, pickup_time, distance):
        reservation = Reservation(customer_name, customer_contact, pickup_location, drop_location, pickup_time)
        self.reservations.append(reservation)
        self.assign_taxi_to_reservation(reservation, distance)

    def assign_taxi_to_reservation(self, reservation, distance):
        available_taxi = next((taxi for taxi in self.taxis if taxi.is_available), None)
        if available_taxi:
            fare = self.calculate_fare(distance)
            reservation.assign_taxi(available_taxi, fare)
        else:
            print("No taxis available for this reservation.")

    @staticmethod
    def calculate_fare(distance):
        base_fare = 5  # Base fare in dollars
        per_km_rate = 2  # Rate per kilometer
        return base_fare + (distance * per_km_rate)

reservation_system = TaxiReservationSystem()

@app.route('/add_taxi', methods=['POST'])
def add_taxi():
    data = request.json
    taxi_id = data['taxi_id']
    driver_name = data['driver_name']
    driver_contact = data['driver_contact']

    reservation_system.add_taxi(taxi_id, driver_name, driver_contact)
    return jsonify({"message": "Taxi added successfully"}), 201

@app.route('/book_taxi', methods=['POST'])
def book_taxi():
    data = request.json
    customer_name = data['customer_name']
    customer_contact = data['customer_contact']
    pickup_location = data['pickup_location']
    drop_location = data['drop_location']
    distance = float(data['distance'])
    pickup_time = datetime.datetime.now()

    reservation_system.create_reservation(customer_name, customer_contact, pickup_location, drop_location, pickup_time, distance)
    return jsonify({"message": "Reservation created successfully"}), 201

@app.route('/available_taxis', methods=['GET'])
def available_taxis():
    available_taxis = [taxi.__dict__ for taxi in reservation_system.taxis if taxi.is_available]
    return jsonify(available_taxis)

@app.route('/reservations', methods=['GET'])
def reservations():
    reservations = [
        {
            "customer_name": res.customer_name,
            "pickup_location": res.pickup_location,
            "drop_location": res.drop_location,
            "status": res.status,
            "fare": res.fare
        } for res in reservation_system.reservations
    ]
    return jsonify(reservations)

if __name__ == "__main__":
    app.run(debug=True)
