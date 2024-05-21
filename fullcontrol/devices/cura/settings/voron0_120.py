default_initial_settings = {
    "name": "Voron 0",
    "manufacturer": "VoronDesign",
    "start_gcode": "print_start EXTRUDER={data['nozzle_temp']} BED={data['bed_temp']} CHAMBER={0}",
    "end_gcode": "print_end",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 300,
    "dia_feed": 2.85,
    "build_volume_x": 120,
    "build_volume_y": 120,
    "build_volume_z": 120,
}
