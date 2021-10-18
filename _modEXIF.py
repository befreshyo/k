import os # Standard Library OS functions
from classLogging import _ForensicLog # Logging Class

# import the Python Image Library
# along with TAGS and GPS related TAGS
from PIL import Image
from PIL.EXIFTags import TAGS, GPSTAGS

try:
    pilImage = Image.open(fileName) 
    EXIFData = pilImage._getEXIF()
except Exception:
    # If exception occurs from PIL processing # Report the
    return None, None

    
# Iterate through the EXIFData 
# Searching for GPS Tags

imageTimeStamp = "NA" CameraModel = "NA" CameraMake = "NA"
if EXIFData:
    for tag, theValue in EXIFData.items():
        # obtain the tag
        tagValue = TAGS.get(tag, tag)
        # Collect basic image data if available
        if tagValue =='DateTimeOriginal': 
            imageTimeStamp = EXIFData.get(tag)
        if tagValue == "Make":
            cameraMake = EXIFData.get(tag)
        if tagValue =='Model':
            cameraModel = EXIFData.get(tag)
        # check the tag for GPS
        if tagValue == "GPSInfo":
            # Found it !
            # Now create a Dictionary to hold the GPS Data
            gpsDictionary = {}
            # Loop through the GPS Information
            for curTag in theValue:
                gpsTag = GPSTAGS.get(curTag, curTag)
                gpsDictionary[gpsTag] = theValue[curTag]
    basicExifData = [imageTimeStamp, cameraMake, cameraModel]    
    return gpsDictionary, basicExifData
else:
    return None, None