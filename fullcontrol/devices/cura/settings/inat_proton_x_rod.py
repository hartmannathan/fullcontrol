default_initial_settings = {
    "name": "Proton X Rod",
    "manufacturer": "Inat s.r.o.",
    "start_gcode": "G28 ;Home\nG0 X-2 Y150 F6000 ;Move to the side\nG0 Z0.3 F200 ;Move nozzle down\nM192 ; Wait for probe temperature to settle\nG28 Z\nG29\nG0 X0 Y0 Z30 F6000\nM84 E\nM0\nG1 Z15.0 F6000 ;Move the platform down 15mm\n",
    "end_gcode": "M400\nM104 S0\nM140 S0\nM107\n;Retract the filament\nG92 E1\nG1 E-1 F300\nG28 R5 X\nG0 Y300 F3000\nM84\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 150,
    "dia_feed": 1.75,
    "build_volume_x": 304,
    "build_volume_y": 304,
    "build_volume_z": 300,
}
