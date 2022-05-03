
import logging
import traceback
import pygame
from controll import controller
from controll import settings
from particle import particles


def main():
    pygame.init()
    controller.white_canvas(settings.screen)
    clock = pygame.time.Clock()
    # Main Loop
    while settings.play_game:
        try:
            clock.tick(40)
            controller.mous_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.play_game = False
                    pygame.quit()
                elif event.type == pygame.MOUSEMOTION:
                    if settings.allow_drawing:
                        if settings.last_pos is not None:
                            pygame.draw.line(settings.screen, settings.set_color, settings.last_pos,
                                             controller.mous_pos, settings.line_size)
                        settings.last_pos = controller.mous_pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    settings.last_pos = None
                    settings.allow_drawing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if controller.mous_pos[0] <= 50 and controller.mous_pos[1] > 50:
                        pick_color = pygame.Surface.get_at(
                            settings.screen, controller.mous_pos)
                        settings.set_color = pick_color
                        pygame.mouse.get_pressed()
                    if settings.draw_line:
                        settings.allow_drawing = True
                    else:
                        pygame.draw.circle(
                            settings.screen, settings.set_color, controller.mous_pos, 20)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings.play_game = False
                        pygame.quit()
                        break
                    else:
                        controller.keybboard(event.key)

            if len(particles.particles) > 0:
                controller.white_canvas(settings.screen)
                for p in particles.particles:
                    p.draw()

            controller.drawColorPicker(
                settings.screen, settings.set_color, settings.line_size)
            controller.drawCurrentColor(settings.screen, settings.set_color)
            pygame.display.flip()
        except Exception as e:
            logging.error(traceback.format_exc())
    pygame.quit()


if __name__ == "__main__":
    main()
p
