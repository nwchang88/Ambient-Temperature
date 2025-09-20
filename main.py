import csv


def load_simulated_readings(filename: str) -> list[tuple[float, float]]:
   """
   Loads pre-recorded temperature readings from a CSV file.
   Each row in the file should contain two float values:
   - CPU temperature
    - Sense HAT temperature
   """
   readings = []
   with open(filename, 'r') as file:
      reader = csv.reader(file)
      for row in reader:
         if len(row) == 2:
            try:
               temp_cpu = float(row[0])
               temp_hat = float(row[1])
               readings.append((temp_hat, temp_cpu))
            except ValueError:
               continue
   return readings
   

try:
   import sense_hat
   use_simulated = False
   my_sensor = sense_hat.SenseHat()
except:
   use_simulated = True
   simulated_data = load_simulated_readings('simulated_data.csv') # AI allowed
   simulated_counter = 0
   print("hi")


def get_temperature() -> tuple[float, float]:
   """
   Returns the Sense HAT temperature and CPU temperature in °C

   On real hardware, the function uses Sense HAT and OS CPU sensor.
   In simulation mode, it cycles through pre-recorded data.
   This wrapper allows the rest of your program to run identically
   on a variety of machines, with or without an actual Sense HAT.
   """
   if use_simulated:
      global simulated_counter
      temp_hat, temp_cpu = simulated_data[simulated_counter]
      simulated_counter = (simulated_counter + 1) % len(simulated_data)
      print(temp_hat, temp_cpu)
   else:
      temp_hat = my_sensor.get_temperature()
      temp_cpu = read_cpu_temperature() # AI allowed
   return (temp_hat, temp_cpu)

get_temperature()