import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60

STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)


def clamp_rect(rect: pygame.Rect, width_limit: int, height_limit: int) -> None:
    """Keeps rect fully inside a 0..width_limit x 0..height_limit area."""
    bounds = pygame.Rect(0, 0, width_limit, height_limit)
    rect.clamp_ip(bounds)


def handle_input(rect: pygame.Rect) -> None:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect.x -= STEP
    if keys[pygame.K_RIGHT]:
        rect.x += STEP
    if keys[pygame.K_UP]:
        rect.y -= STEP
    if keys[pygame.K_DOWN]:
        rect.y += STEP


def main():
    pygame.init()

    display = pygame.display.set_mode(
        (WIDTH_DISPLAY, HEIGHT_DISPLAY),
        pygame.RESIZABLE,
    )
    pygame.display.set_caption("My first game")

    clock = pygame.time.Clock()
    rectangle = pygame.Rect(50, 50, WIDTH_RECTANGLE, HEIGHT_RECTANGLE)

    window_width, window_height = WIDTH_DISPLAY, HEIGHT_DISPLAY

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                window_width, window_height = event.w, event.h
                display = pygame.display.set_mode(
                    (window_width, window_height),
                    pygame.RESIZABLE,
                )

        handle_input(rectangle)
        clamp_rect(rectangle, window_width, window_height)

        display.fill(BLACK_COLOR)
        pygame.draw.rect(display, RED_COLOR, rectangle)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
