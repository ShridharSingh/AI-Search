class ReadFile:
    def __init__(self, f):
        self.text_file = f

    def read(self):
        mazeswamp = []

        with open(self.text_file, 'r') as f:
            f_content = f.readlines()

        for row in range(int(f_content[0])):
            str = f_content[row + 2]
            splitstr = str.split()
            mazeswamp.append(splitstr)
            #print(row)
            print(mazeswamp)

        return mazeswamp




    def StartPoint(self):
        starting_point = []
        drySpace = 'D'
        wetSpace = 'W'
        point = 0
        sp = self.read()
        #print(sp)
        sp_len = len(sp)
        #print(sp_len)

        for i in range(sp_len):
            print(i)

            if sp[point][0] == drySpace:
                starting_point.append([i, 0])
            point+=1

        return starting_point

    def EndPoint(self):
        end_point = []
        drySpace = 'D'
        wetSpace = 'W'
        point = 0
        ep = self.read()
        #print(ep)
        ep_len = len(ep)
        #print(ep_len)

        for i in range(ep_len):
            #limiter test
            if ep[point][len(ep[0])-1] == drySpace:
                end_point.append([i, len(ep[0])-1])

            point+=1
        return end_point

    '''Checking Visited'''
    def BooleanArray(self, b_array):
        visited = []
        temp_visit = []
        for row in b_array:
            for col in row:
                if col == 'W':
                    temp_visit.append(True)
                else:
                    temp_visit.append(False)
            visited.append(temp_visit)
            temp_visit = []
        return visited



""" def openFile(self):
        with open(self.file, 'r') as f:
            f_rows = int(f.readline())
            f_cols = int(f.readline())

            f_maze = f.readlines();
            for row in range(f_rows):
                f_m = f_maze[row]
                f_split = f_m.split()
                env.append(f_split)
"""
