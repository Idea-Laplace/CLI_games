import os
import time as t
import keyboard as k

lan = 0
title = ("CLI DUNGEON", "CLI 던전")
main = [("Start", "시작"), ("Setting", "설정"), ("Information", "게임설명"), ("Challenges", "도전과제"), ("EXIT", "종료")]
lan_start = [("Create a name of the player", "플레이어의 이름을 지어주세요"),
             ("You input '{}', will you continue? (y/n) : ", "{}의 이름으로 계속하시겠습니까? (y/n) : ")]
lan_info = [("", ""), ("Movement: Arrow Keys", "이동: 방향키"),
            ("Character Profile: P", "캐릭터 정보: P"),
            ("Map: M", "지도: M"),
            ("Communication with object or NPC : Z", "물체 또는 NPC와의 상호작용: Z"),
            ("Quit communication: X", "대화 종료: X"),
            ("Back to main menu: ESC", "메인화면으로: ESC")]
lan_setting = ("English", "한국어")
lan_challenges = [["Pacifist", "평화주의자"], ["Genocide", "학살자"],
                  ["Nothing is meaningless", "의미 없는 것에 대한 예찬"],
                  ["Don't bother me", "귀찮게 하지 마"],
                  ["Time is a game", "시간은 게임이다"],
                  ["OCD", "강박증"],
                  ["THE RULE BREAKER", "틀을 깨는 자"],
                  ["Janus", "천의 얼굴"],
                  ["The time when you should stop", "이제 그만해도 됩니다"]]
clear = [["Locked", "잠김"], ["Unlocked", "달성함"]]


class Player:
    def __init__(self, name):
        self.name = name


def game():
    print("\nThe game is not developed yet, please wait.")
    input()


def setting():
    global lan
    loop = True
    os.system("cls")
    for i in range(3):
        print()
    print(" " * 10 + f"{title[lan]}\n")
    print(f"          <     {lan_setting[lan]}     >")
    while loop:
        if k.is_pressed(75):
            os.system("cls")
            lan = (lan + 1) % 2
            for i in range(3):
                print()
            print(" " * 10 + f"{title[lan]}\n")
            print(f"          <     {lan_setting[lan]}     >")
            t.sleep(0.2)
        if k.is_pressed(77):
            os.system("cls")
            lan = (lan + 1) % 2
            for i in range(3):
                print()
            print(" " * 10 + f"{title[lan]}\n")
            print(f"          <     {lan_setting[lan]}     >")
            t.sleep(0.2)
        while k.is_pressed('esc'):
            loop = False
            break
    return main_window()


def start():
    try:
        k.add_hotkey('esc', lambda: k.send("ctrl+c"))
        # Make an account
        while True:
            os.system("cls")
            for i in range(3):
                print()
            print(" " * 10 + f"{title[lan]}\n")
            player = Player(input(f"          > {lan_start[0][lan]} : "))
            if player.name:
                while True:
                    print()
                    confidence = input(" " * 10 + lan_start[1][lan].format(player.name))
                    if confidence not in ["Y", "y", "N", "n"]:
                        print("          > input y or n.")
                        t.sleep(1.5)
                        break
                    elif confidence.lower() == 'y':
                        os.system("cls")
                        return game()
                    else:
                        break

    except KeyboardInterrupt:
        k.unhook_all_hotkeys()
        return main_window()

    finally:
        k.unhook_all_hotkeys()


def information():
    os.system("cls")
    for i in range(3):
        print()
    print(" " * 10 + f"{title[lan]}\n")
    for i in range(len(lan_info)):
        print(f"          {lan_info[i][lan]}\n")
    k.wait('esc')
    return main_window()


def challenges():
    locate_1 = 0
    os.system("cls")
    temp = list(map(lambda x: x[lan], lan_challenges))
    temp[locate_1] = temp[locate_1]+" <"
    for i in range(3):
        print()
    print(" " * 10 + f"{title[lan]}\n\n\n")
    for i in range(len(temp)):
        print(" " * 10 + temp[i], end="\n\n")
    loop = True
    while loop:
        # up
        if k.is_pressed(72):
            temp[locate_1] = temp[locate_1][:-2]
            locate_1 = (locate_1 - 1) % len(temp)
            temp[locate_1] = temp[locate_1] + " <"
            os.system("cls")
            for i in range(3):
                print()
            print(" " * 10 + f"{title[lan]}\n\n\n")
            for i in range(len(temp)):
                print(" " * 10 + temp[i], end="\n\n")
            t.sleep(0.2)

        # down
        if k.is_pressed(80):
            temp[locate_1] = temp[locate_1][:-2]
            locate_1 = (locate_1 + 1) % len(temp)
            temp[locate_1] = temp[locate_1] + " <"
            os.system("cls")
            for i in range(3):
                print()
            print(" " * 10 + f"{title[lan]}\n\n\n")
            for i in range(len(temp)):
                print(" " * 10 + temp[i], end="\n\n")
            t.sleep(0.2)

        if k.is_pressed('esc'):
            loop = False
    return main_window()


def main_window():
    os.system("cls")
    for i in range(3):
        print()
    print(" " * 10 + f"{title[lan]}\n\n\n")
    menu = [main[0][lan] + " <", main[1][lan], main[2][lan], main[3][lan], main[4][lan]]
    for i in range(len(menu)):
        print(" " * 10 + menu[i], end="\n\n")

    # Keyboard input

    loop = True
    position = 0

    while loop:
        # up
        if k.is_pressed(72):
            menu[position] = menu[position][:-2]
            position = (position - 1) % 5
            menu[position] = menu[position] + " <"
            os.system("cls")
            for i in range(3):
                print()
            print(" " * 10 + f"{title[lan]}\n\n\n")
            for i in range(len(menu)):
                print(" " * 10 + menu[i], end="\n\n")
            t.sleep(0.2)
        # down

        if k.is_pressed(80):
            menu[position] = menu[position][:-2]
            position = (position + 1) % 5
            menu[position] = menu[position] + " <"
            os.system("cls")
            for i in range(3):
                print()
            print(" " * 10 + f"{title[lan]}\n\n\n")
            for i in range(len(menu)):
                print(" " * 10 + menu[i], end="\n\n")
            t.sleep(0.2)
        # enter
        if k.is_pressed("enter"):
            if position == 0:
                return start()
            elif position == 1:
                return setting()
            elif position == 2:
                return information()
            elif position == 3:
                return challenges()
            else:
                loop = False


main_window()
