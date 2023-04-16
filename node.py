class Node:
    Nodes = []

    def __init__(self, nodeid: int = 0, coord: tuple = (0, 0), dof: dict = None, force: dict = None):
        self.nodeid = nodeid
        self.coord = coord
        self.dof_num = dict.fromkeys(['uy', 'theta'])
        self.dof = dict.fromkeys(['uy', 'theta'])
        self.force = dict([('Fy', 0), ('Mz', 0)])

        if dof:
            self.setdisplacement(dof)
        if force:
            self.setforce(force)

        self.Nodes.append(self)

    def __str__(self):
        return f'Node ID={self.nodeid}, coord={self.coord}, dof_num={self.dof_num}, force={self.force}'

    def __repr__(self):
        return f'Node(nodeid={self.nodeid}, ' \
               f'coord={self.coord}, ' \
               f'dof_num={self.dof_num}, ' \
               f'force={({k:round(v, 2) for k,v in self.force.items()})})'

    def setdisplacement(self, displacement: dict):
        for dsp, val in displacement.items():
            self.dof[dsp] = val

    def setforce(self, force: dict):
        for dsp, val in force.items():
            self.force[dsp] = val

    @staticmethod
    def listall():
        for node in Node.Nodes:
            print(node)

    @staticmethod
    def update_dof_num():
        cur_dof_num = 1
        for node in Node.Nodes:
            if node.dof.get('uy', None) == None:
                node.dof_num['uy'] = cur_dof_num
                cur_dof_num += 1
            if node.dof.get('theta', None) == None:
                node.dof_num['theta'] = cur_dof_num
                cur_dof_num += 1
