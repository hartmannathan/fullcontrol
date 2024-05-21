default_initial_settings = {
    "name": "Lulzbot Mini 2 | SL | 0.25 mm (Micro)",
    "manufacturer": "Fargo Additive Manufacturing Equipment 3D, LLC",
    "start_gcode": "; This G-Code has been generated specifically for the Lulzbot Mini 2 with SL 0.25 mm toolhead\nM73 P0 ; clear GLCD progress bar\nM75 ; start GLCD timer\nG26 ; clear potential 'probe fail' condition\nM107 ; disable fans\nM420 S0 ; disable leveling matrix\nG90 ; absolute positioning\nM82 ; set extruder to absolute mode\nG92 E0 ; set extruder position to 0\nM140 S{data['bed_temp']} ; start bed heating up\nG28 ; home all axes\nG0 X0 Y187 Z156 F200 ; move away from endstops\nM117 Mini 2 Wiping... ; progress indicator message on LCD\nM109 R{150} ; soften material before retraction\nG1 E-15 F75 ; retract filament\nG1 X45 Y176 F11520 ; move above wiper pad\nG1 Z0 F1200 ; push nozzle into wiper\nG1 X45 Y178 Z-.5 F4000 ; wiping\nG1 X55 Y176 Z-.5 F4000 ; wiping\nG1 X45 Y177 Z0 F4000 ; wiping\nG1 X55 Y176 F4000 ; wiping\nG1 X45 Y178 F4000 ; wiping\nG1 X55 Y176 F4000 ; wiping\nG1 X45 Y178 F4000 ; wiping\nG1 X55 Y176 F4000 ; wiping\nG1 X60 Y178 F4000 ; wiping\nG1 X80 Y176 F4000 ; wiping\nG1 X60 Y178 F4000 ; wiping\nG1 X80 Y176 F4000 ; wiping\nG1 X60 Y178 F4000 ; wiping\nG1 X90 Y176 F4000 ; wiping\nG1 X80 Y178 F4000 ; wiping\nG1 X100 Y176 F4000 ; wiping\nG1 X80 Y178 F4000 ; wiping\nG1 X100 Y176 F4000 ; wiping\nG1 X80 Y178 F4000 ; wiping\nG1 X100 Y176 F4000 ; wiping\nG1 X110 Y178 F4000 ; wiping\nG1 X100 Y176 F4000 ; wiping\nG1 X110 Y178 F4000 ; wiping\nG1 X100 Y176 F4000 ; wiping\nG1 X110 Y178 F4000 ; wiping\nG1 X115 Y176 Z-0.5 F1000 ; wiping\nG1 Z10 ; raise extruder\nG28 X0 Y0 ; home X and Y\nM204 S300 ; set probing acceleration\nG29 ; start auto-leveling sequence\nM420 S1 ; enable leveling matrix\nM425 Z ; use measured Z backlash for compensation\nM425 Z F0 ; turn off measured Z backlash compensation by default\nM204 S2000 ; restore standard acceleration\nG1 X5 Y15 Z10 F5000 ; move up off last probe point\nG4 S1 ; pause\nM400 ; wait for moves to finish\nM117 Heating... ; progress indicator message on LCD\nM109 R{data['nozzle_temp']} ; wait for extruder to reach initial printing temp\nM190 R{data['bed_temp']} ; wait for bed to reach printing temp\nG1 Z2 E0 F75 ; prime tiny bit of filament into the nozzle\nM117 Mini 2 Printing... ; progress indicator message on LCD\n",
    "end_gcode": "; part removal temp is hardcoded to 45\nM400 ; wait for moves to finish\nM140 S45 ; start bed cooling\nM104 S0 ; disable hotend\nM107 ; disable fans\nG92 E5 ; set extruder to 5mm for retract on print end\nM117 Cooling please wait ; progress indicator message on LCD\nG1 X5 Y5 Z183 E0 F3000 ; move to cooling position\nG1 E5 ; re-prime extruder\nM190 R45 ; wait for bed to cool down to removal temp\nG1 X145 F1000 ; move extruder out of the way\nG1 Y175 F1000 ; present finished print\nM140 S0 ; cool down\nM77 ; end LCD print timer\nG90 ; absolute positioning\nM18 X Y E ; turn off X Y and E axis\nM117 Print Complete. ; print complete message\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 162,
    "build_volume_y": 162,
    "build_volume_z": 180,
}
