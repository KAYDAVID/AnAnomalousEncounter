import world
from player import Player


def play():
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            avaliable_actions = room.avaliable_actions()
            for action in avaliable_actions:
                print(action)
            action_input = input('Action: ')
            for action in avaliable_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
