import viconnexusapi
from viconnexusapi import ViconNexus, NexusForcePlate
import re
import os

log_separator = "=============================================================================================================================="

def DisplayTrialInfo(vicon):
    # general trial information
    (path, name) = vicon.GetTrialName()
    framecount = vicon.GetFrameCount()
    framerate = vicon.GetFrameRate()
    (startFrame, endFrame) = vicon.GetTrialRange()

    # list the currently loaded subjects
    Subjects = vicon.GetSubjectNames()

    # list of devices
    device_info = []
    deviceIDs = vicon.GetDeviceIDs()
    if len(deviceIDs) > 0:
        for deviceID in deviceIDs:
            deviceDetails = vicon.GetDeviceDetails(deviceID)
            deviceName = deviceDetails[0]
            deviceType = deviceDetails[1]
            deviceRate = deviceDetails[2]
            device_info.append((deviceID, deviceName, deviceType, deviceRate))
    
    return {
        "name": name,
        "path": path,
        "frame_count": framecount,
        "frame_rate": framerate,
        "start_frame": startFrame,
        "end_frame": endFrame,
        "subjects": Subjects,
        "devices": device_info
    }

def StartStopStamps(vicon):
    SessionLoc = vicon.GetTrialName()[0]
    XCPTrialName = SessionLoc + vicon.GetTrialName()[1] + ".xcp"
    startTime = r"(?<=Capture).*?(?<=START_TIME=\")(.*?)(?=\")"
    endTime = r"(?<=Capture).*?(?<=END_TIME=\")(.*?)(?=\")"
    with open(XCPTrialName) as xcpfile:
        xcpfilestring = xcpfile.read()
    startTimeValue = re.findall(startTime, xcpfilestring, re.MULTILINE)[0]
    endTimeValue = re.findall(endTime, xcpfilestring, re.MULTILINE)[0]

    return {
        "start_time": startTimeValue,
        "end_time": endTimeValue
    }

def save_to_txt(trial_info, start_stop_info, filename="trial_info.txt"):
    with open(filename, mode='w') as file:
        # Write trial information
        file.write(f"Name: {trial_info['name']}\n")
        file.write(f"Path: {trial_info['path']}\n")
        file.write(f"Frame Count: {trial_info['frame_count']}\n")
        file.write(f"Frame Rate: {trial_info['frame_rate']}\n")
        file.write(f"Start Frame: {trial_info['start_frame']}\n")
        file.write(f"End Frame: {trial_info['end_frame']}\n")
        file.write(f"Subjects: {', '.join(trial_info['subjects'])}\n")
        file.write("Devices:\n")
        for device in trial_info['devices']:
            file.write(f"  - ID: {device[0]}, Name: {device[1]}, Type: {device[2]}, Rate: {device[3]}\n")
        
        # Write start/stop information
        file.write(log_separator + "\n")
        file.write(f"Start Time: {start_stop_info['start_time']}\n")
        file.write(f"End Time: {start_stop_info['end_time']}\n")
        file.write(log_separator + "\n")
    
    return os.path.abspath(filename)

if __name__ == "__main__":
    vicon = ViconNexus.ViconNexus()
    
    trial_info = DisplayTrialInfo(vicon)
    start_stop_info = StartStopStamps(vicon)
    
    file_path = save_to_txt(trial_info, start_stop_info)
    
    print(f"Text file saved successfully at {file_path}.")
