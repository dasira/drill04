from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0
dir = 1

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


while True and running:
    clear_canvas()
    grass.draw(400, 30)
    
    if dir == 1:
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    elif dir == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if x == 800:
        dir = -1
    elif x < 0:
        dir = 1
    x += dir * 5
    delay(0.05)

close_canvas()

