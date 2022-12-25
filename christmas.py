# Christmas wish with my programming skill.
import termcolor
import os
import time

# Preview of the program.
'''                 
                       * <--- This one will blink :)
                      * *     
                     *   *
                    *     *
                   *       *  
                  *         *
                   **     **  
                  **       **
                 **         ** 
                **           **
               **             **
              **               **
                  ***     ***    
                 ***       *** 
                ***         *** 
               ***           ***
              ***             ***
             ***               ***
                 ****     ****  
                ****       ****
               ****         ****
              ****           **** 
             ****             ****
            ****               ****       
                    *******             
                    *******             
                    *******                    
[////\\\\////\\\\////\\\\////\\\\////\\\\////\\]
[////\\\\////\\\\////\\\\////\\\\////\\\\////\\]
[////\\\\////\\\\////\\\\////\\\\////\\\\////\\]
'''


def loading_screen():

    text = '\n\nL o a d i n g ...'
    count = 1
    text_count = len(text)
    colours = ['blue', 'green', 'red', 'yellow', 'cyan', 'magenta',
               'blue', 'green', 'red', 'yellow', 'cyan', 'magenta',
               'blue', 'green', 'red', 'yellow', 'cyan', 'magenta',
               'blue', 'green', 'red', 'yellow', 'cyan', 'magenta']

    while text_count >= 0:

        print(termcolor.colored(text[0:count], colours[count]))
        count += 1
        text_count -= 1
        time.sleep(0.2)
        os.system('clear')

    # Rocket launching process.
    boarder = 30

    while boarder >= 0:

        print('\n' * boarder)
        print(termcolor.colored(
            '                                  / \\             ', 'yellow'))
        print(termcolor.colored(
            '                                  [ ]              ', 'blue'))
        print(termcolor.colored(
            '                                  [ ]              ', 'blue'))
        print(termcolor.colored(
            '                                  [ ]              ', 'blue'))
        print(termcolor.colored(
            '                                 /| |\\            ', 'blue'))
        print(termcolor.colored(
            '                                  !!!              ', 'red', attrs=['blink']))
        time.sleep(0.15)
        os.system('clear')
        boarder -= 1


# Christmas tree part.
def christmas_tree():

    colours = ['blue', 'green', 'red', 'yellow', 'cyan', 'magenta']

    # Star in the  of the tree.
    print(termcolor.colored(' ' * 31 + '*', 'yellow', attrs=['blink']))

    astrix_list = ['*', '**', '***', '****']

    # Let's generate leaves of the tree.
    def leaves(space_count, x, i, mark, color):

        # For spaces.
        while space_count >= x:

            print(termcolor.colored('\t\t'+' ' * space_count + mark +
                  ' ' * i + mark, color))
            space_count -= 1
            i += 2
            time.sleep(0.15)

    # Let's make the trunk of the tree.
    def trunk():

        for _ in range(3):

            print(termcolor.colored(' ' * 28 + '*******', 'green'))
            time.sleep(0.15)

    def gifts():

        banner = [['''      [////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\]'''],
                  ['''      [\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////]'''],
                  ['''      [////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\]'''],
                  ['''      [\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////\\\\\\\\////]''']]

        x = 0

        for i in banner:

            print(termcolor.colored(str(i[0]), colours[x]))
            time.sleep(0.15)
            x += 1

    leaves(14, 9, 1, astrix_list[0], color=colours[0])
    leaves(12, 7, 3, astrix_list[1], color=colours[4])
    leaves(10, 5, 5, astrix_list[2], color=colours[0])
    leaves(8, 3, 7, astrix_list[3], color=colours[4])
    trunk()
    gifts()


# Greeting text part.
def greeting():

    time.sleep(0.2)

    banner = '''
███    ███ ███████ ██████  ██████  ██    ██      ██████ ██   ██ ██████  ██ ███████ ████████ ███    ███  █████  ███████ 
████  ████ ██      ██   ██ ██   ██  ██  ██      ██      ██   ██ ██   ██ ██ ██         ██    ████  ████ ██   ██ ██      
██ ████ ██ █████   ██████  ██████    ████       ██      ███████ ██████  ██ ███████    ██    ██ ████ ██ ███████ ███████ 
██  ██  ██ ██      ██   ██ ██   ██    ██        ██      ██   ██ ██   ██ ██      ██    ██    ██  ██  ██ ██   ██      ██ 
██      ██ ███████ ██   ██ ██   ██    ██         ██████ ██   ██ ██   ██ ██ ███████    ██    ██      ██ ██   ██ ███████ '''

    print(termcolor.colored(banner, 'blue', attrs=['blink']))


# Main program.
if __name__ == '__main__':

    os.system('clear')
    loading_screen()
    christmas_tree()
    greeting()
