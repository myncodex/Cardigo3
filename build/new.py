import obd
port='COM20'
# Create an OBD connection
connection = obd.OBD(port)

# Check if the connection has been established
if not connection.is_connected():
    print("Unable to connect to the OBD-II adapter")
    exit()

# Get the coolant temperature
coolant_temp = connection.query(obd.commands.COOLANT_TEMP).value
print(coolant_temp)

# Get the oil temperature
atm_temp = connection.query(obd.commands.AMBIANT_AIR_TEMP).value
print(int(atm_temp))

# Get the barometric pressure
barometric_pressure = connection.query(obd.commands.BAROMETRIC_PRESSURE).value.to("psi")
print(type(barometric_pressure))

# Get the throttle position
throttle_pos = connection.query(obd.commands.THROTTLE_POS).value
print(type(throttle_pos))

# Close the connection
connection.close()
