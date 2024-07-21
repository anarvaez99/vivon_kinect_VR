import json

# Load the JSON data
with open('C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/output_results.json', 'r') as f:
    data = json.load(f)

# Read the timestamps from the text file and store them in a dictionary
timestamps = {}
with open('C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/frame_timestamps.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(': ')
        frame_id = int(parts[0].split()[1])
        timestamp_local = parts[1]
        timestamps[frame_id] = timestamp_local

# Add the timestamp_local to each frame in the JSON data
for frame in data['frames']:
    frame_id = frame['frame_id']
    if frame_id in timestamps:
        frame['timestamp_local'] = timestamps[frame_id]

# Save the updated JSON data
with open('C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/right_kinect_frame_timestamps.json', 'w') as f:
    json.dump(data, f, indent=4)
