def initial_window():
    window.fill(color.black)
    left_paddle.draw(window)
    right_paddle.draw(window)
    ball.draw(window)
    fieldlines.draw_h_line(window, height)
    points_left = font.render(f"{p_left}", 1, color.blue)
    points_right = font.render(f"{p_right}", 1, color.red)
    window.blit(points_left, (width/2-points_left.get_width()*3, 10))
    window.blit(points_right, (width/2+points_right.get_width()*2, 10))


if __name__=="__main__":
    import pygame
    import sys
    import random
    import math
    from objects import *
    from colors import *

    pygame.init()

    fps = 60
    screen = pygame.display.Info()
    size = width, height = screen.current_w, screen.current_h
    paddle = paddle_width, paddle_height = 10, int(0.15*height)
    vel_paddle = 0.003*width
    vel_ball = 0.008*width

    p_left = p_right = 0
    win_score = 5
    won = False

    fpsclock = pygame.time.Clock()
    window = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption("PY PONG")

    font = pygame.font.SysFont("Arial", 50)

    color = Colors()
    fieldlines = FieldLines(color.white, width/2, 6)

    left_paddle = Paddle(size, color.blue, 10, height/2-paddle_height/2, paddle_width, paddle_height, vel_paddle, pygame.K_w, pygame.K_s)
    right_paddle = Paddle(size, color.red, width-10-paddle_width, height/2-paddle_height/2, paddle_width, paddle_height, vel_paddle, pygame.K_UP, pygame.K_DOWN)

    ball = Ball(color.white, 10, width/2, height/2, vel_ball, 0)

    while True:
        initial_window()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        if ball.vel_x < 0:
            if ball.x+ball.size/2 <= left_paddle.x+left_paddle.width and\
               ball.y+ball.size/2 >= left_paddle.y and\
               ball.y+ball.size/2 <= left_paddle.y+left_paddle.height:
                phi = ((ball.y-left_paddle.y)/(left_paddle.height)*0.6+0.2)*math.pi
                ball.vel_y = vel_ball * -math.cos(phi)
                ball.vel_x = vel_ball * math.sin(phi)
        if ball.vel_x > 0:
            if ball.x+ball.size/2 >= right_paddle.x and\
               ball.y+ball.size/2 >= right_paddle.y and\
               ball.y-ball.size/2 <= right_paddle.y+right_paddle.height:
                phi = ((ball.y-right_paddle.y)/(right_paddle.height)*0.6+0.2)*math.pi
                ball.vel_y = vel_ball * -math.cos(phi)
                ball.vel_x = -vel_ball * math.sin(phi)

        if ball.y <= 0 or ball.y+ball.size >= height:
            ball.vel_y *= -1

        if ball.x <= 0 or ball.x+ball.size >= width:
            if ball.vel_x < 0:
                p_right += 1
                if p_right >= win_score:
                    won = True
                    won_text= "Right player won, congratulations!"
            if ball.vel_x > 0:
                p_left +=1
                if p_left >= win_score:
                    won = True
                    won_text= "Left player won, congratulations!"
            ball.reset(ball.vel_x, vel_ball)
            left_paddle.reset()
            right_paddle.reset()
            initial_window()
            pygame.display.update()
            if not won:
                pygame.time.delay(3000)

        if won:
            initial_window()
            winner = font.render(won_text, 1, color.yellow)
            window.blit(winner, (width/2-winner.get_width()/2, height/4))
            pygame.display.update()
            pygame.time.delay(10000)
            sys.exit()


        ball.move()
        left_paddle.move()
        right_paddle.move()

        pygame.display.update()
        fpsclock.tick(fps)