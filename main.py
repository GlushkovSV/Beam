from node import Node
from elem import Elem


def calc():
    node1 = Node(nodeid=1, coord=(0, 0))
    node2 = Node(nodeid=2, coord=(3, 0))
    node3 = Node(nodeid=3, coord=(5, 0))

    elem1 = Elem(elemid=1,
                 nodelist=[node1, node2],
                 material={'Exx': 1,
                           'prxy': 0.3},
                 Iyy=1)
    elem2 = Elem(elemid=2,
                 nodelist=[node2, node3],
                 material={'Exx': 1,
                           'prxy': 0.3},
                 Iyy=1)

    # elem2.setnodes(nodelist=[node2, node3])
    # elem1.setmaterial({'Exx': 1, 'prxy': 0.3})
    # elem1.setinertia(Iyy=1)
    # elem2.setmaterial({'Exx': 1, 'prxy': 0.3})
    # elem2.setinertia(Iyy=1)

    # Node.listall()
   # Node.update_dof_num()
    # Node.listall()

    # Elem.listall()
    # print(*elem1.stiffnes, sep='\n')
    # print(elem1.getindex())

    # print(*elem2.stiffnes, sep='\n')
    # print(elem2.getindex())

    elem1.set_distributed_force(q=-10)
    node3.setforce(force={'Fy': 0, 'Mz': -15})

    node1.setdisplacement(displacement={'uy': 0, 'theta': 0})
    node3.setdisplacement(displacement={'uy': 0})
    Node.update_dof_num()

    Elem.listall()

if __name__ == '__main__':
    calc()
    exit(0)
