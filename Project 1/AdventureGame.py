#Troy Justesen
path_choice = input('You come to two paths with fog surrounding you, one leads LEFT and one leads RIGHT, which way should you go? ')

if path_choice.lower() == 'right':
    hear = input('You chose right to the forest. You start hearing odd NOISES on your left but see a HORSE on your right. Which should you go towards? ')
    if hear.lower() == 'horse':
        go = input('As you get closer to the horse you notice it has a saddle on and is tied to a tree. You hear the noise get closer, do you LOOK or get on the horse and GO? ')
        if go.lower() == 'go':
            print('you ride the horse to get out but as you look back you see two big blue eyes staring at you.')
        elif go.lower() == 'look':
            print('Yeah, look back at the noise instead of getting out. The monster catches you.')
        else:
            print('The monster gets you.')
    elif hear.lower() == 'noises':
        flee = input('Through some bushes you see two big blue eyes coming towards you, do you CONFRONT it, FLEE, or stay STILL? ')
        if flee.lower() == 'flee':
            plane = input('You run and hear foosteps behind you. As you run you come upon a runway with a plane. You ponder for a second on how on earth this is here, but quickly get to the plane and start it up. as you go the monster is right in the way, do you RUN IT OVER or WAIT till it moves? ')
            if plane.lower() == 'run it over':
                print('you take off and go as high as you can. you finally come on top of the clouds to see the sun. You look down but will never know if you took out the monster.')
            elif plane.lower() == 'wait':
                print("It doesn't do anything, but all of a sudden someone comes from behind throwing a bag over your head and you are possibly caught by the monster?")
            else:
                print('The monster gets you.')
        elif flee.lower() == 'confront':
            print('As you come out to meet it, you become mesmerized and the monster catches you.')
        elif flee.lower() == 'still':
            print('The monster finds you and catches you.')
        else:
            print('The monster gets you.')
    else:
        print('You were enveloped by the thick fog and could not find a way out.')
elif path_choice.lower() == 'left':
    boat = input('You chose left to the lake. You find a dock with a SPEEDBOAT and a KAYAK. Which one do you get on? ')
    if boat.lower() == 'kayak':
        jump = input('You start paddling, but as you do you hear the sound of the speedboat. You look back and it is coming right at you. Do you JUMP or try to AVOID it? ')
        if jump.lower() == 'jump':
            tree = input('The speedboat wrecks your kayak but you are able to swim to shore. You find a motorcycle but you think its keys were on the speedboat. You hear the speedboat coming back and starting to stop. Do you hide in a BUSH or climb up a TREE? ')
            if tree.lower() == 'tree':
                dash = input('You hide in the tree but notice on a couple trees there are cameras on them. You see two big blue eyes come your way but pass you to the motorcycle. Do you climb down and make a DASH for the speedboat or wait to POUNCE? ')
                if dash.lower() == 'dash':
                    print('You make it to the boat and start it up to get out. As you ride out of there, you see the monster on the shore line, looking at you with its blue eyes.')
                elif dash.lower() == 'pounce':
                    print('You try to overpower the monster but it catches you instead.')
                else:
                    print('The monster gets you.')
            elif tree.lower() == 'bush':
                print('The monster somehow comes right towards you and gets you.')
            else:
                print('The monster gets you.')
        elif jump.lower == 'avoid':
            print('You get ran over by the speedboat.')
        else:
            print('The monster gets you.')
    elif boat.lower() == 'speedboat':
        keys = input("You try to start it up but it has the wrong keys and can't find the right keys. You look down in the WATER and see something shining but it may be on the GROUND. Where do you look? ")
        if keys.lower() == 'water':
            motorcycle = input('You found the keys under the water but as you come up, you see two big blue eyes staring at you, do you SWIM to the other shore line or SEE what the monster wants? ')
            if motorcycle.lower() == 'swim':
                wait = input('You get to the other shoreline but the monster is using the kayak to get to you. You find a motorcycle and the wrong keys are for the motorcycle. Do you RIDE out or WAIT for the monster? ')
                if wait.lower() == 'ride':
                    print('You ride out of there and as you look back you see the two big blue eyes staring at you as you leave.')
                elif wait.lower() == 'wait':
                    print('If you were asking for a death wish I could have put in an option for you to die, oh wait, I did. The monster gets you.')
                else:
                    print('The monster gets you.')
            elif motorcycle.lower() == 'see':
                print('It wants to kill you obviously, the monster captures you.')
            else:
                print('The monster gets you.')
        elif keys.lower() == 'ground':
            fight = input('As you look around you hear footsteps. You look up to two big blue eyes staring at you. Do you RUN or FIGHT it? ')
            if fight.lower == 'run':
                odd = input("You run down the shore line while you hear footsteps behind you. You hear ODD noises up ahead but there's another BOAT in the water. Which one do you got towards? ")
                if odd.lower() == 'odd':
                    box = input("You go towards the noise and realize it's a bunch of big smoke machines making the fog. The footsteps get closer as you find a box with a KNIFE, GUN, and an EMP. What do you use to fight? ")
                    if box.lower() == 'gun':
                        robot = input('You shoot the monster in the middle of its eyes and realize its a robot. Just then you here someone yelling angrily from the forest, do you STAY to confront the person or get on the BOAT? ')
                        if robot.lower() == 'boat':
                            print('You get on the boat that has keys in them this time, and ride away. As you look back you see multiple big blue eyes staring at you.')
                        elif robot.lower() == 'stay':
                            print('The person yells out attack and multiple big blue eyed monsters come. You get overwhelmed and the monsters get you')
                        else:
                            print('The monsters catch you.')
                    elif box.lower() == 'emp':
                        emp = input('You throw the emp at the monster and it fries it, finding out its a robot. You see it trying to start up again and hear someone yelling angrily towards you from the forest. Do you STAY or get on the BOAT? ')
                        if emp.lower() == 'stay':
                            print('The monster comes back online with the person shouting attack where multiple monsters come and easily overwhelm you.')
                        elif emp.lower() == 'boat':
                            print('You get on the boat and this time it has keys in it. You start it up and ride out. You look back to see the monster coming online with its blue eyes staring at you. But you notice more eyes start appearing, with the same big blue eyes staring at you.')
                        else:
                            print('The monster gets you.')
                    elif box.lower() == 'knife':
                        print('You brought a knife to a monster fight, the monster catches you.')
                    else:
                        print('The monster gets you.')
                elif odd.lower() == 'boat':
                    print('The boat has keys in it and you are able to escape. As you look back you see two big blue eyes staring at you as you leave.')
                else:
                    print('The monster gets you.')
            elif fight.lower() == 'fight':
                print("The monster's eyes mezmorize you and it captures you.")
            else:
                print('The monster gets you.')
        else:
            print('You were enveloped by the thick fog and could not find a way out.')
    else:
        print('You were enveloped by the thick fog and could not find a way out.')
