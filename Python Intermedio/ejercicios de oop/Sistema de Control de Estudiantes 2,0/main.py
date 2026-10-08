import menu
import actions

def main():
    student_list=actions.StudentList()
    menu.menu(student_list)

if __name__ == '__main__':
    main()