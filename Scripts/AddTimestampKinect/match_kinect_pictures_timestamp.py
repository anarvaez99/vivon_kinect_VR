import os
import re

# Define the paths to the folders and the timestamp file
color_folder = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/color'
infrared_folder = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/infrared'
timestamp_file = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/frame_timestamps.txt'

# Read timestamps from the text file
timestamps = {}
with open(timestamp_file, 'r') as file:
    for line in file:
        match = re.match(r'Frame (\d+): (.+)', line)
        if match:
            frame_number = int(match.group(1))
            timestamp = match.group(2).replace(':', '').replace('.', '')
            timestamps[frame_number] = timestamp

# Rename color images
for filename in os.listdir(color_folder):
    match = re.match(r'color_frame_(\d+).(jpg|png|jpeg)', filename)
    if match:
        frame_number = int(match.group(1))
        ext = match.group(2)
        new_name = f'color_frame_{frame_number:04d}.{ext}'
        if frame_number in timestamps:
            new_name = f'color_{timestamps[frame_number]}.{ext}'
        os.rename(os.path.join(color_folder, filename), os.path.join(color_folder, new_name))

# Rename infrared images
for filename in os.listdir(infrared_folder):
    match = re.match(r'ir_frame_(\d+).(jpg|png|jpeg)', filename)
    if match:
        frame_number = int(match.group(1))
        ext = match.group(2)
        new_name = f'ir_frame_{frame_number:04d}.{ext}'
        if frame_number in timestamps:
            new_name = f'ir_{timestamps[frame_number]}.{ext}'
        os.rename(os.path.join(infrared_folder, filename), os.path.join(infrared_folder, new_name))

print("Renaming completed.")
