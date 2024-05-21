default_initial_settings = {
    "name": "Prusa i3 Mk3/Mk3s",
    "manufacturer": "Prusa3D",
    "start_gcode": "G21 ; set units to millimeters\nG90 ; use absolute positioning\nM82 ; absolute extrusion mode\nM104 S{data['nozzle_temp']} ; set extruder temp\nM140 S{data['bed_temp']} ; set bed temp\nM190 S{data['bed_temp']} ; wait for bed temp\nM109 S{data['nozzle_temp']} ; wait for extruder temp\nG28 W ; home all without mesh bed level\nG80 ; mesh bed leveling\nG92 E0.0 ; reset extruder distance position\nG1 Y-3.0 F1000.0 ; go outside print area\nG1 X60.0 E9.0 F1000.0 ; intro line\nG1 X100.0 E21.5 F1000.0 ; intro line\nG92 E0.0 ; reset extruder distance position",
    "end_gcode": "M104 S0 ; turn off extruder\nM140 S0 ; turn off heatbed\nM107 ; turn off fan\nG1 X0 Y210; home X axis and push Y forward\nM84 ; disable motors",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 250,
    "build_volume_y": 210,
    "build_volume_z": 210,
}
