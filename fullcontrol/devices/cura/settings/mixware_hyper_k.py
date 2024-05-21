default_initial_settings = {
    "name": "Hyper K",
    "manufacturer": "Mixware",
    "start_gcode": "M140 S{data['bed_temp']} ; Heat bed\nM109 S{data['nozzle_temp']} ; Heat nozzle\nM190 S{data['bed_temp']} ; Wait for bed heating\nG28 ; home all axes\nM117 Purge extruder\nG92 E0 ; reset extruder\nG1 Z5.0 F1000 ; move z up little to prevent scratching of surface\nG1 X0.1 Y20 Z0.3 F5000.0 ; move to start-line position\nG1 X0.1 Y100.0 Z0.3 F1500.0 E15 ; draw 1st line\nG1 X0.4 Y100.0 Z0.3 F5000.0 ; move to side a little\nG1 X0.4 Y20 Z0.3 F1500.0 E30 ; draw 2nd line\nG92 E0 ; reset extruder\nG1 Z5.0 F1000 ; move z up little to prevent scratching of surface",
    "end_gcode": "G91; relative positioning\nG1 Z1.0 F3000 ; move z up little to prevent scratching of print\nG90; absolute positioning\nG1 X0 Y200 F1000 ; prepare for part removal\nM104 S0; turn off extruder\nM140 S0 ; turn off bed\nG1 X0 Y220 F1000 ; prepare for part removal\nM84 ; disable motors\nM106 S0 ; turn off fan",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 50.0,
    "travel_speed": 120.0,
    "dia_feed": 1.75,
    "build_volume_x": 225,
    "build_volume_y": 225,
    "build_volume_z": 250,
}
