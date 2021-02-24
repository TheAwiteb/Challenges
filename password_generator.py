import string
from random import choice
import curses
from curses import textpad
from time import sleep
import os

password_menu = ['UpperCase','LowerCase','Numbers','Symbolic','Save file','Next']
password_values = {'UpperCase':True, 'LowerCase':True,'Numbers': True, 'Symbolic':True,
                    'Save file':False}

properties_menu = ['File Name','Length','Amount','Done']
properties_values = {'File Name':'','Length':0,'Amount':0}

def have_true():
    for key,val in password_values.items():
        if key == 'Save file':
            continue
        else:
            if val:
                return True
            else:
                pass
    return False

def print_password_list(stdscr,password_list):
    stdscr.clear()
    curses.curs_set(1)
    h,w = stdscr.getmaxyx()
    stdscr.refresh()
    
    try:
        x =1
        y = 3
        for password in password_list:
            if y == h-2:
                x+=len(password)+1
                y = 3
            stdscr.addstr(y,x,password)
            y+=1
            
        stdscr.addstr(0,0,"Press 'Q' to exit")
    except:
        stdscr.addstr(0,0,"ERROR!")
    while True:
        key = stdscr.getch()
        if key == ord('q') or key == ord('Q'):
            break
def password_generator(stdscr,upper=True, lower=True, nums=True, syms=True, length=10,\
    amount=10, save_file= False, file_name='password.txt'):
    chars = ""
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase
    if nums:
        chars += string.digits
    if syms:
        chars += "!()*&_$@#{}"
    passwords_list = []
    if chars == "":
        pass
    else:
        for i in range(amount):
            while True:
                password = ''.join(choice(chars) for i in range(length))
                if upper or lower:
                    if password[0] not in "!()*&_$@#{}"+string.digits:
                        passwords_list.append(password)
                        break
                    else:
                        continue
                else:
                    passwords_list.append(password)
                    break
        if save_file:
            with open(file_name,'a+') as password_file:
                for password in passwords_list:
                    password_file.write(f"{password}\n")
        else:
            print_password_list(stdscr, passwords_list)
            
def textBox(stdscr,text_y: int, text_x: int) -> str:
    ncols, nlines = 18, 1 #العرض، والطول
    box_y, box_x = text_y, text_x+1 # الاحداثيات

    win = curses.newwin(nlines, ncols, box_y, box_x) #انشاء النافذة
    textpad.rectangle(stdscr, box_y-1, box_x-1, box_y + nlines, box_x + ncols) #السماح بالكتابة عليها
    box = textpad.Textbox(win)
    stdscr.refresh()
    return box.edit()


def print_password_menu(stdscr: ' curses.window', selected_word: int, title = "Click on the option to change value"):
    try:
        stdscr.clear()
        h,w = stdscr.getmaxyx()
        #title
        title_x = w//2 - len(title)//2 + 1
        title_y = h//2 - len(password_menu)//2 - 2
        stdscr.addstr(title_y, title_x, title, curses.A_BOLD)
        

        #menu
        for idx, word in enumerate(password_menu):
            x = w//2 - len(word)//2
            y = h//2 - len(password_menu)//2 + idx
            
            if idx == len(password_menu)-1:
                stdscr.addstr(y+1, x+8, word,curses.A_BOLD if idx == selected_word else curses.A_DIM)
            else:    
                stdscr.addstr(y,x,f"{word} {'✓' if password_values[word] else '✕'}",curses.A_BOLD if idx == selected_word else curses.A_DIM)
        #refresh
        stdscr.refresh()
    except Exception as e:
        stdscr.clear()
        stdscr.addstr(0,0,"The window very small" if str(e) == "addwstr() returned ERR" else f"ERROR! {str(e)}")
    return stdscr.getmaxyx()


