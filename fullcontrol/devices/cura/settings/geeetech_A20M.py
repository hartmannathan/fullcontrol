default_initial_settings = {
    "name": "Geeetech A20M",
    "manufacturer": "Geeetech",
    "start_gcode": ";GeeeTech A20M start script\nG28 ;home\nG90 ;absolute positioning\nG1 X0 Y0 Z15 E0 F300 ;go to wait position\nM140 S{data['bed_temp']} ;set bed temp\nM109 S{data['nozzle_temp']} ;set extruder temp and wait\nG1 Z0.8 F200 ;set extruder height\nG1 X220 Y0 E80 F1000 ;purge line\n;end of start script",
    "end_gcode": "G91\nG1 E-1\nG0 X0 Y200\nM104 S0\nG90\nG92 E0\nM140 S0\nM84\nM104 S0\nM140 S0\nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 250,
    "build_volume_y": 250,
    "build_volume_z": 250,
}
