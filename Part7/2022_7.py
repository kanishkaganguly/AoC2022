#/usr/bin/env python3
from treelib import Node, Tree

input_txt = "Part7/2022_7.txt"

class FileDescriptor(object):
    def __init__(self, filetype:str, size:int=0):
        self.filetype = filetype
        self.size = size
    
    def __str__(self):
        return f"FileDescriptor({self.filetype}, {self.size})"
    
    def __repr__(self):
        return self.__str__()
    
    def get_type(self):
        return self.filetype
    
    def get_size(self):
        return self.size

tree = Tree()
tree.create_node("/", "/", data=FileDescriptor('dir'))
curr_level:Node = tree.get_node("/")

with open(input_txt) as f:
    data = f.readlines()
    for line in data:
        cmd = line.strip().split(" ")
        # Check for command
        if cmd[0] == "$":
            # Check for cd
            if cmd[1] == 'cd':
                print(f"Doing cd to {cmd[2]}")
                # Move up directory
                if cmd[2] == '..':
                    if curr_level.identifier == '/':
                        print("Cannot move up past root")
                        continue
                    curr_level = tree.parent(curr_level.identifier)
                    print(f"Moving up directory to {curr_level.identifier}")
                else:
                    # Set current level in tree
                    curr_level = tree.get_node(cmd[2])
                    print(f"Moving to directory {curr_level.identifier}")
            elif cmd[1] == 'ls':
                # Handle ls command
                print(f"Doing ls")
                continue
        # Add directory if it doesn't exist
        elif cmd[0] == 'dir':
            if not tree.contains(cmd[1]):
                print(f"Adding directory {cmd[1]}")
                tree.create_node(cmd[1], cmd[1], parent=curr_level.identifier, data=FileDescriptor('dir'))
        # Add file if it doesn't exist
        elif cmd[0].isnumeric():
            if not tree.contains(cmd[1]):
                print(f"Adding file {cmd[1]}, size {cmd[0]}")
                tree.create_node(cmd[1], cmd[1], parent=curr_level.identifier, data=FileDescriptor('file',int(cmd[0])))

print()
tree.show(data_property="filetype", idhidden=False)


def get_dir_size(tree, start='/')->int:
    file_size = sum(x.data.get_size() for x in tree.children(start) if x.data.get_type() == 'file')
    dir_size = sum(get_dir_size(tree,x.identifier) for x in tree.children(start) if x.data.get_type() == 'dir')
    return file_size + dir_size

def get_all_sub_dirs(tree, start='/')->list:
    all_sub_dirs = [(start, get_dir_size(tree,start))]
    for x in tree.children(start):
        if x.data.get_type() == 'dir':
            all_sub_dirs.extend(get_all_sub_dirs(tree,x.identifier))
    return all_sub_dirs

below_100k = 0
print(sum([i[1] for i in get_all_sub_dirs(tree) if i[1] <= 100_000 ]))
