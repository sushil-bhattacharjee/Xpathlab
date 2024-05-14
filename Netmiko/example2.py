def name_printer(name):
    print(f"hello {name}")

my_friends = ["Suman", "Sayef", "Dipendra", "Baby", "Sourja"]

for friend in my_friends:
    name_printer(friend)


def cmd_printer(cmd):
    print(f"enable\n {cmd}")

my_commands = ["show version", "show run", "sh run | s router ospf"]

for command in my_commands:
    cmd_printer(command)