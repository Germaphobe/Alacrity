#Import
import os.path
import random
import time
from tkinter import *
import sys

#Checks if it's the users first time (see if their averages have been made)
if (os.path.isfile("SavedName.py")) == True:
	from SavedName import*
	
	#Check for SavedMath.py
	try:
		from SavedMath import*
	except ImportError:
		f=open("SavedMath.py", "w")
		f.close()
		
	#Check for SavedEnglish.py
	try:
		from SavedEnglish import*
	except ImportError:
		f=open("SavedEnglish.py", "w")
		f.close()

	#Check for SavedScience.py
	try:
		from SavedScience import*
	except ImportError:
		f=open("SavedScience.py", "w")
		f.close()

	#Check for SavedHistory.py
	try:
		from SavedHistory import*
	except ImportError:
		f=open("SavedHistory.py", "w")
		f.close()

	#Check for SavedCs.py
	try:
		from SavedCs import*
	except ImportError:
		f=open("SavedCs.py", "w")
		f.close()

	print("Welcome back, " + name + ", to Alacrity.")
	print(("The purpose of this program is to calculate how long it will take you to complete your homework based on your current knowledge of the subject of your choice. No more procrastinating!"))

#First time user
else:
	#opening welcome message
	print("Welcome to Alacrity")
	print(("The purpose of this program is to calculate how long it will take you to complete your homework based on your current knowledge of the subject of your choice. No more procrastinating!"))

