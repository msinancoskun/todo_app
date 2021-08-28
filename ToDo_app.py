class App:

    def __init__(self, hierarchy=0):
        """ Initialization class method. """
        self.todo_list = []
        self.hierarchy = hierarchy
        self.create_list()

    def create_list(self):
        """ This method is used to create a TO-DO list."""
        print("Welcome to your TODO list...")

        if len(self.todo_list) < 1:
            print("The list has no items in it.")
            print("Do you want to add items?")
            add_items = input("Y/N? ").upper()
            if add_items == 'Y':
                num_todo = input("How many things you want to do?\n")
                while True:
                    todo = input("What do you want to add?\n")
                    if todo not in self.todo_list:
                        self.todo_list.append(todo)
                        if len(self.todo_list) == int(num_todo):
                            print("You have enough things to do, go do it!")
                            self.show_list()
                            self.create_text_file()
                            break
                    else:
                        print("You already have {} in your list".format(todo))
                        self.show_list()

            else:
                print("You choose NO!")

    def show_list(self):
        """ This method is used to create a show the TO-DO list items according to hierarchy. """
        index = 1
        for list_item in self.todo_list:
            print("{}.{}".format(index, list_item))
            index += 1

    def create_text_file(self):
        """ This method creates a text file containing the TO-DO list in directory."""
        with open('TODO_list', 'w') as file:
            index = 1
            for list_item in self.todo_list:
                line = "{}.{}".format(index, list_item)
                index += 1
                file.write(line + '\n')
        file.close()


if __name__ == '__main__':
    app = App()
