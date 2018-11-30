import game_framework
import pico2d

import start_state
import title_state
import end_state_lose
import end_state_win

import main_state


pico2d.open_canvas(600, 1000, True, False)
#game_framework.run(start_state)
#game_framework.run(title_state)
#game_framework.run(main_state)
game_framework.run(end_state_win)
game_framework.run(end_state_lose)
pico2d.close_canvas()