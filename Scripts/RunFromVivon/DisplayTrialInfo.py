import viconnexusapi
from viconnexusapi import ViconNexus, NexusForcePlate

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 DisplayTrialInfo will display general trial information.

 Input
     vicon    = instance of a Vicon sdk object

 Usage Example: 

    vicon = ViconNexus();
    DisplayTrialInfo(vicon);
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def DisplayTrialInfo(vicon):
  # general trial information
  (path, name) = vicon.GetTrialName()
  framecount = vicon.GetFrameCount()
  framerate = vicon.GetFrameRate()
  (startFrame, endFrame) = vicon.GetTrialRange()

  print ("Name: "+ name)
  print ("Path: "+ path)
  print ("Frame Count: " + str(framecount))
  print ("Rate: " + str(framerate))
  print ("Updatable Frame Range: " + str(startFrame) + "-" + str(endFrame))

  # list the currently loaded subjects
  Subjects = vicon.GetSubjectNames()
  print (Subjects)

  # list of devices
  deviceIDs = vicon.GetDeviceIDs()
  if( len(deviceIDs) > 0 ):
    for deviceID in deviceIDs:
      deviceDetails = vicon.GetDeviceDetails( deviceID )
      deviceName = deviceDetails[0]
      deviceType = deviceDetails[1]
      deviceRate = deviceDetails[2]
      print ("Device ID: "+ str(deviceID)+ " Name: ["+ deviceName+ "] is of type "+ deviceType+ " running at a rate of "+ str(deviceRate))
  
if __name__ == "__main__":
    vicon = ViconNexus.ViconNexus()
    DisplayTrialInfo(vicon) 
  


