import os
import sys

JPGList=open('CollectedJPG', 'r')
PNGList=open('CollectedPNG', 'r')
JPGString=list(JPGList)
PNGString=list(PNGList)

JPGList.close()
PNGList.close()

JPGOutput=[]
for JPGFile in JPGString:
	JPGDir=list(JPGFile)
	Counter=len(JPGFile)-1
	Switch='false'
	while Switch=='false':
		Symbol=JPGDir[Counter]
		if not Symbol=='/':
			del JPGDir[Counter]
			Counter=Counter-1
		else:
			del JPGDir[Counter]
			Switch='true'
	JPGFile=''.join(JPGDir)
	JPGOutput.append(JPGFile)	
	
JPGFinalDir=list(dict.fromkeys(JPGOutput))

PNGOutput=[]
for PNGFile in PNGString:
	PNGDir=list(PNGFile)
	Counter=len(PNGFile)-1
	Switch='false'
	while Switch=='false':
		Symbol=PNGDir[Counter]
		if not Symbol=='/':
			del PNGDir[Counter]
			Counter=Counter-1
		else:
			del PNGDir[Counter]
			Switch='true'
	PNGFile=''.join(PNGDir)
	PNGOutput.append(PNGFile)

PNGFinalDir=list(dict.fromkeys(PNGOutput))

for JPGWord in JPGFinalDir:
#	ShellCommand='mkdir ' + JPGWord + '/JpgBak'
#	os.system(ShellCommand)
#	ShellCommand='cp ' + JPGWord + '/' +'*.jpg ' + JPGWord + '/JpgBak'
#	os.system(ShellCommand)
	ShellCommand='jpegoptim ' + JPGWord + '/*.jpg'
	os.system(ShellCommand)

for PNGWord in PNGFinalDir:
#	ShellCommand='mkdir ' + PNGWord + '/PngBak'
#	os.system(ShellCommand)
#	ShellCommand='cp ' + JPGWord + '/' +'*.png ' + JPGWord + '/PngBak'
	os.system(ShellCommand)
	ShellCommand='optipng ' + JPGWord + '/*.png'
	os.system(ShellCommand)


