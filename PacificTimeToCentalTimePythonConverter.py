#!/usr/bin/python

print("This program converts Pacific Standard Time to Central Standard Time.")

timeOfDay = 501

#ensures the value entered is an int so the conversion can be completed
timeOfDay = int(timeOfDay)

amOrPmChoice = 501

#ensures the value entered is a string so it is readable as such
amOrPmChoice = int(amOrPmChoice)

retryCheck = 501

retryCheck = int(retryCheck)

centralTime = 501

centralTime = int(centralTime)

militaryTime = 501

militaryTime = int(militaryTime)

amOrPmFinal = "501"

amOrPmFinal = str(amOrPmFinal)

amOrPmChoiceText = "AM"

amOrPmChoiceText = str(amOrPmChoiceText)

def getUserEntry():
	global timeOfDay
	global amOrPmChoice
	global amOrPmChoiceText
	
	#while True:
		#gets user input on the time
	timeOfDay = input("Please enter the time you would like converted: ")
		#if timeOfDay.() not in ('1', '2', '3','4','5','6','7','8','9','10','11','12'):
			#print("I'm sorry, please enter a valid time.")
		#else:
			#break

	#gets user input on AM or PM to convert the number to military standard time and back again
	amOrPmChoice = input("Enter 1 for AM: \nEnter 2 for PM: \nYour entry: ")
	
	if amOrPmChoice == 1:
		amOrPmChoiceText = "AM"
	elif amOrPmChoice == 2:
		amOrPmChoiceText = "PM"
	if retryCheck == 0:
		return
	elif retryCheck == 1:
		verifyCorrectInfo()
	
def verifyCorrectInfo():
	global retryCheck 
	global timeOfDay
	global amOrPmChoice
	global amOrPmChoiceText
	
	print("")
	print ("You entered:", timeOfDay, amOrPmChoiceText)
	print("")
	correctEntryCheck = input("Enter 1 if this is correct.\nEnter 2 if you'd like to retry.\nYour entry: ")
	
	correctEntryCheck = int(correctEntryCheck)
	
	print("")
	if correctEntryCheck == 1:
		print("Thank you!")
	elif correctEntryCheck == 2:
		print("Please re-enter the information again")
		retryCheck = 1
		getUserEntry()
	else:
		print("Please choose a valid option")
		verifyCorrectInfo()

def convertToCorrectAndMilitaryTime():
	global timeOfDay
	global amOrPmChoice
	global militaryTime
	
	if amOrPmChoice == 1:
		militaryTime = timeOfDay + 2
	elif amOrPmChoice == 2:
		militaryTime = timeOfDay + 14
	return
	
def convertBackToCentralTime():
	global militaryTime
	global centralTime
	global amOrPmFinal
	
	#for morning numbers 1 through 11 (not 12)
	if militaryTime <= 11:
		centralTime = militaryTime
		amOrPmFinal = "AM"
	#for 12 AM
	elif militaryTime == 14:
		centralTime = militaryTime - 12
		amOrPmFinal = "AM"
	#for afternoon numbers 1 through 10 (not 12)
	elif militaryTime >= 13 and militaryTime <= 23:
		centralTime	= militaryTime - 12
		amOrPmFinal = "PM"
	#for 10 AM
	elif militaryTime == 12:
		centralTime = militaryTime
		amOrPmFinal = "PM"
	#for 10 PM
	elif militaryTime == 24:
		centralTime = militaryTime - 12
		amOrPmFinal = "AM"
	#for 11 PM
	elif militaryTime == 25:
		centralTime = militaryTime - 24
		amOrPmFinal = "AM"
	#for 12 PM
	elif militaryTime == 26:
		centralTime = militaryTime - 24
		amOrPmFinal = "PM"
	
def printFinalConversion():
	global amOrPmChoice
	global amOrPmChoiceText
	global centralTime
	global amOrPmFinal
	
	if amOrPmChoice == 1:
		amOrPmChoiceText = "AM"
	elif amOrPmChoice == 2:
		amOrPmChoiceText = "PM"
		
	print ("You entered", timeOfDay, amOrPmChoiceText, "Pacific Standard Time, which is", centralTime,  amOrPmFinal, "in Central Standard Time")

getUserEntry()
verifyCorrectInfo()
convertToCorrectAndMilitaryTime()
convertBackToCentralTime()
printFinalConversion()
