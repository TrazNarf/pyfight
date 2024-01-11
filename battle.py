import random
import time

loop = True
hp = 10
enemyhp = 10
print("Enemy attacking!")
while loop == True:
    act = input("Fight or Item? ")
    if act == "fight":
        atkdam = random.randint(1, 3)
        crit = random.randint(1, 10)
        if crit == 10:
            print("Critical Hit!")
            atkdam = random.randint(4, 6)
        time.sleep(1)
        print("The attack did", atkdam, "damage!")
        enemyhp = enemyhp - atkdam
        time.sleep(1)
        if enemyhp < 1:
            print("you win!")
            time.sleep(0.5)
            done = input("do you want to play again? (y/n) ")
            if done == "y":
                time.sleep(0.5)
                hp = 10
                enemyhp = 10
                print("Enemy attacking!")
            elif done == "n":
                loop = False
                time.sleep(0.5)
        else:
            print("the enemy has", enemyhp, "hp left.")
            time.sleep(0.5)
            print("enemy turn.")
            time.sleep(0.8)
            enemyturn = random.randint(1, 4)
            if enemyturn != 4:
                enemyatk = random.randint(1, 5)
                print("the enemy attacks!")
                time.sleep(1)
                print("it did", enemyatk, "damage.")
                hp = hp - enemyatk
                time.sleep(0.7)
                if hp < 1:
                    print("You died!")
                    time.sleep(0.5)
                    done = input("do you want to play again? (y/n) ")
                    if done == "y":
                        time.sleep(0.5)
                        hp = 10
                        enemyhp = 10
                        print("Enemy attacking!")
                    elif done == "n":
                        loop = False
                        time.sleep(0.5)
                else:
                    print("you have", hp, "hp left.")
                    time.sleep(0.5)
            elif enemyturn == 4:
                enemyheal = random.randint(1, 3)
                print("the enemy used an item!")
                time.sleep(0.8)
                enemyhp = enemyhp + enemyheal
                if enemyhp > 10:
                    enemyhp = 10
                print("the enemy has", enemyhp, "hp left.")
                time.sleep(1)
    elif act == "item":
        heal = random.randint(1, 3)
        time.sleep(0.5)
        hp = hp + heal
        if hp > 10:
            hp = 10
        print("you healed", heal, "hp!")
        time.sleep(0.5)
        print("you have", hp, "hp remaining.")
        time.sleep(0.4)
        print("enemy turn.")
        time.sleep(0.8)
        enemyturn = random.randint(1, 4)
        if enemyturn != 4:
            enemyatk = random.randint(1, 5)
            print("the enemy attacks!")
            time.sleep(1)
            print("it did", enemyatk, "damage.")
            hp = hp - enemyatk
            time.sleep(0.7)
            if hp < 1:
                print("You died!")
                time.sleep(0.5)
                done = input("do you want to play again? (y/n) ")
                if done == "y":
                    time.sleep(0.5)
                    hp = 10
                    enemyhp = 10
                    print("Enemy attacking!")
                elif done == "n":
                    loop = False
                    time.sleep(0.5)
            else:
                print("you have", hp, "hp left.")
                time.sleep(0.5)
        elif enemyturn == 4:
            enemyheal = random.randint(1, 3)
            print("the enemy used an item!")
            time.sleep(0.8)
            enemyhp = enemyhp + enemyheal
            print("the enemy healed", enemyheal, "hp.")
            time.sleep(0.8)
            print("the enemy has", enemyhp, "hp left.")
            time.sleep(1)