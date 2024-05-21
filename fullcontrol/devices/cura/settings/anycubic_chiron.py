default_initial_settings = {
    "name": "Anycubic Chiron",
    "manufacturer": "Anycubic",
    "start_gcode": "M107 ;Start with the fan off\nG21 ;Set units to millimeters\nG91 ;Change to relative positioning mode for retract filament and nozzle lifting\nG1 F200 E-3 ;Retract 3mm filament for a clean start\nG92 E0 ;Zero the extruded length\nG1 F1000 Z5 ;Lift the nozzle 5mm before homing axes\nG90 ;Absolute positioning\nM82 ;Set extruder to absolute mode too\nG28 X0 Y0 ;First move X/Y to min endstops\nG28 Z0 ;Then move Z to min endstops\nG1 F1000 Z15 ;After homing lift the nozzle 15mm before start printing\n",
    "end_gcode": "G91 ;Change to relative positioning mode for filament retraction and nozzle lifting\nG1 F200 E-4;Retract the filament a bit before lifting the nozzle\nG1 F1000 Z5;Lift nozzle 5mm\nG90 ;Change to absolute positioning mode to prepare for part rermoval\nG1 X0 Y400 ;Move the print to max y pos for part rermoval\nM104 S0 ; Turn off hotend\nM106 S0 ; Turn off cooling fan\nM140 S0 ; Turn off bed\nM84 ; Disable motors\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 400,
    "build_volume_y": 400,
    "build_volume_z": 450,
}
