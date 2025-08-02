menu = """ 
        1 -> Phonebook 
        2 -> Messages 
        3 -> Chat 
        4 -> Call register 
        5 -> Tones 
        6 -> Settings 
        7 -> Call divert 
        8 -> Games 
        9 -> Calculator 
       10 -> Remainders 
       11 -> Clock 
       12 -> Profiles 
       13 -> SIM services
       14 -> Exit
        """ 
print(menu)

menu_select = int(input("Which of the menu do you want? "))
match menu_select:
	case 1:
		phone_book =  """
		PhoneBook:
	       1 -> Search
	       2 -> Service Nos.
	       3 -> Add name
	       4 -> Erase
	       5 -> Edit
	       6 -> Assign tone
	       7 -> Send b'card
	       8 -> Options
	       9 -> Speed dials
	      10 -> Voice tags
	      11 -> Previous
	       """ 
		print(phone_book)
		phonebook_select = int(input("Which of the phonebook do you want? "))
		match phonebook_select:
			case 1:
				print("""
				Search:
				1 -> Search
				2 -> Back
				""")
				search_select = int(input("Which of the phonebook do you want? "))
				match search_select:
					case 1:
						print("Search")
					case 2:
						print(phone_book)
						phonebook_select = int(input("Which of the phonebook do you want? "))
					case _:
						print("Invalid Input")

			case 2:
				print("""
				Service Nos.:
				1 -> Service Nos.
				2 -> Back
				""")
			case 3:
				print("""
				Add name:
				1 -> Add name
				2 -> Back
				""")
			case 4:
				print("""
				Erase:
				1 -> Erase
				2 -> Back
				""")
			case 5:
				print("""
				Edit:
				1 -> Edit
				2 -> Back
				""")
			case 5:
				print("""
				Edit:
				1 -> Edit
				2 -> Back
				""")
			case 6:
				print("""
				Assign:
				1 -> Assign
				2 -> Back
				""")
			case 7:
				print("""
				Send b'card:
				1 -> Send b'card
				2 -> Back
				""")
			case 8:
				options = """
				Options:
				1 -> Type of view
				2 -> Memory Status	 
				3 -> Back
				"""
				optionsSelect = int(input("Which of the Options do you need? "))
				match optionsSelect:
					case 1:
						print("Type of view")
					case 2:
						print("Memory Status")
					case 3:
						phonebook_select = int(input("Which of the phonebook do you want? "))	
					case _ :
						print("Invalid Input")			
			case 9:
				print("""
				Speed dials
	      		1 -> Speed dials
				2 -> 	Back
				""")			
				match
			case 10:
				print("""
				Voice tags:
				1 -> Voice tags				
				2 -> Back
				""")
			case 11:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")


	case 2:
		Messages = """
		Messages:
	       1 -> Write messages
	       2 -> Inbox
	       3 -> Outbox
	       4 -> Picture messages
	       5 -> Templates
	       6 -> Smileys
	       7 -> Message settings
	       8 -> Info service
	       9 -> Voice mailbox number
	      10 -> Service command editor
	      11 -> Back
	     	 """
		print(Messages)
		messages_select = int(input("Which of the Messages do you want? "))
		match messages_select:
			case 1:
				print("""
				Write messages:
				1 -> Write messages				
				2 -> Back
				""")
			case 2:
				print("""
				Inbox:
				1 -> Inbox				
				2 -> Back
				""")
			case 3:
				print("""
				Outbox:
				1 -> Outbox				
				2 -> Back
				""")
			case 4:
				print("""
				Picture messages:
				1 -> Picture messages				
				2 -> Back
				""")
			case 5:
				print("""
				Templates:
				1 -> Templates				
				2 -> Back
				""")
			case 6:
				print("""
				Smileys:
				1 -> Smileys				
				2 -> Back
				""")
			case 7:
				print("""
				Message settings:
				1 -> Set 1	
				2 -> Common	
				3 -> Back
				""")
				message_settings_select = int(input("Which of the Message settings do you need? "))
				match message_settings_select:
					case 1:
						print("""
						Set 1:
						1 -> Message centre number
						2 -> Messages sent as
						3 -> Message validity
						4 -> Back
						""")
					case 2:
						print("""
						Common:
						1 -> Delivery reports
						2 -> Reply via same centre
						3 -> Character Support
						""")
					case 3:
						print(Messages)
						messages_select = int(input("Which of the Messages do you want? "))
					case _:
						print("Invalid Input")
			case 8:
				print("""
				Info service:
				1 -> 	Info service
				2 -> 	Back
				""")
			case 9:
				print("""
				Voice mailbox number:
				1 -> 	Voice mailbox number
				2 -> 	Back
				""")
			case 10:
				print("""
				Service command editor:
				1 -> 	Service command editor
				2 -> 	Back
				""")
			case _ :
				print("Invalid Input")
				
	case 3:
		print("""
		Chat:
		1 -> Chat
		2 -> Back
		""")
		chat_select = int(input("Which of the Chat do you want? "))
		match chat_select:
			case 1:
				print("Chat")
			case 2:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 4:
		call_register = """
		Call register:
	       1 -> Missed calls
	       2 -> Received calls
	       3 -> Dialled numbers
	       4 -> Erase recent call lists
	       5 -> Show call duration
	       6 -> Show call costs
	       7 -> Call cost settings
	       8 -> Prepaid credit
	       9 -> Back
	     	 """
		print(call_register)
		call_register_select = int(input("Which of the Call register do you want? "))
		match call_register_select:
			case 1:
				print("""
				Missed calls:
				1 -> Missed calls
				2 -> Back
				""")
			case 2:
				print("""
				Received calls:
				1 -> Received calls
				2 -> Back
				""")
			case 3:
				print("""
				Dialled numbers:
				1 -> Dialled numbers
				2 -> Back
				""")
			case 4:
				print("""
				Erase recent call lists:
				1 -> Erase recent call lists
				2 -> Back
				""")
			case 5:
				print("""
				Show call duration:
				1 -> Last call duration
				2 -> All calls' duration
				3 -> Received calls' duration
				4 -> Dialled calls' duration
				5 -> Clear timers				
				6 -> Back
				""")
				call_duration_select = int(input("Which of the Call duration do you need? "))
				match call_duration_select:
					case 1:
						print("""
						Last call duration:
						1 -> Last call duration
						2 -> Back
						""")
					case 2:
						print("""
						All calls' duration:
						1 -> All calls' duration
						2 -> Back
						""")
					case 3:
						print("""
						Received calls' duration:
						1 -> Received calls' duration
						2 -> Back
						""")
					case 4:
						print("""
						Dialled calls' duration:
						1 -> Dialled calls' duration
						2 -> Back
						""")
					case 5:
						print("""
						Clear timers:
						1 -> Clear timers
						2 -> Back
						""")
					case 6:
						print(call_register)
						call_register_select = int(input("Which of the Call register do you want? "))
					case _ :
						print("Invalid Input")
			case 6:
				print("""
				Show call costs:
				1 -> Last call cost
				2 -> All calls' cost
				3 -> Clear counters				
				4 -> Back
				""")
				show_calls_costs_select = int(input("Which of the Show call costs do you need? "))
				match show_calls_costs_select:
					case 1:
						print("""
						Last call cost:
						1 -> Last call cost
						2 -> Back
						""")
					case 2:
						print("""
						All calls' cost:
						1 -> All calls' cost
						2 -> Back
						""")
					case 3:
						print("""
						Clear counters:
						1 -> Clear counters
						2 -> Back
						""")
					case 4:
						print(call_register)
						call_register_select = int(input("Which of the Call register do you want? "))
					case _ :
						print("Invalid Input")
			case 7:
				print("""
				Call cost settings:
				1 -> Call cost limit
				2 -> Show costs in
				3 -> Back				
				""")
				call_cost_settings_select = int(input("Which of the Call cost settings do you need? "))
				match call_cost_settings_select:
					case 1:
						print("""
						Call cost limit:
						1 -> Call cost limit
						2 -> Back
						""")
					case 2:
						print("""
						Show costs in:
						1 -> Show costs in
						2 -> Back
						""")
					case 3:
						print(call_register)
						call_register_select = int(input("Which of the Call register do you want? "))
					case _ :
						print("Invalid Input")
			case 8:
				print("""
				Prepaid credit:
				1 -> Prepaid credit
				2 -> Back				
				""")
				prepaid_credit_select = int(input("Which of the Prepaid credit do you need? "))
				match prepaid_credit_select:
					case 1:
						print("Prepaid credit")
					case 2:
						print(call_register)
						call_register_select = int(input("Which of the Call register do you want? "))
					case _ :
						print("Invalid Input")
			case 9:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 5:
		Tones = """
		Tones:
	       1 -> Ringing tone
	       2 -> Ringing volume
	       3 -> Incoming call alert
	       4 -> Composer
	       5 -> Message alert tone
	       6 -> Keypad tones
	       7 -> Warning and game tones
	       8 -> Vibrating alert
	       9 -> Screen saver
	      10 -> Back
	      """
		print(Tones)
		tones_select = int(input("Which of the Call register do you want? "))
		match tones_select:
			case 1:
				print("""
				Ringing tone:
				1 -> Ringing tone				
				2 -> Back
				""")
			case 2:
				print("""
				Ringing volume:
				1 -> Ringing volume				
				2 -> Back
				""")
			case 3:
				print("""
				Incoming call alert:
				1 -> Incoming call alert				
				2 -> Back
				""")
			case 4:
				print("""
				Composer:
				1 -> Composer				
				2 -> Back
				""")
			case 5:
				print("""
				Message alert tone:
				1 -> Message alert tone				
				2 -> Back
				""")
			case 6:
				print("""
				Keypad tones:
				1 -> Keypad tones				
				2 -> Back
				""")
			case 7:
				print("""
				Warning and game tones:
				1 -> 	Warning and game tones
				2 -> Back	
				""")
			case 8:
				print("""
				Vibrating alert:
				1 -> Vibrating alert				
				2 -> Back
				""")
			case 9:
				print("""
				Screen saver:
				1 -> Screen saver				
				2 -> Back
				""")
			case 10:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 6:
		settings = """
		Settings:
	       1 -> Call settings
	       2 -> Phone settings
	       3 -> Security settings
	       4 -> Back
	     """
		print(settings)
		settings_select = int(input("Select a Settings function? "))
		match settings_select:
			case 1:
				call_settings = """
				Call settings:
				1 -> Automatic redial
				2 -> Speed dialling
				3 -> Call waiting options
				4 -> Own number sending
				5 -> Phone line in use
				6 -> Automatic answer
				7 -> Back
				"""
				print(call_settings)			
				call_settings_select = int(input("Which of the Call register do you want? "))
				match call_settings_select:
					case 1:
						print("""
						Automatic redial:
						1 -> Automatic redial
						2 -> Back
						""")
					case 2:
						print("""
						Speed dialling:
						1 -> Speed dialling
						2 -> Back
						""")
					case 3:
						print("""
						Call waiting options:
						1 -> Call waiting options
						2 -> Back
						""")
					case 4:
						print("""
						Own number sending:
						1 -> Own number sending
						2 -> Back
						""")
					case 5:
						print("""
						Phone line in use:
						1 -> Phone line in use
						2 -> Back
						""")
					case 6:
						print("""
						Automatic answer:
						1 -> Automatic answer
						2 -> Back
						""")
					case 7:
						print(settings)
						settings_select = int(input("Select a Settings function? "))
					case _ :
						print("Invalid Input")
			case 2:
				phone_setting = """
				 Phone settings:
				 1 -> Language
				 2 -> Cell info display
				 3 -> Welcome note
				 4 -> Network selection
				 5 -> Lights
				 6 -> Confirm SIM service Actions
				 7 -> Back
			      """
				print(phone_setting)
				phone_setting_select = int(input("Select a Phone settings function? "))
				match phone_setting_select:
					case 1:
						print("""
						Language:
						1 -> Language
						2 -> Back
						""")
					case 2:
						print("""
						Cell info display:
						1 -> Cell info display
						2 -> Back
						""")
					case 3:
						print("""
						Call waiting options:
						1 -> Call waiting options
						2 -> Back
						""")
					case 4:
						print("""
						Welcome note:
						1 -> Welcome note
						2 -> Back
						""")
					case 5:
						print("""
						Network selection:
						1 -> Network selection
						2 -> Back
						""")
					case 6:
						print("""
						Lights:
						1 -> Lights
						2 -> Back
						""")
					case 7:
						print("""
						Confirm SIM service Actions:
						1 -> Confirm SIM service Actions
						2 -> Back
						""")
					case 7:
						print(settings)
						settings_select = int(input("Select a Settings function? "))
					case _ :
						print("Invalid Input")
			case 3:
				security_settings = """
				 Security settings:
				 1 -> PIN code request
				 2 -> Call barring service
				 3 -> Fixed dialling
				 4 -> Closed user group
				 5 -> Phone security
				 6 -> Change access codes
				 7 -> Back
			      """
				print(security_settings)
				security_settings_select = int(input("Select a Security settings function? "))
				match security_settings_select:
					case 1:
						print("""
						PIN code request:
						1 -> PIN code request
						2 -> Back
						""")
					case 2:
						print("""
						Call barring service:
						1 -> Call barring service
						2 -> Back
						""")
					case 3:
						print("""
						Fixed dialling:
						1 -> Fixed dialling
						2 -> Back
						""")
					case 4:
						print("""
						Closed user group:
						1 -> Closed user group
						2 -> Back
						""")
					case 5:
						print("""
						Phone security:
						1 -> Phone security
						2 -> Back
						""")
					case 6:
						print("""
						Change access codes:
						1 -> Change access codes
						2 -> Back
						""")
					case 7:
						print(settings)
						settings_select = int(input("Select a Settings function? "))
					case _ :
						print("Invalid Input")
			case 4:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 7:
		print("""
 		Call Divert:
	       1 -> Call Divert
	       2 -> Back
	      """)
		call_divert_select = int(input("Which of the Call Divert do you want? "))
		match call_divert_select:
			case 1:
				print("Call Divert")
			case 2:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 8:
		print( """
		Games:
		 1 -> Games
		 2 -> Back
	     """ )
		games_select = int(input("Which of the Games do you want? "))
		match games_select:
			case 1:
				print("Games")
			case 2:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 9:
		print( """
		Calculator:
	       1 -> Calculator
	       2 -> Back
	      """ )
		calculator_select = int(input("Which of the Calculator do you want? "))
		match calculator_select:
			case 1:
				print("Calculator")
			case 2:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 10:
		print("""
		Remainders:
	       1 -> Remainders
	       2 -> Back
	      """)
		remainders_select = int(input("Which of the Remainders do you want? "))
		match remainders_select:
			case 1:
				print("Remainders")
			case 2:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 11:
		clock = """
		Clock:
	       1 -> Alarm clock
	       2 -> Clock settings
	       3 -> Date setting
	       4 -> Stopwatch
	       5 -> Countdown timer
	       6 -> Auto update of date and time
	       7 -> Back
	    """
		print(clock)
		clock_select = int(input("Which of the Clock do you want? "))
		match clock_select:
			case 1:
				print("""
				Alarm clock:
				1 -> Alarm clock				
				2 -> Back
				""")
			case 2:
				print("""
				Clock settings:
				1 -> Clock settings			
				2 -> Back
				""")
			case 3:
				print("""
				Date setting:
				1 -> Date setting			
				2 -> Back
				""")
			case 4:
				print("""
				Stopwatch:
				1 -> Stopwatch			
				2 -> Back
				""")
			case 5:
				print("""
				Countdown timer:
				1 -> Countdown timer			
				2 -> Back
				""")
			case 6:
				print("""
				Auto update of date and time:
				1 -> Auto update of date and time			
				2 -> Back
				""")
			case 7:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
	case 12:
		print("""
		SIM services:
	       1 -> SIM services
	       2 -> Back
	      """)
		sim_sevices_select = int(input("Which of the SIM services do you want? "))
		match sim_sevices_select:
			case 1:
				print("SIM services")
			case 2:
				print(menu)
				menu_select = int(input("Which of the menu do you want? "))
			case _ :
				print("Invalid Input")
				
	case _ :
		print("Invalid Input")		

	      

	    
	    
	    
	    
	
	
	





							      			
			
			
			
			
			
			
			
			
			
			

		





	         
	         	      
	      	      					     				

	     




						




					
				

				

				

				

				

				
		

		
				

				



				

								
									



	     	 
