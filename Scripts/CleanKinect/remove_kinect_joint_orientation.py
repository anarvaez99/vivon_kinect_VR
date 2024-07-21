import json

# Define the input and output file paths
input_file_path = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/right_kinect_frame_timestamps.json'
output_file_path = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/KinectRight/right_kinect_frame_noorientation.json'

# Read the JSON data from the input file
with open(input_file_path, 'r') as input_file:
    json_data = json.load(input_file)

# Remove joint_orientations
for frame in json_data['frames']:
    for body in frame['bodies']:
        if 'joint_orientations' in body:
            del body['joint_orientations']

# Write the modified JSON data to the output file
with open(output_file_path, 'w') as output_file:
    json.dump(json_data, output_file, indent=4)

print(f"Modified JSON data has been written to {output_file_path}")
