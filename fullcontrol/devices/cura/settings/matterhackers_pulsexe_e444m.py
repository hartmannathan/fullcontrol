default_initial_settings = {
    "name": "Pulse XE E-444M",
    "manufacturer": "MatterHackers",
    "start_gcode": "G21 ; set units to millimeters\nG90 ; use absolute positioning\nM82 ; absolute extrusion mode\nG28 ; home axes\nM104 S{data['nozzle_temp']} ; set extruder temp\nM140 S{data['bed_temp']} ; set bed temp\nM190 S{data['bed_temp']} ; wait for bed temp\nM109 S{data['nozzle_temp']} ; wait for extruder temp\nG29 ; mesh bed leveling\n\nG92 E0\nG1 X5 Y5 Z0.8 F1800\nG1 X100 Z0.3 E25 F900\nG92 E0\nG1 E-2 F2400",
    "end_gcode": "M104 S0 ; turn off extruder\nM140 S0 ; turn off heatbed\nM107 ; turn off fan\nG1 X0 Y{data['build_volume_y']}; home X axis and push Y forward\nG28 Z0\nM84 ; disable motors",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 50,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 250,
    "build_volume_y": 220,
    "build_volume_z": 215,
}
