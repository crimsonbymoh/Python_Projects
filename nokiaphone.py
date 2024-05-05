prompt = """

    LIST OF MENU FUNCTIONS!!!

    Press 
    1 -> PHONEBOOK
    2 -> MESSAGES
    3 -> CHAT
    4 -> CALL REGISTER
    5 -> TONES
    6 -> SETTINGS
    7 -> CALL DIVERT
    8 -> GAMES
    9 -> CALCULATOR
    10 -> REMINDERS
    11 -> CLOCK
    12 -> PROFILES
    13 -> SIM SERVICES
    """

print(prompt)

userInput = int(input())

match userInput:

	case 1:
            print("PHONEBOOK")
            phonebookPrompt = """
            Press 
            1.-> Search
            2.-> Services Nos
            3.-> Add Name
            4.-> Erase
            5.-> Edit
            6.-> Assign Tone
            7.-> Send B'Card
            8.-> Options
            9.-> Speed Dials
            10.-> Voice Tags
            """
            print(phonebookPrompt)
            userPhoneBook = int(input())

            match userPhoneBook:
                case 1:
                    print("Search")
                case 2:
                    print("Service Nos")
                case 3:
                    print("Add Name")
                case 4:
                    print("Erase")
                case 5:
                    print("Edit")
                case 6:
                    print("Assign Tone")
                case 7:
                    print("Send B'Card")
                case 8:
                    print("Options")
                    options = """
                    Press
                    1-> Type Of View
                    2-> Memory
                    """
                    print(options)
                    userOptions = int(input())

                    match userOptions:
                        case 1:
                            print("Type Of View")
                        case 2:
                            print("Memory")
                        case _:
                            print("Whatever You Conceive Him To Be")
                case 9:
                    print("Speed Dials")
                case 10:
                    print("Voice Tags")
                case _:
                    print("Back To Menu")
	case 2:
		print("MESSAGES")

		messages_prompt = """
    		Press 
   		1.-> Write Messages
    		2.-> Inbox
   		3.-> Outbox
    		4.-> Picture Messages
    		5.-> Templates
    		6.-> Smileys
   		7.-> Message Settings
    		8.-> Info Service
    		9.-> Voice Mailbox Number
    		10.-> Service Command Editor
    		"""
		print(messages_prompt)
		user_input_message = int(input())

		match user_input_message:
			case 1:
           	 		print("Write Messages")
			case 2:
           	 		print("Inbox")
			case 3:
            			print("Outbox")
			case 4:
            			print("Picture Messages")
			case 5:
            			print("Templates")
			case 6:
            			print("Smileys")
			case 7:

				print("Message Settings")
				message_settings = """
            			Press
            			1-> Set
            			2-> Common 
            			"""
				print(message_settings)
				user_message_settings = int(input())

				match user_message_settings:
					case 1:
						print("Set")
						settings = """
                   				Press
                   			 	1-> Message Centre Number
                    			 	2-> Messages Sent As
                    			 	3-> Message Validity
                    			 	"""
				print(settings)
				user_set = int(input())

				match user_set:
					case 1:
						print("Message Centre Number")
					case 2:
						print("Messages Sent As")
					case 3:
						print("Message Validity")
					case _:
						print("Find Solace In Your Solitary Solitude")

					case 2:
						print("Common")
						common = """
						Press
						1-> Delivery Reports
						2-> Reply Via Same Centre
						3-> Character Support
						"""
						print(common)
						user_common = int(input())

				match user_common:
					case 1:
						print("Delivery Reports")
					case 2:
						print("Reply Via Same Centre")
					case 3:
						print("Character Support")
					case _:
						print("Find Solace In Your Solitary Solitude")

			case 8:
				print("Info Service")
			case 9:
				print("Voice Mailbox Number")
			case 10:
				print("Service Command Editor")
			case _:
				print("Find Solace In Your Solitary Solitude")


	case 3:
            print("CHAT")
            print("""
                Press 
                  Chat
                """)
            user_input_chat = int(input())

            match user_input_chat:
                case 1:
                    print("Chat")
                    break
                case _:
                    print("Make Peace With God")
                    break
	case 4:
            print("CALL REGISTER")
            print("""
                Press 
                1.-> Missed Calls
                2.-> Received Calls
                3.-> Dialled Calls
                4.-> Erase Recent Call Lists
                5.-> Show Call Duration
                6.-> Show Call Costs
                7.-> Call Cost Settings
                8.-> Prepaid Credit 
                """)

            user_input_call_register = int(input())

            match user_input_call_register:

                case 1:
                    print("Missed Calls")
                    break
                case 2:
                    print("Received Calls")
                    break
                case 3:
                    print("Dialled Calls")
                    break
                case 4:
                    print("Erase Recent Call Lists")
                    break
                case 5:
                    print("Show Call Duration")
                    print("""
                        Press 
                        1.-> Last Call Duration 
                        2.-> All Calls Duration
                        3.-> Received Calls Duration
                        4.-> Dialled Calls Duration
                        5.-> Clear Timers
                        """)

                    user_input_show_call_duration = int(input())

                    match user_input_show_call_duration:

                        case 1:
                            print("Last Call Duration")
                            break
                        case 2:
                            print("All Calls Duration")
                            break
                        case 3:
                            print("Received Calls Duration")
                            break
                        case 4:
                            print("Dialled Calls Duration")
                            break
                        case 5:
                            print("Clear Timers")
                            break
                        case _:
                            print("Make Peace With God")
                            break
                
                case 6:

                    print("Show Call Costs")

                    print("""
                        Press 
                        1.-> Last Call Cost
                        2.-> All Calls Cost
                        3.-> Clear Counters
                        """)
                    user_input_show_call_costs = int(input())
                    match user_input_show_call_costs:
                        case 1:
                            print("Last Call Cost")
                            break
                        case 2:
                            print("All Calls Cost")
                            break
                        case 3:
                            print("Clear Counters")
                            break
                        case _:
                            print("Make Peace With God")
                            break
                
                case 7:

                    print("Call Cost Settings")
                    print("""
                        Press 
                        1.-> Call Cost Limit
                        2.-> Show Costs In
                        """)
                    user_input_call_cost_settings = int(input())
                    match user_input_call_cost_settings:
                        case 1:
                            print("Call Cost Limit")
                            break
                        case 2:
                            print("Show Costs In")
                            break
                        case _:
                            print("Make Peace With God")
                            break
                
                case 8:
                    print("Prepaid Credits")
                    break
                case _:
                    print("Find Solace In Your Solitary Solitude")
                    break

	case 5:

		print("TONES")

		tones = """
		Press 

		1.-> Ringing Tone
		2.-> Ringing Volume
		3.-> Incoming Call Alert
		4.-> Composer
		5.-> Message Alert Tone
		6.-> Keypad Tones
		7.-> Warning And Game Tones
		8.-> Vibrating Alert
		9.-> Screen Saver

		"""

		print(tones)

		user_tones = int(input())

		match user_tones:

			case 1:
				print("Ringing Tone")
				break
			case 2:
				print("Ringing Volume")
				break
			case 3:
				print("Incoming Call Alert")
				break
			case 4:
				print("Composer")
				break
			case 5:
				print("Message Alert Tone")
				break
			case 6:
				print("Keypad Tones")
				break
			case 7:
				print("Warning And Game Tones")
				break
			case 8:
				print("Vibrating Alert")
				break
			case 9:
				print("Screen Saver")
				break
			case _:
				print("Whatever You Conceive Him To Be")
				break

    
	case 6:

		print("SETTINGS")
		settings = """
		Press 

		1.-> Call Settings
		2.-> Phone Settings
		3.-> Security Settings
		4.-> Restore Factory Settings
		"""
		print(settings)

		user_settings = int(input())

		match user_settings:

			case 1:
				print("Call Settings")
				call_settings = """
				Press 

				1.-> Automatic Redial
				2.-> Speed Dialling
				3.-> Call Waiting Options
				4.-> Own Number Sending
				5.-> Phone Line In Use
				6.-> Automatic Answer
				"""
				print(call_settings)

		user_call_settings = int(input())

		match user_call_settings:

			case 1:
				print("Automatic Redial")
				break
			case 2:
                            	print("Speed Dialling")
				
			case 3:
                            	print("Call Waiting Options")
				
			case 4:
                           	 print("Own Number Sending")
				
			case 5:
                            	print("Phone Line In Use")
				
			case 6:
                            	print("Automatic Answer")
				
			case _:
                            	print("Whatever You Conceive Him To Be")
				
			case 2:
				print("Phone Settings")

				phone_settings = """

				Press 

				1.-> Language
				2.-> Cell Info Display
				3.-> Welcome Note
				4.-> Network Selection
				5.-> Lights
				6.-> Confirm SIM Service
				"""
				print(phone_settings)

			
		user_phone_settings = int(input())

		match user_phone_settings:
				case 1:
					print("Language")
					break
				case 2:
					print("Cell Info Display")
					break
				case 3:
					print("Welcome Note")
					break
				case 4:
					print("Network Selection")
					break
				case 5:
					print("Lights")
					break
				case 6:
					print("Confirm SIM Service")
					break
				case _:
					print("Whatever You Conceive Him To Be")
					break
				case 3:
					print("Security Settings")

					security_settings = """

					Press 

					1.-> PIN Code Request
					2.-> Call Barring Service
					3.-> Fixed Dialling
					4.-> Closed User Group
					5.-> Phone Security
					6.-> Change Access Codes
					"""
					print(security_settings)

					user_security_settings = int(input())

		match user_security_settings:
			case 1:
				print("PIN Code Request")
				break
			case 2:
				print("Call Barring Service")
				break
			case 3:
				print("Fixed Dialling")
				break
			case 4:
				print("Closed User Group")
				break
			case 5:
				print("Phone Security")
				break
			case 6:
				print("Change Access Codes")
				break
			case _:
				print("Whatever You Conceive Him To Be")
				break
			case 4:
				print("Restore Factory Settings")
				break
			case _:
				print("Whatever You Conceive Him To Be")

	case 7:
        	print("CALL DIVERT")
			
	case 8:
        	print("GAMES")
			
	case 9:
        	print("CALCULATOR")
			
	case 10:
        	print("REMINDERS")
			
	case 11:

        	print("CLOCK")

		clock_options = """

		Press 
		1.-> Alarm Clock
		2.-> Clock Settings
		3.-> Date Setting
		4.-> Stop Watch	
		5.-> Countdown Timer
		6.-> Auto Update Of Date And Time
		"""
		print(clock_options)

	user_clock = int(input("Enter your choice: "))

	match user_clock:

		case 1:
			print("Alarm Clock")
			break
		case 2:
			print("Clock Settings")
			break
		case 3:
			print("Date Setting")
			break
		case 4:
			print("Stop Watch")
			break
		case 5:
			print("Countdown Timer")
			break
		case 6:
			print("Auto Update Of Date And Time")
			break
		case _:
			print("Whatever You Conceive Him To Be")
	case 12:

        	print("PROFILES")
	case 13:
        	print("SIM SERVICES")
	case _:

        print("Find Solace In Your Solitary Solitude")

	

	


	
    
    


            
