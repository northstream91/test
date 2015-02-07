#array for messages
kvittr_messages = []
menu_index = 0

while menu_index != 9:
	print "1. Print all messages"
	print "2. Add new message"
	print "3. Delete a message"
	print "4. Exit kvittr"
	menu_index = input("What would you like to do?: ")

	if menu_index == 1:
		#remove brackets, and print each message on a new line
		print '\n'.join(kvittr_messages) 
	elif menu_index == 2:
		message = raw_input("Type in your message: ")
		if len(message) > 140:
			print "You message is longer than 140 charachters, please try again"
			menu_index = 2
		else:
			# add the new message to the array
			kvittr_messages.append(message)
	elif menu_index == 3:
		# if kvittr_messages is not empty
		if len(kvittr_messages) >= 1:
			# go thru all messages in array and print them with place in array
			for message_index in range(len(kvittr_messages)):
				print message_index, kvittr_messages[message_index]	
			message_delete_index = input("Which message do you want to delete?: ")
			# delete the chosen message in array
			del kvittr_messages[message_delete_index]
		else:
			#if kvittr_messages is empty
			print "There are no messages to delete"
			menu_index = 2
	elif menu_index == 4:
		quit()
	else:
		# if user chooses wrong, press return for main menu
		print "That is not an option. Please choose 1, 2, 3 or 4"
		menu_index = raw_input("Press enter to try again")
