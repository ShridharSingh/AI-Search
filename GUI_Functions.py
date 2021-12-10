from tkinter import filedialog
from Searching import *
from tkinter import *
from ReadFile import *

class GUI_Functions:

    def __init__(self):
        self.search_type=None
        self.filepath = None
        self.list = None

    def OpenTextFile(self):
        f_path = filedialog.askopenfilename(title="Select File", filetypes=(("text", "*txt"), ("all files", "*.*")))
        file = ReadFile(f_path)
        self.filepath = file
        #print(file.read())
        print(f_path)



    #def ReadFile(self):
    #    with open("swamp1.txt") as f:
    #            #f_content = f.read().split()
    #            f_content = f.readlines();
    #            #numrows = f_content.pop(0)
    #            #numcols = f_content.pop(0)
    #            mazeswamp = []


    #            for row in range (int(f_content[0])):
    #                    str = f_content[row+2]
    #                    splitstr = str.split()
    #            mazeswamp.append(splitstr)
    #    print(mazeswamp)
    #    return mazeswamp



    def breathFirst(self):
        file = self.filepath
        if(file!=None):
            Start_State = file.StartPoint()
            End_State = file.EndPoint()
            # print(Start_State)
            # print(End_State)


            check_arr = file.read()
            # print(check_arr)

            valid_Moves = file.BooleanArray(check_arr)
            p = Problem(Start_State, valid_Moves, End_State)


            self.list = breadth_first_graph_search(p)
            self.search_type = "Breath-First Search"
            self.OnButtonClick()
            print(self.list)
        else:
            self.OnButtonClick()






    def depthFirst(self):
        file = self.filepath
        if (file != None):
            Start_State = file.StartPoint()
            End_State = file.EndPoint()
            # print(Start_State)
            # print(End_State)

            check_arr = file.read()
            #print(check_arr)

            valid_Moves = file.BooleanArray(check_arr)
            p = Problem(Start_State, valid_Moves, End_State)


            self.list = depth_first_graph_search(p)
            self.search_type = "Depth-First Search"
            self.OnButtonClick()
            print(self.list)
        else:
            self.OnButtonClick()


    def bestFirst(self):
        file = self.filepath
        if (file != None):
            Start_State = file.StartPoint()
            End_State = file.EndPoint()
            # print(Start_State)
            # print(End_State)

            check_arr = file.read()
            # print(check_arr)


            valid_Moves = file.BooleanArray(check_arr)

            p = Problem(Start_State, valid_Moves, End_State)
            N = Node(Start_State[0])


            self.list = best_first_graph_search(p,N)
            self.search_type = "Best-First Search"
            self.OnButtonClick()
            print(self.list)
        else:
            self.OnButtonClick()


    def aStar(self):
        file = self.filepath
        if (file != None):
            Start_State = file.StartPoint()
            End_State = file.EndPoint()
            # print(Start_State)
            # print(End_State)

            check_arr = file.read()
            # print(check_arr)


            valid_Moves = file.BooleanArray(check_arr)

            p = Problem(Start_State, valid_Moves, End_State)
            N = Node(Start_State[0])


            self.list = astar_search(p,N)
            self.search_type = "A* Search"
            self.OnButtonClick()
            print(self.list)
        else:
            self.OnButtonClick()


    def OnButtonClick(self):
        popUp = Toplevel()
        popUp.title("AI Search")
        popUp.geometry("400x200")

        if(self.filepath!=None):
            space = Label(popUp, text=" ")
            space.pack()

            space = Label(popUp, text=" ")
            space.pack()

            Label1 = Label(popUp, text=self.search_type, fg="white", bg="gray")
            Label1.pack()

            space = Label(popUp, text=" ")
            space.pack()

            Label2 = Label(popUp, text= self.list)
            Label2.pack()
        else:
            space = Label(popUp, text=" ")
            space.pack()

            space = Label(popUp, text=" ")
            space.pack()

            Label1 = Label(popUp, text="Please load swamp file", fg="white", bg="gray")
            Label1.pack()



    def Report(self):
        filePath = filedialog.askopenfilename(title="Select File", filetypes=(("text", "*txt"), ("all files", "*.*")))
        with open(self.filepath, 'r') as f:
            report = f.readlines()

        popUp = Toplevel()
        popUp.title("AI Search Report")
        popUp.geometry("500x500")




        Label3 = Label(popUp, text=report)
        Label3.pack()



    def close(self):
        self.filepath=None
