#3D Print Settings Retriever
#Shane O'Brien - @TheShaneOBrien
import datetime

date = datetime.datetime.now()

#Strings we need to identify settings in the gCode file
s3dKeyword = "Simplify3D"
primaryExtruderSettingsKeys = ["extruderToolheadNumber", "extruderDiameter", "extruderAutoWidth", 
	"extruderWidth", "extrusionMultiplier", "extruderUseRetract", "extruderRetractionDistance", "extruderExtraRestartDistance", 
	"extruderRetractionZLift", "extruderRetractionSpeed", "extruderUseCoasting", "extruderCoastingDistance", "extruderUseWipe", 
	"extruderWipeDistance"]

#Strings we need to key the new profile
primaryExtruderProfileKeys = ["toolheadNumber", "diameter", "autoWidth", "width", "extrusionMultiplier", "useRetract", 
	"retractionDistance", "extraRestartDistance", "retractionZLift", "retractionSpeed", "useCoasting", "coastingDistance", 
	"useWipe", "wipeDistance"]
temperatureControllerKeys = ["temperatureNumber", "isHeatedBed", "relayBetweenLayers", "relayBetweenLoops", 
	"stabilizeAtStartup", "setpoint"]
fanSpeedKeys = ["setpoint"]

fileToRead = input("Drag the gCode you wish to extract settings from into the window\ngCode to load: ")
saveProfileAs = input("Enter a name for your retrieved profile eg: GoodSettings\nBe careful as we will overwrite existing files\nSave profile as: ")

#Our empty dictionaries where our found settings will go, used to populate the XML profile
foundSettings = {}
primaryExtruderSettings = {}

def ReadS3dSettings():
	#TODO: Error Handling
	gcodeFile = open(fileToRead, "rt")
	#Get all the s3d settings from the comments, they are always at the start of the file
	if gcodeFile.readline().find(s3dKeyword) != -1:
		for x in gcodeFile.readlines():
			currentLine = x
			if currentLine:
				if currentLine.startswith(";"):
					#Actual Settings on S3D Files start with ";   "
					if currentLine.find(";   ") != -1:
						#remove the first 4 characters at the start ";    " and remove the line break at the end
						#not good for gcode settings
						setting = currentLine[4:-1].split(",")
						if len(setting) > 1:
							foundSettings.update({setting[0]: setting[1]})
							#print(setting[0] + "|" +setting[1])
				else:
					break
	gcodeFile.close()
	print("All Settings Found")

#Set aside up nested settings
#TODO: Handle multiple extruders
def GetPrimaryExtruder():
	#Primary Extruder
	primaryExtruderSettings.update({"name" : foundSettings["extruderName"]})
	keyCount = 0
	for x in primaryExtruderSettingsKeys:
		primaryExtruderSettings.update({primaryExtruderProfileKeys[keyCount] : foundSettings[x]})
		print({primaryExtruderProfileKeys[keyCount] : foundSettings[x]})
		foundSettings.pop(x)
		keyCount = keyCount + 1
	print("Primary Extruder Found")

#TODO:
def GetTemperatureSettings():
	print("Temp Settings Not Implemented")

#TODO:
def GetFanSpeeds():
	print("Fan Speeds Not Implemented")

def CreateNewProfile():
	#TODO: Error Handling
	#Generate new profile file
	newProfile = open(saveProfileAs + ".fff", "w")

	newProfile.write('<?xml version="1.0"?>\n')
	newProfile.write('<profile name="' + foundSettings["processName"] + '" version="' + date.strftime('%c') +'" app="3dretrieve">\n')
	#add the none nested settings
	for x in foundSettings:
		newProfile.write('  <' + x + '>' + foundSettings[x] + '</' + x + '>\n')
	#nested settings
	#extruders
	newProfile.write('  <extruder name="' + primaryExtruderSettings["name"] + '">\n')
	primaryExtruderSettings.pop("name")
	for x in primaryExtruderSettings:
		newProfile.write('    <' + x + '>' + primaryExtruderSettings[x] + '</' + x + '>\n')
	newProfile.write('  </extruder>\n')
	#end profile
	newProfile.write('</profile>\n')

	newProfile.close()
	print("New Profile Ready")

#Program Flow
ReadS3dSettings()
GetPrimaryExtruder()
GetTemperatureSettings()
GetFanSpeeds()
CreateNewProfile()