default_initial_settings = {
    "name": "Tizyx Evy",
    "manufacturer": "Tizyx",
    "start_gcode": "M82\nG90\nG28 X\nG28 Y\nG28 Z\nG29\nG91\nG1 Z0\nG90\nM82\nG92 E0\nG1 X125 Y245 F3000\nG1 Z0",
    "end_gcode": "M104 S0\nM140 S0\nG91\nG1 E-5 F300\nG1 Z+3 F3000\nG1 Y245 F3000\nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 255,
    "build_volume_y": 255,
    "build_volume_z": 255,
}
