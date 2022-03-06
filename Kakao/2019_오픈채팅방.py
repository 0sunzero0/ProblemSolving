def solution(record):
    result = []
    user_nickname = {}

    for action in record:
        if action[0] == "E" or action[0] == "C":
            command, id, nickname = action.split(" ")
            user_nickname[id] = nickname

    for action in record:
        element = action.split(" ")
        command, id = element[0], element[1]
        if command == "Enter":
            result.append(user_nickname.get(id) + "님이 들어왔습니다.")
        elif command == "Leave":
            result.append(user_nickname.get(id) + "님이 나갔습니다.")

    return result
