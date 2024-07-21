import pandas as pd
from datetime import datetime, timedelta

# Paths to the CSV and text files
csv_path = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/Vicon/wk_of_cf_00.csv'
txt_path = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/Vicon/trial_info.txt'

# Read the CSV file with all headers
with open(csv_path, 'r') as file:
    headers = [next(file).strip() for _ in range(4)]  # Read the first 4 lines for headers

# Load the CSV data into a DataFrame skipping the first 4 rows
df = pd.read_csv(csv_path, skiprows=4)

# Read the text file and extract metadata
with open(txt_path, 'r') as file:
    lines = file.readlines()

# Extract necessary metadata
start_time_str = lines[9].split(": ", 1)[1].strip()  # Assuming the start time is on the 9th line
end_time_str = lines[10].split(": ", 1)[1].strip()  # Assuming the end time is on the 10th line
frame_count = int(lines[2].split(": ", 1)[1].strip())  # Assuming the frame count is on the 3rd line
frame_rate = float(lines[3].split(": ", 1)[1].strip())  # Assuming the frame rate is on the 4th line

# Remove the 'DST' part from the datetime strings
start_time_str = start_time_str.replace(' DST', '')
end_time_str = end_time_str.replace(' DST', '')

# Convert start and end time to datetime objects
start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S.%f')
end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S.%f')

# Calculate the time difference per frame
time_per_frame = (end_time - start_time) / (frame_count - 1)

# Generate the timestamp for each frame
timestamps = [start_time + i * time_per_frame for i in range(frame_count)]

# Add the timestamp column to the DataFrame
df['Timestamp'] = timestamps[:len(df)]

# Modify the fourth header line to include 'Timestamp'
headers[3] += ',Timestamp'

# Save the updated DataFrame back to a CSV file with the original headers
output_csv_path = 'C:/Users/Vicon-OEM/Desktop/KinectViconMatching/Session1-20240718-203605/Vicon/vicon_frame_timestamp.csv'
with open(output_csv_path, 'w', newline='') as file:
    for header in headers:
        file.write(header + '\n')
    df.to_csv(file, index=False)
