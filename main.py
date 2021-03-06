LIPO_DIS_PER = 0.8
LIPO_SPEC_ENG = 100 * 3600 *  LIPO_DIS_PER# 100 Wh/Kg - 158 Wh/Kg > KJ / Kg

VEHICLE_SPEC_POW_CON = 200 # 200 W/Kg
OPERATING_HEIGHT = 200 # 200 m
PAYLOAD = 5# Kg
FIXED_WEIGHT = PAYLOAD 
RANGE = 5000 # m

WPNAV_ACCEL = 2.50 # m/s^2
WPNAV_ACCEL_Z = 1.0 # m/s^2
WPNAV_JERK = 1 # m /s^3

WPNAV_SPEED = 10  # m/s
WPNAV_SPEED_DN = 2.5 # m/s
WPNAV_SPEED_UP = 10 # m/s


LAND_ALT_LOW = 3 # m
LAND_SPEED = .3 # m/s
LAND_SPEED_HIGH = 5 # m/s

 

def time_to_climb(altitude):
	t1 = (WPNAV_SPEED_UP/ WPNAV_ACCEL_Z)
	d1 = 0.5 * t1**2
	t3 = t1
	d3 = d1
	d2 = altitude - (d1 + d3)
	t2 = d2 / WPNAV_SPEED_UP

	return t1 + t2 + t3
	
def time_to_land(altitude):
	t1 = (WPNAV_SPEED_DN/ WPNAV_ACCEL_Z)
	d1 = 0.5 * t1**2
	t3 = t1
	d3 = d1
	t4 = (LAND_ALT_LOW / LAND_SPEED)
	d4 = LAND_ALT_LOW
	d2 = altitude - (d1 + d3 + d4)
	t2 = d2 / WPNAV_SPEED_UP
	return t1 + t2 + t3 + t4
	
	
def time_to_cruise(distance):
	t1 = (WPNAV_SPEED/ WPNAV_ACCEL)
	d1 = 0.5 * t1**2
	t3 = t1
	d3 = d1
	d2 = distance - (d1 + d3)
	t2 = d2 / WPNAV_SPEED
	return t1 + t2 + t3

CLIMB_TIME = time_to_climb(OPERATING_HEIGHT) * 2 
DESCENT_TIME = time_to_land(OPERATING_HEIGHT)* 2
CRUISE_TIME = time_to_cruise(RANGE)* 2
TOTAL_TIME = (CLIMB_TIME + DESCENT_TIME + CRUISE_TIME)
TOTAL_SPEC_ENERGY = (VEHICLE_SPEC_POW_CON * 1.5) * (CLIMB_TIME + DESCENT_TIME) + CRUISE_TIME * VEHICLE_SPEC_POW_CON
BATT_WEIGHT = (TOTAL_SPEC_ENERGY * 2 * PAYLOAD)/(LIPO_SPEC_ENG - TOTAL_SPEC_ENERGY)
print(BATT_WEIGHT)
