def solution(record):
    user_nickname = {}
    events = []
    message = []

    for action in record:
        action = action.split(" ")
        command = action[0]
        id = action[1]

        if command == "Enter" or command == "Change":
            nickname = action[2]
            user_nickname[id] = nickname
        if command == "Enter":
            events.append(id + "님이 들어왔습니다.")
        if command == "Leave":
            events.append(id + "님이 나갔습니다.")

    for event in events:
        event_split = event.split("님")
        id = event_split[0]
        action = event_split[1]
        message.append(user_nickname[id] + "님" + action)

    return message

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