#Re-run the program with different subject
completedSubjects=[]
rerun=1
while rerun==1:
	
	#Used app before
	if (os.path.isfile("SavedName.py")) == True:
	#What does the old user want to do
		rerun=1
		while rerun==1:
			#Validates entry
			possibleOptions=["calculate homework time","time","re-take quiz","quiz", "change name","name","quit app","quit"]
			optionLength=len(possibleOptions)
			counter=0
			invalid=1
			while invalid==1:
				UserPick=str(input("\nWould you like to: calculate homework time (time), re-take quiz (quiz) or change name (name) or quit app (quit)?\nYour choice: ")).lower()
				while counter<optionLength:
					if UserPick==possibleOptions[counter]:
						invalid=0
					counter=counter+1
				if invalid==1:
					print("\nInvalid option")
					print("Valid options:",possibleOptions)
				counter=0
			
			#Calculates Homework Time
			if UserPick=="calculate homework time" or UserPick =="time":
				
				#Validates entry
				possibleSubjects=["math","english","history","science", "computer science"]
				subjectLength=len(possibleSubjects)
				counter=0
				invalid=1
				while invalid==1:
					print("\nSubjects:",possibleSubjects)
					CalculateSubject=str(input("\nWhat subject do you want to calculate homework for? "))
					subject=CalculateSubject.lower()
					while counter<subjectLength:
						if subject==possibleSubjects[counter]:
							invalid=0
						counter=counter+1
					if invalid==1:
						print("\nInvalid option")
						print("Please Try again")
					counter=0
					#Gets their average time for that subject, anld makes sure it exists
				def doesAverageExist(average):
					if (average) in globals():
						questions=int(input("\nHow many questions do you have (sub questions count too) "))
						Avg=globals()[average]*questions
						secs = int(Avg % 60)
						mins = int((Avg-secs) // 60)
						hours = int((Avg // 60) // 60)

						Hmwktime = (str(hours) + 'hrs : ' + str(mins) + 'mins : ' + str(secs) + 's')
						return (Hmwktime)
			
				if CalculateSubject == "math" and ("MathAvgTime") in globals():
					print("\nIt will take you",doesAverageExist("MathAvgTime"))
				elif CalculateSubject == "english" and ("EnglishAvgTime") in globals():
					print("\nIt will take you",doesAverageExist("EnglishAvgTime"))
				elif CalculateSubject == "history" and ("HistoryAvgTime") in globals():
					print("\nIt will take you",doesAverageExist("HistoryAvgTime"))
				elif CalculateSubject == "science" and ("ScienceAvgTime") in globals():
					print("\nIt will take you",doesAverageExist("ScienceAvgTime"))
				elif CalculateSubject == "computer science" and ("CSAvgTime") in globals():
					print("\nIt will take you",doesAverageExist("CSAvgTime"))
				else:
					print("\nYou haven't done the quiz yet for this subject, we can't calculate the average")
				
			#Changes the users name
			if UserPick=="change name" or UserPick=="name":
				name=(input("\nPlease enter your new name: "))
				f=open("SavedName.py", "w")
				f.write("\n""name = " +"'"+(name)+"'"+"\n")
				f.close()
				print("I will call you " + name +" from now on")
				Quit=input("would you like to quit now? (Y/N)").lower()
				if Quit=="y":
					sys.exit()
			
			#Lets the user re-take a quiz
			if UserPick=="re-take quiz" or UserPick=="quiz":
				rerun=0
				quiz=1
			
			#quits app
			if UserPick=="quit" or UserPick=="quit app":
				sys.exit()
	
	#asks for name and saves it
	if (os.path.isfile("SavedName.py")) == False:
		name=(input("\nPlease enter your name: "))
		f=open("SavedName.py", "w")
		f.write("name = " +"'"+(name)+"'"+"\n")
		f.close()

  #subject selection and valid subject verification
  #Make sure all subjects in the list are lowercase
	possibleSubjects=["math","english","history","science", "computer science"]
	subjectLength=len(possibleSubjects)
	counter=0
	invalid=1
	while invalid==1:
		print("\nSubjects:",possibleSubjects)
		originalSubject=str(input("What subject do you want to test? "))
		subject=originalSubject.lower()
		while counter<subjectLength:
			if subject==possibleSubjects[counter]:
				invalid=0
			counter=counter+1
		if invalid==1:
			print("\nInvalid option")
			print("Please Try again")
		counter=0
	
	#Do they want to see the answers
	invalid=1
	while invalid==1:
		print("\nPlease answer with 'yes' or 'no'")
		seeAnswers=str(input("Would you like to see the answers for incorrect answers? "))
		seeAnswers=seeAnswers.lower()
		if seeAnswers=="yes":
			invalid=0
			showAns=1
		elif seeAnswers=="no":
			invalid=0
			showAns=0
		else:
			print("\nInvalid Answer")
			print("Please enter 'yes' or 'no'")

	#=====================================Questions=====================================
	#Math
	if subject=="math":

		mathPlayAgain = 0

		while mathPlayAgain == 0:

				print("\nYou selected math!")
				correct=0
				total=10
				counter=1
				
				#Starts math Timer
				StartMath=time.time()

				while counter<=10:
					opperator=random.randint(1,4)
					num1=random.randint(1,50)
					num2=random.randint(1,50)

				#Addition
					if opperator==1:
							invalid=1
							while invalid==1:
								addition = num1 + num2
								addAnswer=str(input("\n%d. What is %d + %d: "%(counter,num1,num2)))
								try:
									val = int(addAnswer)
									invalid=0
								except ValueError:
									print("\nInvalid answer")
									print("Please try again")
							addAnswer=int(addAnswer)
							if addAnswer==addition:
								print("\nCorrect")
								correct=correct+1
							else:
								print("\nIncorrect")
								if showAns==1:
									print("The correct answer is:",addition)
							counter=counter+1

				#Subtraction
					elif opperator==2:
							if num1>num2:
								invalid=1
								while invalid==1:
									subtraction1=num1-num2
									subAnswer1=str(input("\n%d. What is %d - %d: "%(counter,num1,num2)))
									try:
										val = int(subAnswer1)
										invalid=0
									except ValueError:
										print("\nInvalid answer")
										print("Please try again")
								subAnswer1=int(subAnswer1)
								if subAnswer1==subtraction1:
									print("\nCorrect")
									correct=correct+1
								else:
									print("\nIncorrect")
									if showAns==1:
										print("The correct answer is:",subtraction1)
							else:
								invalid=1
								while invalid==1:
									subtraction2=num2-num1
									subAnswer2=str(input("\n%d. What is %d - %d: "%(counter,num2,num1)))
									try:
										val = int(subAnswer2)
										invalid=0
									except ValueError:
										print("\nInvalid answer")
										print("Please try again")
								subAnswer2=int(subAnswer2)
								if subAnswer2==subtraction2:
									print("\nCorrect")
									correct=correct+1
								else:
									print("\nIncorrect")
									if showAns==1:
										print("The correct answer is:",subtraction2)
							counter=counter+1

				#Multiplication
					elif opperator==3:
							invalid=1
							while invalid==1:
								multiplication=num1*num2
								multAnswer=str(input("\n%d. What is %d x %d: "%(counter,num1,num2)))
								try:
									val = int(multAnswer)
									invalid=0
								except ValueError:
									print("\nInvalid answer")
									print("Please try again")
							if multAnswer==multiplication:
								print("\nCorrect")
								correct=correct+1
							else:
								print("\nIncorrect")
								if showAns==1:
									print("The correct answer is:",multiplication)
							counter=counter+1

				#Floor Division
					elif opperator==4:
							if num1>num2:
								invalid=1
								while invalid==1:
									div1=num1//num2
									divAnswer1=str(input("\n%d. What is %d // %d: "%(counter,num1,num2)))
									try:
										val = int(divAnswer1)
										invalid=0
									except ValueError:
										print("\nInvalid answer")
										print("Please try again")
								divAnswer1=int(divAnswer1)
								if divAnswer1==div1:
									print("\nCorrect")
									correct=correct+1
								else:
									print("\nIncorrect")
									if showAns==1:
										print("The correct answer is:",div1)
							else:
								invalid=1
								div2=num2//num1
								divAnswer2=str(input("\n%d. What is %d // %d: "%(counter,num2,num1)))
								try:
									val = int(divAnswer2)
									invalid=0
								except ValueError:
									print("\nInvalid answer")
									print("Please try again")
								divAnswer2=int(divAnswer2)
								if divAnswer2==div2:
									print("\nCorrect")
									correct=correct+1
								else:
									print("\nIncorrect")
									if showAns==1:
										print("The correct answer is:",div2)
							counter=counter+1

				#Ends Math stopwatch and gets total average time
				EndMath=time.time()
				mathTime=(EndMath-StartMath)
				MathAvgTime=(mathTime)/10
				f=open("SavedMath.py", "w")
				f.write("\n"+"MathAvgTime = "+str(MathAvgTime)+"\n")
				f.close()
				#Results
				print("\nYou got {}/10 questions correct".format(correct))
				secs = int(mathTime % 60)
				mins = int((mathTime-secs) // 60)
				hours = int((mathTime // 60) // 60)
				print("\nIt took you ", hours,'hrs :',mins,'mins :',secs,'secs')
				avgHours=hours/10
				avgMins=mins/10
				avgSecs=secs/10
				print("\nYou averaged %d hrs : %d mins : %d secs for each question"%(avgHours,avgMins,avgSecs))

				completedSubjects.append("math")
				
				#Asks user if they want to play again.
				invalid=1
				while invalid==1:
					userMathAns=str(input("\nDo you want to try the quiz again (yes or no)\nYour choice: ")).lower()			
					if userMathAns == "no":
						mathPlayAgain=1
						invalid=0
					elif userMathAns == "yes":
						mathPlayAgain=0
						invlaid=0
					else:
						print("\nInvalid option")
						print("Please try again")


	#English Test=========================================================================
	if subject=="english":
		engPlayAgain = 0

		while engPlayAgain == 0:
		
			print("\nYou selected english!")
			print("The following questions will be about Romeo and Juliet")
			
			#Set Category One's Score to 0 because no questions have been answered correctly yet.
			englishScore = 0

			#------------------------
			#Starts English Stopwatch
			StartEnglish=time.time()

			#Question One (Correct Answer = B):
			print("\n1. To which city does Romeo go after being exiled from Verona?")
			print("a) Padua")
			print("b) Mantua")#Correct Answer
			print("c) Venice")
			print("d) None of the above\n")
			#Will Validate User Input:
			while True:
				englishAnswer1 = input("Answer: ").upper()
				if englishAnswer1 == "A" or englishAnswer1 == "B" or englishAnswer1 == "C" or englishAnswer1 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer1 == "B":
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: B) Mantua")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Two (Correct Answer = A):
			print("\n2. Who performs Romeo and Juliet’s marriage?")
			print("a) Friar Lawrence")#Correct Answer
			print("b) Friar Tomas")
			print("c) Friar Vincent")
			print("d) Friar Mateo\n")
			#Will Validate User Input:
			while True:
				englishAnswer2 = input("Answer: ").upper()
				if englishAnswer2 == "A" or englishAnswer2 == "B" or englishAnswer2 == "C" or englishAnswer2 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer2 == "A":
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is A) Friar Lawrence")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Three (Correct Answer = True / A):
			print("\n3. Tybalt kills Mercutio True or False?")
			print("a) True")#Correct Answer
			print("b) False\n")
			#Will Validate User Input:
			while True:
				englishAnswer3 = input("Answer: ").upper()
				if englishAnswer3 == "A" or englishAnswer3 == "B":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer3 == "A":
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is A) True")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Four (Correct Answer = A):
			print("\n4. Which character first persuades Romeo to attend the feast?")
			print("a) Benvolio")#Correct Answer
			print("b) Mercutio")
			print("c) Juliet")
			print("d) None of the above\n")
			#Will Validate User Input:
			while True:
				englishAnswer4 = input("Answer: ").upper()
				if englishAnswer4 == "A" or englishAnswer4 == "B" or englishAnswer4 == "C" or englishAnswer4 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer4 == "A":
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: A) Benvolio")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Five (Correct Answer = False / B):
			print("\n5. Romeo hears a lark the night after their wedding. True or False?")
			print("a) True")
			print("b) False\n")#Correct Answer
			#Will Validate User Input:
			while True:
				englishAnswer5 = input("Answer: ").upper()
				if englishAnswer5 == "A" or englishAnswer5 == "B":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer5 == "B":
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: B) False")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Six (Correct Answer = D):
			print("\n6. To what does Romeo first compare Juliet during the balcony scene?")
			print("a) The silver moon")
			print("b) The stars")
			print("c) A summer's day")
			print("d) The morning sun\n")#Correct Answer
			#Will Validate User Input:
			while True:
				englishAnswer6 = input("Answer: ").upper()
				if englishAnswer6 == "A" or englishAnswer6 == "B" or englishAnswer6 == "C" or englishAnswer6 == "D":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer6 == "D":
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: D) The morning sun")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Seven (Correct Answer = True / A):
			print("\n7. Paris is related to Prince Escalus. True or False?")
			print("a) True")#Correct Answer
			print("b) False\n")

			#Will Validate User Input:
			while True:
				englishAnswer7 = input("Answer: ").upper()
				if englishAnswer7 == "A" or englishAnswer7 == "B":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer7 == "A":  
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: A) True")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again \n")
			#------------------------------------------------------------------

			#Question Eight (Correct Answer = B):
			print("\n8. Who proposes that a gold statue of Juliet be built in Verona?")
			print("a) Romeo")
			print("b) Montague")#Correct Answer
			print("c) Capulet")
			print("d) All of the above\n")
			#Will Validate User Input:
			while True:
				englishAnswer8 = input("Answer: ").upper()
				if englishAnswer8 == "A" or englishAnswer8 == "B" or englishAnswer8 == "C" or englishAnswer8 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if englishAnswer8 == "B":
						("\nCorrect")
						englishScore = englishScore + 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: B) Montague")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Nine (Correct Answer = False / B):
			print("\n9. Romeo is killed with a dagger in Juliet's tomb")
			print("a) True")
			print("b) False\n")#Correct Answer
			#Will Validate User Input:
			while True:
				englishAnswer9 = input("Answer: ").upper()
				if englishAnswer9 == "A" or englishAnswer9 == "B":
					if englishAnswer9 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: B) False")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Ten (Correct Answer = False / B):
			print("\n10. Romeo madly in love for with Juliet for the entirety of the play. True or False?")
			print("a) True")
			print("b) False\n")#Correct Answer
			#Will Validate User Input:
			while True:
				englishAnswer10 = input("Answer: ").upper()
				if englishAnswer10 == "A" or englishAnswer10 == "B":
					if englishAnswer10 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						("\nCorrect")
						englishScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correc answer is: B) False")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")

			#Ends English stopwatch and gets total average time
			EndEnglish=time.time()
			EnglishTime=EndEnglish-StartEnglish
			EnglishAvgTime=(EnglishTime)/10

			#Results
			print("\nYou got {}/10 questions correct".format(englishScore))
			secs = int(EnglishTime % 60)
			mins = int((EnglishTime-secs) // 60)
			hours = int((EnglishTime // 60) // 60)
			print("\nIt took you ", hours,'hrs :',mins,'mins :',secs,'secs')
			avgHours=hours/10
			avgMins=mins/10
			avgSecs=secs/10
			print("\nYou averaged %d hrs : %d mins : %d secs for each question"%(avgHours,avgMins,avgSecs))

			completedSubjects.append("english")

			#Asks user if they want to play again.
			invalid=1
			while invalid==1:
				userEngAns=str(input("\nDo you want to try the quiz again (yes or no)\nYour choice: "))
				if userEngAns == "no":
					engPlayAgain=1
					invlaid=0
				elif userEngAns == "yes":
					engPlayAgain=0
					invalid=0
				else:
					print("\nInvalid option")
					print("Please try again")

	#History Test=========================================================================
	if subject=="history":
		historyPlayAgain = 0

		while historyPlayAgain == 0:
		
			print("\nYou selected history!")

			#Set Category One's Score to 0 because no questions have been answered correctly yet.
			historyScore = 0
			#------------------------

			#Starts History Timer
			StartHistory=time.time()

			#Question One (Correct Answer = B):
			print("\n1. In the 1500s, fur hats became very popular in Europe. This created a huge demand for imported pelts from which hard-working and industrious animal from Canada?")
			print("a) muskrat")
			print("b) beaver")
			print("c) polar bear")
			print("d) arctic fox\n")
			#Will Validate User Input:
			while True:
				historyAnswer1 = input("Answer: ").upper()
				if historyAnswer1 == "A" or historyAnswer1 == "B" or historyAnswer1 == "C" or historyAnswer1 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if historyAnswer1 == "B":
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: B) Beaver")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    
			#------------------------------------------------------------------

			#Question Two (Correct Answer = C):
			print("\n2. Jeanne Sauve was the first Canadian female to hold what important position?")
			print("a) Zamboni driver for the Toronto Maple Leafs Hockey Club")
			print("b) Top car buyer for Prime Minister")#Correct Answer
			print("c) Canada's Governor General")
			print("d) Head Janitor for Canada's House of Parliament\n")
			#Will Validate User Input:
			while True:
				historyAnswer2 = input("Answer: ").upper()
				if historyAnswer2 == "A" or historyAnswer2 == "B" or historyAnswer2 == "C" or historyAnswer2 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if historyAnswer2 == "C":
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: C) Canada's Govenor General")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    
			#------------------------------------------------------------------

			#Question Three (Correct Answer = A):
			print("\n3. This man was Canada's Prime Minister during WWII. What was his name?")
			print("a) William Lyon Mackenzie King")#Correct Answer
			print("b) Terrance Stanley Fox")
			print("c) Gordon Merdith Lightfoot")
			print("d) Gordon Meredith Lightfoot\n")
			#Will Validate User Input:
			while True:
				historyAnswer3 = input("Answer: ").upper()
				if historyAnswer3 == "A" or historyAnswer3 == "B" or historyAnswer3 == "C" or historyAnswer3 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if historyAnswer3 == "A":
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: A) William Lyon Mackenzie King")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    
			#------------------------------------------------------------------

			#Question Four (Correct Answer = C):
			print("\n4. What animal, hunted almost to extinction, was once the main source of food for the Blackfoot Indians of Canada?")
			print("a) Whooping Crane")
			print("b) Leatherback Turtle")
			print("c) Bison")#Correct Answer
			print("d) Sea Otter\n")
			#Will Validate User Input:
			while True:
				historyAnswer4 = input("Answer: ").upper()
				if historyAnswer4 == "A" or historyAnswer4 == "B" or historyAnswer4 == "C" or historyAnswer4 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if historyAnswer4 == "C":
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: C) Bison")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    
			#------------------------------------------------------------------

			#Question Five (Correct Answer = True / D):
			print("\n5. Including the amateur era, which of the following two teams were Canada's first ice hockey teams to win a Stanley Cup Championship?")
			print("a) Toronto Argonauts & Montreal Alouettes")
			print("b) Toronto Raptors & Vancouver Grizzlies")
			print("c) Toronto Blue Jays & Montreal Expos")
			print("d) Winnipeg Victorias & Montreal Hockey Club\n")#Correct Answer
			#Will Validate User Input:
			while True:
				historyAnswer5 = input("Answer: ").upper()
				if historyAnswer5 == "A" or historyAnswer5 == "B" or historyAnswer5 == "C" or historyAnswer5 == "D":
					if historyAnswer5 == "D":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: D) Winnipeg Victorias & Montreal Hockey Club")
					break
				#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    
			#------------------------------------------------------------------

			#Question Six (Correct Answer = C):
			print("\n6. What type of 'footwear,' used specifically for winter travel, was invented by Canada's first native peoples?")
			print("a) toboggan")
			print("b) snowmobile")
			print("c) snowshoes")#Correct Answer
			print("d) dog sled\n")
			#Will Validate User Input:
			while True:
				historyAnswer6 = input("Answer: ").upper()
				if historyAnswer6 == "A" or historyAnswer6 == "B" or historyAnswer6 == "C" or historyAnswer6 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if historyAnswer6 == "C":
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: C) Snowshoes")
					break
					#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    
			#------------------------------------------------------------------

			#Question Seven (Correct Answer = True / A):
			print("\n7. The world-famous Canadian, Rick Hansen, travelled around the world to raise money for spinal cord research. What made this trip extremely difficult?")
			print("a) He completed the trip in a wheelchair")#Correct Answer
			print("b) He became confused and went around the Great Wall of China 3 times")
			print("c) He made the entire trip walking on his hands")
			print("d) He almost drowned swimming across the Alantic and Pacific Oceans\n")
			#Will Validate User Input:
			while True:
				historyAnswer7 = input("Answer: ").upper()
				if historyAnswer7 == "A" or historyAnswer7 == "B" or historyAnswer7 == "C" or historyAnswer7 == "D":
					if historyAnswer7 == "A":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: A) He completed the trip in a wheelchair")
					break
			#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    
			#-----------------------------------------------------------------

			#Question Eight (Correct Answer = D):
			print("\n8. From 1920-1933, weven well known Canadians were known as 'The Group of Seven.' What wass this group famous for doing?")
			print("a) They were a female hockey team who won eight Stanley Cups")
			print("b) They built the CN Tower and Skydome in 1920-1933")
			print("c) They were seven Canadian men who were friends of Adolph Hitler")
			print("d) They were a group of talented landscape painters\n")#Correct Answer
			#Will Validate User Input:
			while True:
				historyAnswer8 = input("Answer: ").upper()
				if historyAnswer8 == "A" or historyAnswer8 == "B" or historyAnswer8 == "C" or historyAnswer8 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if historyAnswer8 == "D":
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: D) They were a group of talented landscape painters")
					break		
			#If Use Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")
			#------------------------------------------------------------------

			#Question Nine (Correct Answer = B):
			print("\n9. The name 'Canada' was taken from the same Iroquois Indian word 'canada.' What does 'canada' mean when translated to English?")
			print("a) bir red leaf")
			print("b) village")#Correct Answer
			print("c) home of Santa Claus")
			print("d) lazy beaver\n")
			#Will Validate User Input:
			while True:
				historyAnswer9 = input("Answer: ").upper()
				if historyAnswer9 == "A" or historyAnswer9 == "B" or historyAnswer9 == "C" or historyAnswer9 == "D":
					#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
					if historyAnswer9 == "B":
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: B) Village")
					break		
			#If Use Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")    #------------------------------------------------------------------
					
			#Question Ten (Correct Answer = B:
			print("\n10. In 1917 during the first world war, a Canadian city was flattened when two ships collided in the harbour, causing a large fire which then caused an enormous explosion. Which city am I talking about?")
			print("a) Whitehorse, Yukon Territories")
			print("b) Halifax, Nova Scotia")#Correct Answer
			print("c) Frederiction, New Brunswick")
			print("d) Winnipeg, Manitoba")
			#Will Validate User Input:
			while True:
				historyAnswer10 = input("Answer: ").upper()
				if historyAnswer10 == "A" or historyAnswer10 == "B" or historyAnswer10 == "C" or historyAnswer10 == "D":
					if historyAnswer10 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						print("\nCorrect")
						historyScore += 1
					else:
						print("\nIncorrect")
						if showAns == 1:
							print("The correct answer is: B) Halifax, Nova Scotia")
					break
				#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
				else:
					print("\nInvalid option")
					print("Please try again\n")

			#Ends History stopwatch and gets total average time
			EndHistory=time.time()
			HistoryTime=StartHistory-EndHistory
			HistoryAvgTime=(HistoryTime)/10

			#Results:
			print("\nYou answered {}/10 questions correctly".format(historyScore))
			secs = int(HistoryTime % 60)
			mins = int((HistoryTime-secs) // 60)
			hours = int((HistoryTime // 60) // 60)
			print("\nIt took you ", hours,'hrs :',mins,'mins :',secs,'secs')
			avgHours=hours/10
			avgMins=mins/10
			avgSecs=secs/10
			print("\nYou averaged %d hrs : %d mins : %d secs for each question"%(avgHours,avgMins,avgSecs))
			completedSubjects.append("history")

			#Asks user if they want to play again.
			invalid=1
			while invalid==1:
				userHistoryAns=str(input("\nDo you want to try the quiz again (yes or no)\nYour choice: ")).lower()
				if userHistoryAns=="yes":
					historyPlayAgain=0
					invalid=0	
				if userHistoryAns == "no":
					historyPlayAgain=1
					invalid=0
				else:
					print("\nInvalid option")
					print("Please try again")

	#Science Test=========================================================================
	if subject=="science":
		sciencePlayAgain = 0

		while sciencePlayAgain == 0:
		
			print("\nYou selected science!")
			#Set Category One's Score to 0 because no questions have been answered correctly yet.
			scienceScore = 0

			#Starts science stopwatch
			StartScience=time.time()
			
			#Too lazy to fix formatting
			if subject=="science":

				#Question One (Correct Answer = A):
				print("\n1. Electric resistance is typically measured in what units?")
				print("a) Ohms")#Correct Answer
				print("b) Amperes")
				print("c) Coulombs")
				print("d) None of the above\n")
				#Will Validate User Input:
				while True:
						scienceAnswer1 = input("Answer: ").upper()
						if scienceAnswer1 == "A" or scienceAnswer1 == "B" or scienceAnswer1 == "C" or scienceAnswer1 == "D":
							#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
								if scienceAnswer1 == "A":
									("\nCorrect")
									scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: A) Ohms")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
						else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Two (Correct Answer = A):
				print("\n2. What orbits the nucleus of an atom?")
				print("a) Electrons")#Correct Answer
				print("b) Neutrons")
				print("c) Protons")
				print("d) All of the above\n")
				#Will Validate User Input:
				while True:
						scienceAnswer2 = input("Answer: ").upper()
						if scienceAnswer2 == "A" or scienceAnswer2 == "B" or scienceAnswer2 == "C" or scienceAnswer2 == "D":
								#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
								if scienceAnswer2 == "A":
									("\nCorrect")
									scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: A) Electrons")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
						else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Three (Correct Answer = Low / B):
				print("\n3. Conductors have high or low resistance?")
				print("a) High")
				print("b) Low\n")#Correct Answer
				#Will Validate User Input:
				while True:
					scienceAnswer3 = input("Answer: ").upper()
					if scienceAnswer3 == "A" or scienceAnswer3 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if scienceAnswer3 == "B":
							("\nCorrect")
							scienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: B) Low")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Four (Correct Answer = C):
				print("\n4. Which famous scientist introduced the idea of natural selection?")
				print("a) Issac Newton")
				print("b) Albert Einstein")
				print("c) Charles Darwin")#Correct Answer
				print("d) None of the above\n")
				#Will Validate User Input:
				while True:
						scienceAnswer4 = input("Answer: ").upper()
						if scienceAnswer4 == "A" or scienceAnswer4 == "B" or scienceAnswer4 == "C" or scienceAnswer4 == "D":
								#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
								if scienceAnswer4 == "C":
									("\nCorrect")
									scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: C) Charles Darwin")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
						else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Five (Correct Answer = True / A):
				print("\n5. DNA is the shortened form of the term ‘Deoxyribonucleic acid’? True or False?")
				print("a) True")#Correct Answer
				print("b) False\n")
				#Will Validate User Input:
				while True:
						scienceAnswer5 = input("Answer: ").upper()
						if scienceAnswer5 == "A" or scienceAnswer5 == "B":
								if scienceAnswer5 == "A":
										#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
										("\nCorrect")
										scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: A) True")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
						else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Six (Correct Answer = D):
				print("\n6. The area of biology devoted to the study of fungi is known as?")
				print("a) Paleontology")
				print("b) Ichtyology")
				print("c) Entomology")
				print("d) Mycology\n")#Correct Answer
				#Will Validate User Input:
				while True:
						scienceAnswer6 = input("Answer: ").upper()
						if scienceAnswer6 == "A" or scienceAnswer6 == "B" or scienceAnswer6 == "C" or scienceAnswer6 == "D":
								#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
								if scienceAnswer6 == "D":
									("\nCorrect")
									scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: D) Mycology")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
						else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Seven (Correct Answer = True / A):
				print("\n7. A neutron has no net electric charge. True or False?")
				print("a) True")#Correct Answer
				print("b) False\n")
				#Will Validate User Input:
				while True:
						scienceAnswer7 = input("Answer: ").upper()
						if scienceAnswer7 == "A" or scienceAnswer7 == "B":
								if scienceAnswer7 == "A":
										#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
										("\nCorrect")
										scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: A) True")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
						else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Eight (Correct Answer = B):
				print("\n8. What is the hottest planet in our solar system?")
				print("a) Earth")
				print("b) Venus")#Correct Answer
				print("c) Mars")
				print("d) Jupiter\n")
				#Will Validate User Input:
				while True:
					scienceAnswer8 = input("Answer: ").upper()
					if scienceAnswer8 == "A" or scienceAnswer8 == "B" or scienceAnswer8 == "C" or scienceAnswer8 == "D":
								#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
								if scienceAnswer8 == "B":
									("\nCorrect")
									scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: B) Venus")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Nine (Correct Answer = False / A):
				print("\n9. Plasma is a state of matter. True or False?")
				print("a) True")#Correct Answer
				print("b) False\n")
				#Will Validate User Input:
				while True:
						scienceAnswer9 = input("Answer: ").upper()
						if scienceAnswer9 == "A" or scienceAnswer9 == "B":
								if scienceAnswer9 == "A":
									#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
									("\nCorrect")
									scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: A) True")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
						else:
							print("\nInvalid option")
							print("Please try again\n")
				#------------------------------------------------------------------

				#Question Ten (Correct Answer = True / B:
				print("\n10. Bases have a pH level below 7. True or False?")
				print("a) True")
				print("b) False\n")#Correct Answer
				#Will Validate User Input:
				while True:
					scienceAnswer10 = input("Answer: ").upper()
					if scienceAnswer10 == "A" or scienceAnswer10 == "B":
								if scienceAnswer10 == "B":
									#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
									("\nCorrect")
									scienceScore += 1
								else:
									print("\nIncorrect")
									if showAns == 1:
										print("The correct answer is: B) False")
								break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
							print("\nInvalid option")
							print("Pleas try again\n")
				
				#End science Timer
				EndScience=time.time()

				#Final Time
				ScienceTime=EndScience-StartScience
				ScienceAvgTime=(ScienceTime)/10

				#Results:
				print("\nYou answered {}/10 questions correctly".format(scienceScore))
				secs = int(ScienceTime % 60)
				mins = int((ScienceTime-secs) // 60)
				hours = int((ScienceTime // 60) // 60)
				print("\nIt took you ", hours,'hrs :',mins,'mins :',secs,'secs')
				avgHours=hours/10
				avgMins=mins/10
				avgSecs=secs/10
				print("\nYou averaged %d hrs : %d mins : %d secs for each question"%(avgHours,avgMins,avgSecs))
				completedSubjects.append("science")

				#Asks user if they want to play again.
				invalid=1
				while invalid==1:
					userScienceAns=str(input("\nDo you want to try the quiz again (yes or no)\nYour choice: ")).lower()
					if userScienceAns=="yes":
						sciencePlayAgain=0
						invlaid=0
					elif userScienceAns == "no":
						sciencePlayAgain=1
						invalid=0
					else:
						print("\nInvalid option")
						print("Please try again")

  #Computer Science Test================================================================
	if subject=="computer science":
		computerSciencePlayAgain = 0

		while computerSciencePlayAgain == 0:
		
			print("\nYou selected computer science!")
			
			#I removed define function and was too lazy to fix indentation so i just added another if statement to fix it :)
			if subject=="computer science":
			#-------------------------
				computerScienceScore = 0

				#Starts Stopwatch
				StartCS=time.time()

				#Question One (Correct Answer = True / A):
				print("1. A network is a system or group of interconnected beings or things. True or False?")
				print("a) True")#Correct Answer
				print("b) False\n")
				#Will Validate User Input:
				while True:
					computerScienceAnswer1 = input("Answer: ").upper()
					if computerScienceAnswer1 == "A" or computerScienceAnswer1 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer1 == "A":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: A) True")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again")
				#------------------------------------------------------------------

				#Question Two (Correct Answer = C):
				print("\n2. What is the basic storage unit on a portable device?")
				print("a) Byte ")
				print("b) Megabyte")
				print("c) Bit")#Correct Answer
				print("d) Geopbyte\n")
				#Will Validate User Input:
				while True:
					computerScienceAnswer2 = input("Answer: ").upper()
					if computerScienceAnswer2 == "A" or computerScienceAnswer2 == "B" or computerScienceAnswer2 == "C" or computerScienceAnswer2 == "D":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer2 == "C":
							print("\nCorrect")
							computerScienceScore = computerScienceScore + 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: C) Bits")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Three (Correct Answer = True / A):
				print("\n3. Before the 20th century, calculations were performed by humans. True or False?")
				print("a) True")#Correct Answer
				print("b) False\n")
				#Will Validate User Input:
				while True:
					computerScienceAnswer3 = input("Answer: ").upper()
					if computerScienceAnswer3 == "A" or computerScienceAnswer3 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer3 == "A":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: A) True")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Four (Correct Answer = False / B):
				print("\n4. The Astrolabe, a mechanical computer was invented by the Greeks about 2100 years ago was used as a navigational aid by pilots. True or False?")
				print("a) True")
				print("b) False\n")#Correct Answer
				#Will Validate User Input:
				while True:
					computerScienceAnswer4 = input("Answer: ").upper()
					if computerScienceAnswer4 == "A" or computerScienceAnswer4 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer4 == "B":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: B) False")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Five (Correct Answer = False / B):
				print("\n5. There are 4 significant generations of computers. True or False?")
				print("a) True")
				print("b) False\n")#Correct Answer
				#Will Validate User Input:
				while True:
					computerScienceAnswer5 = input("Answer: ").upper()
					if computerScienceAnswer5 == "A" or computerScienceAnswer5 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer5 == "B":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: B) False")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Six (Correct Answer = False / B):
				print("\n6. LAN is widespread over a large geographic area. True or False?")
				print("a) True")
				print("b) False\n")#Correct Answer
				#Will Validate User Input:
				while True:
					computerScienceAnswer6 = input("Answer: ").upper()
					if computerScienceAnswer6 == "A" or computerScienceAnswer6 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer6 == "B":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: B) False")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Seven (Correct Answer = False / B):
				print("\n7. Network connections can only be wireless. True or False?")
				print("a) True")
				print("b) False\n")#Correct Answer
				#Will Validate User Input:
				while True:
					computerScienceAnswer7 = input("Answer: ").upper()
					if computerScienceAnswer7 == "A" or computerScienceAnswer7 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer7 == "B":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: B) False")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Eight (Correct Answer = True / A):
				print("\n8. The computer is an electronic device that executes program instructions. True or False?")
				print("a) True")#Correct Answer
				print("b) False\n")
				#Will Validate User Input:
				while True:
					computerScienceAnswer8 = input("Answer: ").upper()
					if computerScienceAnswer8 == "A" or computerScienceAnswer8 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer8 == "A":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorect")
							if showAns == 1:
								print("The correct answer is: A) True")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Nine (Correct Answer = B):
				print("\n9. The Third Generation of computers used….")
				print("a) Transistor driven machines that stored information in memory")
				print("b) Integrated circuits with miniaturized transistors on silicon chips, called semiconductors")#Correct Answer
				print("c) Vacuum tube as circuits and magnetic drums for memory")
				print("d) Parallel processing and superconductors\n")
				#Will Validate User Input:
				while True:
					computerScienceAnswer9 = input("Answer: ").upper()
					if computerScienceAnswer9 == "A" or computerScienceAnswer9 == "B" or computerScienceAnswer9 == "C" or computerScienceAnswer9 == "D":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer9 == "B":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: B) Integrated circuits with miniaturized transistors on silicon chips, called semiconductors")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Question Ten (Correct Answer = True / A):
				print("\n10. The Analytical Engine was the first programmable mechanical computer. True or False?")
				print("a) True")#Correct Answer
				print("b) False\n")
				#Will Validate User Input:
				while True:
					computerScienceAnswer10 = input("Answer: ").upper()
					if computerScienceAnswer10 == "A" or computerScienceAnswer10 == "B":
						#Will Validate To See If User Input Matches The Correct Answer, If User Input Does, Adds Another Point Towards Category One Score:
						if computerScienceAnswer10 == "A":
							print("\nCorrect")
							computerScienceScore += 1
						else:
							print("\nIncorrect")
							if showAns == 1:
								print("The correct answer is: A) True")
						break
						#If User Input Does Not Match Availiable Answer Options Then An Error Message Prints:
					else:
						print("\nInvalid option")
						print("Please try again\n")
				#------------------------------------------------------------------

				#Ends CS stopwatch and gets total average time
				EndCS=time.time()
				CSTime=(EndCS-StartCS)
				CSAvgTime=(CSTime)/10

				#Results:
				print("\nYou answered {}/10 questions correctly".format(computerScienceScore))
				secs = int(CSTime % 60)
				mins = int((CSTime-secs) // 60)
				hours = int((CSTime // 60) // 60)
				print("\nIt took you ", hours,'hrs :',mins,'mins :',secs,'secs')
				avgHours=hours/10
				avgMins=mins/10
				avgSecs=secs/10
				print("\nYou averaged %d hrs : %d mins : %d secs for each question"%(avgHours,avgMins,avgSecs))
				completedSubjects.append("computer science")

				#Asks user if they want to play again.
				invalid=1
				while invalid==1:
					userComputerScienceAns=str(input("\nDo you want to try the quiz again (yes or no)\nYour choice: ")).lower()
					if userComputerScienceAns=="yes":
						ComputerSciencePlayAgain=0
						invalid=0
					elif userComputerScienceAns == "no":
						ComputerSciencePlayAgain=1
						invalid=0
					else:
						print("\nInvalid option")
						print("Please try again")

	#Saves time
	completedSubjectListLength=len(completedSubjects)
	counter=0

	#Math
	while counter<completedSubjectListLength:
		if completedSubjects[counter]=="math":
			f=open("SavedMath.py","w")
			f.write("\nmathTime="+str(mathTime))
			f.write("\nMathAvgTime="+str(MathAvgTime))
			f.close()
		counter=counter+1
	counter=0

	#English
	while counter<completedSubjectListLength:
		if completedSubjects[counter]=="english":
			f=open("SavedEnglish.py","w")
			f.write("\nEnglishTime="+str(EnglishTime))
			f.write("\nEnglishAvgTime="+str(EnglishAvgTime))
			f.close()
		counter=counter+1
	counter=0

	#History
	while counter<completedSubjectListLength:
		if completedSubjects[counter]=="history":
			f=open("SavedHistory.py","w")
			f.write("\nHistoryTime="+str(HistoryTime))
			f.write("\nHistoryAvgTime="+str(HistoryAvgTime))
			f.close()
		counter=counter+1
	counter=0

	#Science
	while counter<completedSubjectListLength:
		if completedSubjects[counter]=="science":
			f=open("SavedScience.py","w")
			f.write("\nScienceTime="+str(ScienceTime))
			f.write("\nScienceAvgTime="+str(ScienceAvgTime))
			f.close()
		counter=counter+1
	counter=0

	#Computer science
	while counter<completedSubjectListLength:
		if completedSubjects[counter]=="computer science":
			f=open("SavedCs.py","w")
			f.write("\nCSTime="+str(CSTime))
			f.write("\nCSAvgTime="+str(CSAvgTime))
			f.close()
		counter=counter+1
	counter=0