import time
import random


def print_pause(message):
    print(message)
    time.sleep(1.25)


def valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        for option in options:
            if option in choice:
                return choice
        print_pause("That isn't a valid choice, please choose again")


def play_game():

    items = []

    player_health = []

    player_status = []

    Werewolf_health = []

    werewolf_status = []

    scenario_1(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status)


def play_again():
    play = valid_input("Would you like to play again?\n" "Yes or No?\n",
                       ["yes", "no"]).lower()
    if "yes" in play:
        play_game()
    elif "no" in play:
        print_pause("Thanks for playing, hope it was interesting.")


def silversword_attack(Werewolf_health):
    print_pause("You attack the Werewolf with the silversword.")
    Werewolf_health.append(random.randint(1, 6) + 4)


def unarmed_attack(Werewolf_health):
    print_pause("Stand or die!\n")
    Werewolf_health.append(random.randint(1, 6))


def wolf_damage_check_silversword(Werewolf_health, werewolf_status):
    if sum(Werewolf_health) <= 6:
        print_pause("It was a weak attack.")
        print_pause(
            "Your silversword creates a small cut across the werewolf's leg.")
        print_pause(
            "It recoils from the touch of the silver and faces you "
            "with a bit of apprehension.\n")
    elif sum(Werewolf_health) < 11 and sum(Werewolf_health) >= 6:
        print_pause("It was a solid hit!")
        print_pause(
            "Your silversword opens a deep gash across the werewolf's chest.")
        print_pause("It is now bleeding heavily.\n")
    elif sum(Werewolf_health) >= 12:
        print_pause(
            "Another slash from your silversword "
            "connects with the werewolf's neck, "
            "sending its head flying and "
            "causing blood to spray from its neck!\n")
        werewolf_status.append("dead")


def wolf_damage_check_unarmed(Werewolf_health, werewolf_status):
    if sum(Werewolf_health) <= 6:
        print_pause("You punch the werewolf in the ribs.")
        print_pause("It doesn't even flinch.\n")
    if sum(Werewolf_health) >= 6 and sum(Werewolf_health) <= 8:
        print_pause("You throw your weight into a punch.")
        print_pause("It connects and knocks one of the werewolf's teeth out.")
        print_pause("The werewolf actually looks a disoriented.\n")
    if sum(Werewolf_health) >= 8 and sum(Werewolf_health) <= 11:
        print_pause("With a mighty strike you hit the werewolf in its throat.")
        print_pause("It grasps at its own throat.")
        print_pause("After a few moments it can finally breathe.")
        print_pause("It looks at you with genuine rage.\n")
    if sum(Werewolf_health) >= 12:
        print_pause("You put all your energy into one last swing.")
        print_pause("Your punch knocks it down.")
        print_pause("You get on top of it and stomp its throat.\n")
        werewolf_status.append("dead")


def battleaxe_attack(Werewolf_health):
    print_pause("You attack the Werewolf with the battleaxe.\n")
    Werewolf_health.append(random.randint(1, 6) + 2)


def wolf_damage_check_battleaxe(Werewolf_health, werewolf_status):
    if sum(Werewolf_health) <= 6:
        print_pause("It was a weak attack.")
        print_pause("It creates a small cut on the werewolf's shoulder.")
    elif sum(Werewolf_health) >= 6 and sum(Werewolf_health) <= 11:
        print_pause("It was a solid attack.")
        print_pause("It hits the werewolf in the abdomen, "
                    "creating a deep wound. it howls in pain.\n")
    elif sum(Werewolf_health) >= 12:
        print_pause("It was a critical hit!")
        print_pause("The battleaxe comes down right on the werewolf's head."
                    "The axe splits the werewolf's head in two.\n")
        werewolf_status.append("dead")