def print_second(stdscr: ' curses.window', selected_word: int,title = ''):
    try:
        if password_values['Save file']:
            pass
        else:
            del properties_values['File Name']
            del properties_menu[0]
    except:
        pass
    try:
        stdscr.clear()
        h,w = stdscr.getmaxyx()
        #title
        title_x = w//2 - len(title)//2 + 1
        title_y = h//2 - len(properties_menu)//2 - 2
        stdscr.addstr(title_y, title_x, title, curses.A_BOLD)

        #menu
        for idx, word in enumerate(properties_menu):
            if word == "File Name" and not password_values['Save file']:
                continue
            x = w//2 - len(word)//2
            y = h//2 - len(properties_menu)//2 + idx
            
            if idx == len(properties_menu)-1:
                stdscr.addstr(y+1, x+8, word,curses.A_BOLD if idx == selected_word else curses.A_DIM)
            else:
                stdscr.addstr(y,x, word, curses.A_BOLD if idx == selected_word else curses.A_DIM)
        #refresh
        stdscr.refresh()
    except Exception as e:
        stdscr.clear()
        stdscr.addstr(0,0,"The window very small" if str(e) == "addwstr() returned ERR" else f"ERROR! {str(e)}")
    return stdscr.getmaxyx()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) #لون عندما يتم اختيار الكلمة
    word_idx = 0    
    Coordinates_password_menu = print_password_menu(stdscr,word_idx)
    print_win = print_password_menu
    while True:
        key = stdscr.getch() #اخذ الزر المضغوط
        if Coordinates_password_menu != stdscr.getmaxyx(): #اذا تم تغير حجم الشاشة يحدث حجم القائمة
            Coordinates_password_menu = print_win(stdscr,word_idx)
        else:
            pass

        if key == curses.KEY_DOWN:
            if word_idx < len(password_menu) -1:
                word_idx +=1
            else:
                word_idx = 0
            print_win(stdscr,word_idx)
            
        elif key == curses.KEY_UP:
            if word_idx > 0:
                word_idx -=1
            else:
                word_idx = len(password_menu)-1
            print_win(stdscr,word_idx)

        elif key == curses.KEY_ENTER or key in [10,13]:
            if word_idx == len(password_menu) -1:
                if have_true():
                    print_second(stdscr,0)
                    break
                else:
                    print_win(stdscr,word_idx,title="You cannot create a password that does not contain anything !!")
            else:
                password_values[list(password_values)[word_idx]] = not password_values[list(password_values)[word_idx]]
                print_win(stdscr,word_idx)
        stdscr.refresh()
    
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) #لون عندما يتم اختيار الكلمة
    word_idx = 0    
    Coordinates_password_menu = print_second(stdscr,word_idx)
    print_win = print_second
    while True:
        key = stdscr.getch() #اخذ الزر المضغوط
        if Coordinates_password_menu != stdscr.getmaxyx(): #اذا تم تغير حجم الشاشة يحدث حجم القائمة
            Coordinates_password_menu = print_win(stdscr,word_idx)
        else:
            pass

        if key == curses.KEY_DOWN:
            if word_idx < len(properties_menu) -1:
                word_idx +=1
            else:
                word_idx = 0
            print_win(stdscr,word_idx)
            
        elif key == curses.KEY_UP:
            if word_idx > 0:
                word_idx -=1
            else:
                word_idx = len(properties_menu)-1
            print_win(stdscr,word_idx)

        elif key == curses.KEY_ENTER or key in [10,13]:
            if word_idx == len(properties_menu) -1:
                if properties_values['Length'] != 0 and properties_values['Amount'] != 0:
                    if password_values['Save file']:
                        if properties_values['File Name'] != '':
                            break
                    else:
                        break
                print_win(stdscr,word_idx,title="Please fill out all options")
            else:
                h,w = stdscr.getmaxyx()
                box_x = w//2 - 15
                box_y = h//2 - len(properties_menu)//2 + len(properties_menu)
                
                text = f"Enter {list(properties_values)[word_idx]} {'end of the path .txt' if list(properties_menu)[word_idx] == 'File Name' else 'just number'}"
                print_win(stdscr,word_idx,title=text)
                val = textBox(stdscr,box_y,box_x).strip()
                if list(properties_menu)[word_idx] == 'File Name':
                    if val.endswith('.txt'):
                        if os.path.lexists(val):
                            print_win(stdscr,word_idx,title="Path is exists pleas try again.!")
                        else:
                            properties_values[list(properties_values)[word_idx]] = val
                            print_win(stdscr,word_idx,title=f'Done {val}')
                    else:
                        print_win(stdscr,word_idx,title="end of file neme must be .txt")
                else:
                    try:
                        val = int(val)
                        if val <= 0:
                            print_win(stdscr,word_idx,title=f"Password {list(properties_menu)[word_idx]} must be greater than zero!")
                        else:
                            properties_values[list(properties_values)[word_idx]] = val
                            print_win(stdscr,word_idx,title=f'Done {list(properties_menu)[word_idx]} is {val}')
                    except ValueError:
                        print_win(stdscr,word_idx,title="pleas enter just number!")
        stdscr.refresh()        
    password_generator(stdscr=stdscr,upper=password_values['UpperCase'],lower=password_values['LowerCase'],
                        nums=password_values['Numbers'],syms=password_values['Symbolic'],
                            length=properties_values['Length'],amount=properties_values['Amount'],
                                save_file=password_values['Save file'], file_name=properties_values['File Name'] if password_values['Save file'] else '')

curses.wrapper(main)
