def law_parse(instruction):
    instruction = instruction[len("Law Description: "):instruction.find("\n")]
    # print(instruction)
    return instruction