def player_damage_check(player_health, player_status):
    if sum(player_health) <= 4:
        print_pause("The werewolf swipes at you with its claws")
        print_pause("Thankfully, it was a weak swipe. You're hurt, "
                    "but can continue.\n")
        player_status.append("minor injuries")
    elif sum(player_health) <= 7:
        print_pause("The werewolf swipes at you with its claws.")
        print_pause("You're seriously injured, "
                    "but it's die fighting or die running.")
        print_pause("You continue to fight.\n")
        player_status.append("major injuries")
    elif sum(player_health) >= 8 and sum(player_health) <= 9:
        print_pause("The werewolf swipes at you with its claws.")
        print_pause("Its claws open a large gash in your neck.")
        print_pause("You're going to die, "
                    "but decide to see if you can take the wolf with you.\n")
        player_status.append("critically injured")
    elif sum(player_health) >= 10:
        print_pause("The werewolf hits you with a massive strike.")
        print_pause("You are thrown backwards and land on your back.")
        print_pause("Before you can even try to get up, "
                    "the were wolf is already on top of you.")
        print_pause("It rips your throat out and everything goes black\n")
        player_status.append("dead")
        print_pause("GAME OVER\n")
        play_again()


def werewolf_attack(player_health, items, player_status):
    print_pause("The werewolf counter-attacks")
    player_health.append(random.randint(2, 10) + 2)
    if "chainmail" in items:
        player_health.append(-2)
    if "heavy armor" in items:
        player_health.append(-4)
    if "leather armor" in items:
        player_health.append(-1)


