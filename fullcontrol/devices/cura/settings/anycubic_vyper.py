default_initial_settings = {
    "name": "Anycubic Vyper",
    "manufacturer": "Anycubic",
    "start_gcode": "G21 ;metric values\nG90 ;absolute positioning\nM82 ;set extruder to absolute mode\nM107 ;start with the fan off\nG28 X0 Y0 ;move X/Y to min endstops\nM300 S1318 P266\nG28 Z0 ;move Z to min endstops\nG0 Z0.2\nG92 E0 ;zero the extruded length\nG1 X40 E25 F400 ; Extrude 25mm of filament in a 4cm line. Reduce speed (F) if you have a nozzle smaller than 0.4mm!\nG92 E0 ;zero the extruded length again\nG1 E-1 F500 ; Retract a little\nG1 X80 F4000 ; Quickly wipe away from the filament line\nM117 ; Printing…\nG5",
    "end_gcode": "M104 S0 ; turn off extruder\nM140 S0 ; turn off bed\nM84 ; disable motors\nM107\nG91 ;relative positioning\nG1 E-1 F300 ;retract the filament a bit before lifting the nozzle, to release some of the pressure\nG1 Z+0.5 E-5 ;X-20 Y-20 F{data['travel_speed']} ;move Z up a bit and retract filament even more\nG28 X0 ;Y0 ;move X/Y to min endstops, so the head is out of the way\nG1 Y180 F2000\nM84 ;steppers off\nG90\nM300 S1318 P266",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 250,
    "build_volume_y": 255,
    "build_volume_z": 265,
}
