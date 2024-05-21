default_initial_settings = {
    "name": "Creality Ender-3 S1 Pro",
    "manufacturer": "Creality3D",
    "start_gcode": "; Ender 3 S1 Pro Start G-code\n; M413 S0 ; Disable power loss recovery\nG92 E0 ; Reset Extruder\n\n; Prep surfaces before auto home for better accuracy\nM140 S{data['bed_temp']}\nM104 S{data['nozzle_temp']}\n\nG28 ; Home all axes\nG1 Z10.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\nG1 X0 Y0\n\nM190 S{data['bed_temp']}\nM109 S{data['nozzle_temp']}\n\nG1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position\nG1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line\nG1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little\nG1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line\nG92 E0 ; Reset Extruder\nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\nG1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish\n",
    "end_gcode": "G91 ;Relative positioning\nG1 E-2 F2700 ;Retract a bit\nG1 E-2 Z0.2 F2400 ;Retract and raise Z\nG1 X5 Y5 F3000 ;Wipe out\nG1 Z10 ;Raise Z more\nG90 ;Absolute positioning\n\nG1 X0 Y{data['build_volume_y']} ;Present print\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\n\nM84 X Y E ;Disable all steppers but Z\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 150.0,
    "dia_feed": 1.75,
    "build_volume_x": 220,
    "build_volume_y": 220,
    "build_volume_z": 270,
}
