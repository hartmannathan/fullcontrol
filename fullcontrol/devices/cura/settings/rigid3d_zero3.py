default_initial_settings = {
    "name": "Rigid3D Zero3",
    "manufacturer": "Rigid3D",
    "start_gcode": "G21\nG92 E0\nG28\nM420 S1\nM107\nG90\nG1 X10.0 Y0.1 Z0.3 F3000.0\nG1 X190.0 Y0.1 Z0.3 F1500.0 E15\nG1 X190 Y0.4 Z0.3 F3000.0\nG1 X10.0 Y0.4 Z0.3 F1500.0 E30\nG1 Z2.0 F1500.0\nG92 E0\n",
    "end_gcode": "G92 E0\nT0\nG1 F1800 E-2\nG27 P2\nM107\nM104 T0 S0\nM140 S0\nG90\nG92 E0\nM18\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 80.0,
    "dia_feed": 1.75,
    "build_volume_x": 200,
    "build_volume_y": 200,
    "build_volume_z": 200,
}
