default_initial_settings = {
    "name": "JGAurora A5 & A5S",
    "manufacturer": "JGAurora",
    "start_gcode": "; -- START GCODE --\nG21                     ;set units to millimetres\nG90                     ;set to absolute positioning\nM106 S0                 ;set fan speed to zero (turned off)\nG28                     ;home all axis\nM420 S1                 ;turn on mesh bed levelling if enabled in firmware\nG92 E0                  ;zero the extruded length\nG1 Z1 F1000             ;move up slightly\nG1 X60.0 Z0 E9.0 F1000.0;intro line\nG1 X100.0 E21.5 F1000.0 ;continue line\nG92 E0                  ;zero the extruded length again\n; -- end of START GCODE --",
    "end_gcode": "; -- END GCODE --\nM104 S0                 ;turn off nozzle heater\nM140 S0                 ;turn off bed heater\nG91                     ;set to relative positioning\nG1 E-10 F300            ;retract the filament slightly\nG90                     ;set to absolute positioning\nG28 X0                  ;move to the X-axis origin (Home)\nG0 Y280 F600            ;bring the bed to the front for easy print removal\nM84                     ;turn off stepper motors\n; -- end of END GCODE --",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 40,
    "travel_speed": 120,
    "dia_feed": 1.75,
    "build_volume_x": 300,
    "build_volume_y": 300,
    "build_volume_z": 320,
}