def scenario_1(
        items, player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    scenario_1_intro()
    scenario_1_game(
        items,
        player_health, player_status,
        Werewolf_health,
        werewolf_status)


def scenario_1_intro():
    print_pause("You wake up in a forest.")
    print_pause("The forest is too dense to make out what time it is.")
    print_pause("Looking around for a few moments, "
                "you realize it's pointless.")
    print_pause("Suddenly, there is a loud long howl, several more follow it.")
    print_pause("Wolves.....")
    print_pause("A chill runs down your spine.")
    print_pause("You can't make out where the howls originated from.")
    print_pause("You've got to get out of here.\n")


def scenario_1_game(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("Pick a direction to go: ")
    direction = valid_input("1. There is a faint path on the left\n"
                            "2. Make your way forward.\n"
                            "3. You decide to go right, "
                            "the tress don't seem as thick this way.\n",
                            ["1", "2", "3"])

    if direction == '1':
        faint_path(
            items,
            player_health,
            player_status,
            Werewolf_health,
            werewolf_status)
    elif direction == '2':
        forward(
            items,
            player_health,
            player_status,
            Werewolf_health,
            werewolf_status)
    elif direction == '3':
        right(items, werewolf_status)


def faint_path(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("You choose to follow the faint path on your left.")
    print_pause("It seems as if this path hasn't been used in years.")
    print_pause("After following the path for some time, "
                "you come upon an old cottage.")
    print_pause("Looking at the cottage, "
                "it's easy to see why this path hasn't been used.")
    print_pause("The cottage is crumbling and abandoned.\n")
    faint_path_dilemma(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status)


def faint_path_dilemma(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("Investigate the cottage? Or keep following the path past it?")
    choice = valid_input("1. Investigate the cottage.\n"
                         "2. Move past it.\n", ["1", "2"])
    if choice == '1':
        cottage(
            items,
            player_health,
            player_status,
            Werewolf_health,
            werewolf_status)
    elif choice == '2':
        cottage_path(
            items,
            player_health,
            player_status,
            Werewolf_health,
            werewolf_status)


def cottage(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("You approach the cottage, you see the door is still intact.")
    print_pause("You open the door and enter the remains of the cottage.")
    print_pause("You see a skeleton in chainmail slumped in the corner, "
                "and dried blood splattered across the wall.")
    print_pause("There's also what appears to be another stain under it, "
                "like blood pooled there.\n")
    print_pause("Its right hand is still clenching a sword, "
                "its left arm is missing.")
    print_pause("You bend down, pry the skeleton's fingers off the sword, "
                "and take it.")
    items.append("silversword")
    print_pause("It takes a while, but, you also remove the chainmail "
                "and put it on.")
    items.append("chainmail")
    print_pause("This skeleton also has a pair of thick leather boots")
    items.append("thick leather boots")
    print_pause("You put the boots on too.")
    print_pause("This grisly scene makes you think that it might not be just "
                "wolves in this forest. "
                "After inspecting the sword you find that it's made out of "
                "silver.")
    print_pause("Now you're convinced there's something horrible in "
                "this forest.")
    print_pause("You exit the cottage as quickly as possible, "
                "and start running down the path outside of the cottage.\n")
    cottage_path(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status)


def cottage_path(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("As you start going down the path you hear that howl again. "
                "This time it sounds as if it's directly on your right. "
                "You run as fast as you can, but hear a rhythmic thumping "
                "behind you.")
    print_pause("Something's chasing you! And it's catching up!")
    choice_2 = valid_input("What do you do?\n"
                           "1. Turn and fight?\n"
                           "2. Keep running!\n", ["1", "2"])
    if choice_2 == '1':
        print_pause("You turn and face whatever it is.")
        print_pause("It's a werewolf!")
        fight_1(
            items,
            Werewolf_health,
            player_health,
            player_status,
            werewolf_status)
    elif choice_2 == '2':
        print_pause("You try to keep running, "
                    "but whatever is chasing you is too fast.")
        print_pause("You feel a sharp pain as something bites you right calf.")
        print_pause("Falling to the ground, you turn to look at what bit you.")
        if "silversword" in items:
            print_pause("You look down and see the werewolf has its fangs are"
                        " sunk into your calf.")
        elif "silversword" not in items:
            print_pause("It's much worse than a wolf, it's a Werewolf! "
                        "Its fangs are deep in your calf")
        print_pause("You kick it in the face. It recoils and you scramble "
                    "to your feet.")
        if "thick leather boots" in items:
            print_pause("Those leather boots protected you from being hurt "
                        "too badly. Although you're bleeding, "
                        "you can still move fine for the most part.\n")
            player_health.append(1)
        elif "thick leather boots" not in items:
            player_health.append(2)
            print_pause("You experience some minor injuries\n")
            player_status.append("minor injuries")
        fight_1(
            items,
            Werewolf_health,
            player_health,
            player_status,
            werewolf_status)


def fight_1(
        items,
        Werewolf_health,
        player_health,
        player_status,
        werewolf_status):
    if "silversword" in items:
        for attacks in range(5):
            silversword_attack(Werewolf_health)
            wolf_damage_check_silversword(Werewolf_health, werewolf_status)
            if "dead" in werewolf_status:
                break
            werewolf_attack(player_status, items, player_health)
            player_damage_check(player_health, player_status)
            if "dead" in player_status:
                break
    if "silversword" not in items:
        for attacks in range(5):
            unarmed_attack(Werewolf_health)
            wolf_damage_check_unarmed
            if "dead" in werewolf_status:
                break
            werewolf_attack(player_health, player_status, items)
            player_damage_check(player_health, player_status)
            if "dead" in player_status:
                break
    if "dead" not in player_status:
        faint_path_end(player_status)


def faint_path_end(player_status):
    if "minor injuries" in player_status:
        print_pause("With the werewolf defeated, you continue along the path."
                    "You follow it for what seems like hours.")
        print_pause("Eventually, the forest starts thinning, "
                    "and the the sun pierces the forest canopy.")
        print_pause("It's not long before you walk out of the forest into an "
                    "open field.")
        print_pause("Congratulations, you made it out of the forest.")
        play_again()
    if "major injuries" in player_status:
        print_pause("You defeated the werewolf, but are seriously injured."
                    "You need to get out of the forest before something else "
                    "finds you."
                    "You limp along the path.")
        print_pause("You eventually reach the edge of the forest."
                    "before you is an open field."
                    "Relieved, you stop to catch your breath.")
        print_pause("Turning to see if anything is following you, "
                    "you see something coming up the path."
                    "You turn and run with the last bit of energy you can "
                    "muster.")
        print_pause("While running, you stumble and fall in the middle of the "
                    "open field. Looking back at the forest, "
                    "you get the feeling something is watching you.\n")
        print_pause("Congratulations, you just barely made it out.")
        play_again()
    if "critically injured" in player_status:
        print_pause("You may have defeated the werewolf, "
                    "but are bleeding too heavily to survive. "
                    "You decide to sit against a tree and await "
                    "the inevitable.")
        print_pause("Everything starts to fade, and you're feeling sleepy.\n")
        print_pause("GAME OVER")
        play_again()


def forward(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("You decide to move forward.")
    print_pause("After trudging through the undergrowth for some time, "
                "you come upon a clearing. "
                "It looks like a skirmish took place here, "
                "because the clearing has at least a dozen corpses in it.")
    print_pause("There is blood almost everywhere and it smells awful. "
                "It appears as if something has been eating these bodies. "
                "There are bits missing from some of them.")
    forward_dilemma(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status)


def forward_dilemma(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("This is a grim place, "
                "but there could be useful materials around.")
    choice_2 = valid_input("1. Look around and see what you can take.\n"
                           "2. Looting corpses? Never!\n", ["1", "2"])
    if choice_2 == '1':
        loot_the_corpses(
            items,
            player_health,
            player_status,
            Werewolf_health,
            werewolf_status)
    elif choice_2 == '2':
        forward_again(
            items,
            player_health,
            player_status,
            Werewolf_health,
            werewolf_status)


def loot_the_corpses(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("You decide to loot the corpses, "
                "they don't need this anymore anyway.")
    print_pause("After looking around you find a corpse with a nice suit of "
                "heavy armor.")
    print_pause("That will definitely offer some good protection.")
    choice_3 = valid_input("1. The the heavy armor.\n"
                           "2. Leave it and keep looking.\n", ["1", "2"])
    if choice_3 == '1':
        print_pause("It takes some time, but, "
                    "you strip the corpse of the armor and put it on.")
        items.append("heavy armor")
    elif choice_3 == '2':
        print_pause("You decide to keep looking for a better choice.")
        print_pause("You find a lighter set of leather armor.")
        items.append("leather armor")
    print_pause("Now that you have some armor, "
                "you start looking for a weapon.")
    print_pause("You walk around once more and a battleaxe catches your eye.")
    items.append("battleaxe")
    print_pause("Now that you're armed and armored it's time to get moving.")
    forward_again(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status)


def forward_again(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("You begin making your way through the undergrowth again. "
                "After some time, you decide to take a break and rest.")
    print_pause("You haven't heard anything like those howls from earlier.")
    print_pause("Maybe the danger is gone.")
    print_pause("Feeling much calmer, "
                "you get back to finding a way out of this forest.")
    print_pause("The forest starts becoming less dense.")
    print_pause("Rays of sun start penetrating the forest canopy.")
    print_pause("You're almost out!\n")
    print_pause("Something's not right though. You turn around.")
    print_pause("You can't see anything, but you know something's there.")
    if "battleaxe" in items:
        print_pause("Gripping your battleaxe with both hands and get ready.")
    Sudden_choice(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status)


def Sudden_choice(
        items,
        player_health,
        player_status,
        Werewolf_health,
        werewolf_status):
    print_pause("Realizing you know something is wrong, "
                "something rushes out of some bushes at you!")
    choice_4 = valid_input("It's a werewolf! It throws itself at you!\n"
                           "1. Dodge\n"
                           "2. Delfect\n"
                           "3. Counter charge\n",
                           ["1", "2", "3"])
    if choice_4 == '1' and "heavy armor" in items:
        print_pause("You try to dodge the beast, "
                    "but your heavy armor slows you down.")
        print_pause("The werewolf's charge hits you and knocks you down. "
                    "It takes a swipe at your head!")
        player_health.append(3)
        print_pause("You kick the monster off, "
                    "but it leaves a large cut on your face.")
        fight_2(
            items,
            Werewolf_health,
            player_health,
            player_status,
            werewolf_status)
    elif choice_4 == '1' and "heavy armor" or "battleaxe" not in items:
        print_pause("You step out of the way just in time and "
                    "prepare to attack.")
        fight_2(
            items,
            Werewolf_health,
            player_health,
            player_status,
            werewolf_status)
    elif choice_4 == '2' and "battleaxe" in items:
        print_pause("You deflect the werewolf's charge with a "
                    "heavy swing from the battleaxe.")
        print_pause("Your swing severs one of its hands.")
        Werewolf_health.append(4)
        print_pause("The werewolf struggles back to its feet and "
                    "snarls at you.")
        fight_2(
            items,
            Werewolf_health,
            player_health,
            player_status,
            werewolf_status)
    elif choice_4 == '3' and "heavy armor" in items:
        print_pause("You decide to rush at the monster with your "
                    "battleaxe held high.")
        print_pause("Fortune favors the brave!")
        print_pause("You crash into the beast with such force it is "
                    "thrown backward.")
        print_pause("It doesn't have time to recover before you split "
                    "its head in half!")
        forward_end(player_status)
    elif choice_4 == '3' and "heavy armor" not in items:
        print_pause("You charge at the werewolf.")
        print_pause("The two of you crash into each other.")
        print_pause("You didn't have the mass for this to be a good idea.")
        print_pause("You are thrown backwards and the beast towers over you.")
        print_pause("It's too quick for you and it tears your throat out!")
        player_status.append("dead")
        print_pause("GAME OVER!")
        play_again()


def fight_2(
        items,
        Werewolf_health,
        player_health,
        player_status,
        werewolf_status):
    if "battleaxe" in items:
        for attacks in range(5):
            battleaxe_attack(Werewolf_health)
            wolf_damage_check_battleaxe(Werewolf_health, werewolf_status)
            if "dead" in werewolf_status:
                break
            werewolf_attack(items, player_health, player_status)
            player_damage_check(player_health, player_status)
            if "dead" in player_status:
                break
        if "dead" in werewolf_status:
            forward_end(player_status)
    elif "battleaxe" not in items:
        for attacks in range(10):
            unarmed_attack(Werewolf_health)
            wolf_damage_check_unarmed(Werewolf_health, werewolf_status)
            if "dead" in werewolf_status:
                break
            werewolf_attack(items, player_health, player_status)
            player_damage_check(player_health, player_status)
            if "dead" in player_status:
                break
        if "dead" in werewolf_status:
            forward_end(player_status)


def forward_end(player_status):
    print_pause("With the werewolf dead, you turn around and exit the forest.")
    print_pause("You walk into a meadow, and in the distance"
                " is a village, beyond that is a castle.")
    print_pause("You begin making your way to them.")
    print_pause("Congratulations, you made it out of the forest.")
    if "critically injured" in player_status:
        print_pause("You may have defeated the werewolf, "
                    "but there is no chance you survive.")
        print_pause("You kneel at the edge of the forest and "
                    "look out of it.")
        print_pause("There is a meadow, beyond it is a village, "
                    "and in the distance a castle.")
        print_pause("The sky is clear and it is actually a beautfiul day "
                    "outside of the forest.")
        print_pause("Seems like a good enough place to die.")
        print_pause("GAME OVER!")
        play_again()
    play_again()


def right(items, werewolf_status):
    print_pause("You decide to start making your way to the right.")
    print_pause("After navigating through the tress for some time, "
                "you hear the faint sound of water running.")
    print_pause("There must be a river or stream ahead.")
    print_pause("There is another series of howls.")
    print_pause("This time it sounds like they are farther away.")
    print_pause("You must be moving in the right direction.")
    print_pause("The sound of running water gets louder.")
    print_pause("You stop, "
                "there is a someone sitting against a tree in front of you.")
    print_pause("You ask who they are, there's no answer.")
    print_pause("You move closer and repeat yourself. No answer.")
    print_pause("After moving closer again, you smell death.")
    print_pause("Their eyes are milky, they're dead.")
    print_pause("There is no blood or marks on the corpse.")
    print_pause("However, "
                "there are some mushrooms a few feet away from the corpse.")
    print_pause("Those mushrooms must have killed whoever this is.")
    print_pause("That could be useful.")
    right_dilemma(items, werewolf_status)


def right_dilemma(items, werewolf_status):
    print_pause("There's still a hatchet in the corpse's left hand.")
    print_pause("More useful than mushrooms!")
    print("You hear another series of howls, they're much closer this time.")
    choice_5 = valid_input("You have to get moving, now!\n"
                           "Take something before you go!\n"
                           "1. The hatchet is obviously more useful "
                           "than mushrooms.\n"
                           "2. The mushrooms could be better....maybe.",
                           ["1", "2"])
    if choice_5 == '1':
        print_pause("You grab the hatchet and run!")
        items.append("hatchet")
    elif choice_5 == '2':
        print_pause("You grab a mushroom and run!")
        items.append("mushroom")
    print_pause("Running forward for several minutes, "
                "you finally come to the river you were hearing.")
    right_split_decision(items, werewolf_status)


def right_split_decision(items, werewolf_status):
    print_pause("You rush into the water and "
                "wade across the river as fast as you can.")
    print_pause("After making it to the other side you pause and "
                "look behind you.")
    print_pause("You don't see anything, "
                "but as you turn around there is a rustling in some bushes.")
    print_pause("Something rushes at you and knocks you down. "
                "It's a werewolf!")
    print_pause("It gets on top of you, think fast!")
    if "mushroom" in items:
        print_pause("You try to shove the mushroom into the werewolf's mouth!")
        mushroom_roll = random.randint(1, 6)
        mushroom_roll
        if mushroom_roll >= 4:
            print_pause("You force the mushroom into the werewolf's mouth and "
                        "kick it off you.")
            print_pause("You scramble up and look at the beast, "
                        "it's locking eyes with you and circling you.")
            print_pause("Suddenly, its eyes widen and it grasps at its throat."
                        " It's suffocating.")
            print_pause("Knowing that the beast is going to die you turn and "
                        "bolt before more show up.")
            werewolf_status.append("dead")
            right_end()
        elif mushroom_roll <= 3:
            print_pause("You're too slow and the werewolf bites down on "
                        "your neck.")
            print_pause("It rips your throat out and everything fades to "
                        "black.")
            print_pause("GAME OVER!")
            play_again()
    if "hatchet" in items:
        print_pause("You try to strike the werewolf with the hatchet!")
        hatchet_roll = random.randint(1, 6)
        hatchet_roll
        if hatchet_roll >= 4:
            print_pause("You hit the werewolf in the face with the hatchet.")
            print_pause("blood gushes out and the beast goes limp and "
                        "falls on you.")
            print_pause("It's dead. You push its corpse off you, "
                        "and rush off before more show up.")
            werewolf_status.append("dead")
            right_end()
        elif hatchet_roll <= 3:
            print_pause("You're too slow and the werewolf bites down on "
                        "your neck.")
            print_pause("It rips your throat out and everything fades to "
                        "black.")
            print_pause("GAME OVER!")
            play_again()


def right_end():
    print_pause("After running until you feel like you're going to collapse, "
                "you notice that the forest is starting to thin.")
    print_pause("You stop and catch your breath. After a few moments you "
                "continue forward at a jog.")
    print_pause("The forest continues to thin, finally the forest opens up "
                "into farmland.")
    print_pause("You've made it out!")
    play_again()


play_game()