elif path_choice.lower() == 'straight' or 'forward':
    house = input('You found a hidden path through the bushes. The path leads to the back of a house, go to the HOUSE or continue on the PATH? ')
    if house.lower() == 'house':
        peek = input('You hear an odd noise when you approach the house. Do you PEEK in the window, walk IN, or KNOCK? ')
        if peek.lower() == 'peek':
            inside = input('You look in and see nothing but a set of car keys on the table. Then you hear the noise again coming from a room inside. You found the WINDOW is unlocked but so is the DOOR, how should you enter? ')
            if inside.lower() == 'window':
                outside = input('You get in and grab the keys from off the table but you hear the door where the noise is start to open, do you run out the FRONT or the WINDOW? ')
                if outside.lower() == 'front':
                    print('You escape out the front and find the car for the keys. You get in and as you drive away, you see two big blue eyes stare at you through the fog at the front door.')
                elif outside.lower() == 'window':
                    print('It took you too long to climb out the window and you were caught by the monster.')
                else:
                    print('The monster got you.')
            elif inside.lower() == 'door':
                print('An alarm was activated by the door, alerting the monster and catching you.')
            else:
                print('You were enveloped by the thick fog and could not find a way out.')
        elif peek.lower() == 'in':
            print('An alarm was activated by the door, alerting the monster and catching you.')
        elif peek.lower() == 'knock':
            print('The monster opens the door and you only see two big blue eyes. They seem confused but you get mesmerized to go near it and the monster catches you.')
        else:
            print('You were enveloped by the thick fog and could not find a way out.')
    elif house.lower() == 'path':
        run = input('You continue past the house but get the feeling something is watching you. You look back and see two big blue eyes looking at you from the front door of the house. Do you go BACK or RUN? ')
        if run.lower() == 'run':
            ride = input("You start running but here something running behind you as well. You find a bike but you also don't hear anything behind you anymore. Do you stop to LOOK back or RIDE out of there? ")
            if ride.lower() == 'ride':
                print('You escape and as you ride out, you see the blue eyes right where you found the bike.')
            elif ride.lower() == 'look':
                print('Why would you stop to look back? the monster catches you.')
            else:
                print('The monster gets you.')
        elif run.lower() == 'back':
            print('As you approach, the eyes start to mesmerize you closer and you get caught by the monster')
        else:
            print('You were enveloped by the thick fog and could not find a way out.')
    else:
        print('You were enveloped by the thick fog and could not find a way out.')
else:
    print('You were enveloped by the thick fog and could not find a way out.')