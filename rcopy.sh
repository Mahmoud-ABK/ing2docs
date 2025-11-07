#!/bin/bash

# Copy BigData shared folder to local folder
rclone copy "gdrive:BigData_ING2_2025" ./bases_de_donnees_nosql_et_big_data \
    --drive-shared-with-me --ignore-existing --progress

# Copy Design Pattern shared folder to local folder
rclone copy "gdrive:Cours DP-ING2-GL" ./design_pattern_et_conception_par_contrats \
    --drive-shared-with-me --ignore-existing --progress

