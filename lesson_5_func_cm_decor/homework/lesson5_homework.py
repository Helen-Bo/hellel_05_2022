LOGGING = True

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def repr_players(players: list[dict], player_sorter: bool, key=lambda x: x["number"]) -> None:
    print("Team:")
    if player_sorter is True:
        for player in sorted(players, key=key):
            print(f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}")
    else:
        for player in players:
            print(f"\t{player['number']} Name: {player['name']}, Age: {player['age']}")
        print("\n")


def log(message: str) -> None:
    print(f"-> -> -> {message} <- <- <- ")


def add_player(num: int, name: str, age: int) -> None:
    player = {"name": name, "number": num, "age": age}
    if num in {player["number"] for player in team}:
        log(message="Player with this number already exist")
    else:
        team.append(player)
        log(message=f"Adding {player['name']}")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting  {player_name}")
            return


def update_player(players: list[dict], num: int, name: str, age: int) -> None:
    player = {"name": name, "number": num, "age": age}

    if num not in {player["number"] for player in team}:
        log(message="Player with this number does not exist")

    elif num in {player["number"] for player in team}:
        if player["number"] == num:
            player.update()
            player = {
                "name": player["name"],
                "age": player["age"],
                "number": player["number"],
            }
        team.append(player)
        log(message=f"Update player with #{num}")


def main():
    repr_players(team, False)

    add_player(num=17, name="Cris", age=31)
    add_player(num=2, name="Bob", age=39)
    add_player(num=21, name="Tom", age=32)
    add_player(num=22, name="Matthew", age=33)

    # repr_players(team, False)
    remove_player(players=team, num=17)
    # repr_players(team, True)

    update_player(team, num=10, name="Sofi", age=18)
    repr_players(team, True)

    update_player(team, num=1, name="Sofi", age=18)
    repr_players(team, True)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
