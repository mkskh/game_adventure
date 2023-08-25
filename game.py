game = True

while game == True:
    print('\n Welcome to a game "Adventure"!')
    name = input('\n Please write your name: ')
    print('\n Hello,', name,'. You stand in a dark room and see 2 portals with names: \n1. Fairy World. \n2. Space.')

    choice = int(input('\n What do ou want to choose? (write the number): '))
    if choice == 1:
        print('\n Welcome to Fairy World!')
        print("\n That's a beautiful world where you can find your love! But first you need to get to the city. There you will find your love!")
        print('\nYou can: \n1. Go to the city. \n2. Come back ')
        
        choice_city = int(input('\n What do you want to choose? (write the number): '))
        if choice_city == 1:
            print('\n You get lost, but you can see an old man in the distance. ')
            print('\n You can: \n1. Come to the old man to ask a way \n2. Pass by the old man and try to get to city by my own')
            
            choice_lost = int(input(('\n What do you want to do? (write the number): ')))
            if choice_lost == 1:
                print('\n You came to the old man. And asked for help. The old man said hat he will help you but first you need to say 5 times word "Please".')
                print('You can: \n1. Say 5 times "Please" \n2. Disagree and try to get to city by my own')
                
                choice_old_man = int(input('\n What do you want to do? (write the number): '))
                if choice_old_man == 1:
                    for i in range(6):
                        print('Please')
                    print('\n The old man showed the way and you got to the city. In 2 days you met your love. And you lived with her until the end of your life in happiness. ')
                elif choice_old_man == 2:
                    print("\n You disagreed. But the old man offended your refusal and cursed you. You tried to find the way by your own. But you got lost in the mountains. You couldn't to get out and death overtook you. Game over!")

            elif choice_lost == 2:
                print("\n You went by your own. But you got lost in the mountains. You tried to get out but you spend for it 10 days (!). You almost died but you got out. You spend a lot of time on the recovery. You met your love in 2 month. And you lived with her until the end of your life in happiness.")
        
        elif choice_city == 2:
            print('\n You got back! Thank you for playing!')
            play = False




    elif choice == 2:
        print("\n Welcome to Space! \nThat's a cold and dark place. You are scared and you don't understand what do you need to do. But you turned to the right and see a spaceship and International Space Station. Where do you want to get to? \nYou can: \n1. Go to the spaceship. \n2. Go to the International Space Station ")
        
        choice_dir = int(input('\n What do ou want to do? (write the number): '))
        if choice_dir == 1:
            print('\n You made it to the spaceship. You were noticed and spaceship took you on board. You met the capitan of the ship named Spock. He said that the name of the ship is "USS Enterprise" and the team heads for Andromeda. He suggest you to go with them. ')
            print('\n You can: \n1. To go with them to Andromeda. \n2. Ask to send you to International Space Station')
            
            choice_dir2 = int(input(('\n What do you want to do? (write the number): ')))
            if choice_dir2 == 2:
                print('\n You asked to send you to ISS. Spock said hat he will help. He took an portal gun and said that you will get to ISS you need at first say 3 times  "The portal gun send me to ISS please". But he said that it can be dangerous for you. And if you do not want to have a risk you should go by your own.')
                print('\n You can: \n1. Say 3 times "The portal gun please send me to ISS " \n2. Disagree and try to get to ISS by my own')
                
                choice_spock = int(input('\n What do you want to do? (write the number): '))
                if choice_spock == 1:
                    for i in range(3):
                        print('The portal gun please send me to ISS')
                    print('\n The portal gun created a portal and you entranced there and ou got to ISS. It turned out that after passing the portal you have aged 30 years. You wanted to start doing research but you died after 2 years did not make any discovery.')
                elif choice_old_man == 2:
                    print("\n You disagreed. You went out the spaceship and tried to get the ISS by your own. But you had difficulties. You flied there 2 weeks. You almost died but you got there. You spend a lot of time on the recovery. But after that you started doing research and made a big discovery")
            
            elif choice_dir2 == 1:
                print("\n You went with them to Andromeda. Spoke and you discovered a new star system with habitable planets. 5 years later, earthlings built colonies there.")
        
        elif choice_city == 2:
            print('\n You tried to get the ISS by your own. But you had difficulties. You flied there 2,5 weeks. You almost died but you got there. You spend a lot of time on the recovery. But after that you started doing research and made a big discovery')
            play = False