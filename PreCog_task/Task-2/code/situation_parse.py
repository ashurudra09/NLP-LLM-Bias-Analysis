def situation_parse(instruction):
    instruction = instruction[instruction.find('Situation: ') + len('Situation: '):]
    items = instruction.split(',')
    name = items[0]
    identity = items[1]
    gender = identity.split(" ")[-1]
    identity = identity[1:len(identity) - len(gender) - 1]
    action = items[2]
    return name, identity, gender, action
