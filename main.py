RANGE = 5000 # m
VELOCITY_HORZONTAL = 10 # m/s
PAYLOAD_WEIGHT = 5 # kg
FRAME_WEIGHT_RATIO = # percent
MOTOR_WEIGHT_RATIO = # percent # motor plus propeller plus esc plus power distribution plus wires weight
FRAME_WEIGHT_RATIO = # percent
BATTERY_WEIGHT_RATIO = # percent
ELECTRONICS_WEIGHT = 1 # kg
WATT_PER_KG = # watt/kg
BATTREY_POWER_DENSITY = # Wh / kg
flight_time_rrequired = RANGE / VELOCITY_HORZONTAL # seconds

total_weight = FRAME_WEIGHT + ELECTRONICS_WEIGHT + PAYLOAD_WEIGHT + BATTERY_WEIGHT

average_current_draw = total_weight * WATT_PER_KG

battery_capacity_required = 

battery_weight_calculated = battery_capacity_required / BATTREY_POWER_DENSITY 