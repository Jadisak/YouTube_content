from pickle import dump, load
print('\t\t—— Welcome ——\t\t')
while True:
    print('What you wanna do?\n1.Add Task\n2.See saved Tasks\n3.Remove every Task\n4.Quit')
    answer = int(input('Enter numbers only[i.e, 1, 2, 3, 4 etc.]\t:'))
    if answer==1:
        try:
            task_to_add = str(input('Enter Task:\t'))
            dump(task_to_add, open('tasks.dat', 'wb'))
            print('Success !!')
        except Exception as e:
            print(f'Oops !! {e}')
    elif answer == 2:
        try:
            load_task = load(open('tasks.dat', 'rb'))
            for line in load_task:
                print(f'These are the saved tasks:\n\t{load_task}')
        except Exception as e:
            print(f'Oops !! {e}')
    elif answer == 3:
        try:
            print('Under development')
        except Exception as e:
            print(f'Oops !! {e}')
    elif answer == 4:
        print('Thanks for using !!')
        exit()