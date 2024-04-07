import pygame_gui

from src.entities.coin import YellowCoin, GreenCoin, BlueCoin
from src.globals import *


class ScreenMode:
    def __init__(self, manager: pygame_gui.UIManager) -> None:
        self.buttons = []
        self.manager = manager

    def start_screen(self, screen: pygame.Surface) -> None:
        background = pygame.Surface(screen.get_size())
        background.fill(pygame.Color(COLOR))
        screen.blit(background, (0, 0))

        my_image = pygame.image.load(DATA['start_bg']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, screen.get_size())
        screen.blit(scaled_image, (0, 0))

        my_image = pygame.image.load(DATA['player_1']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (300, 270))
        screen.blit(scaled_image, (50, 50))

        my_image = pygame.image.load(DATA['enemy']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (280, 300))
        screen.blit(scaled_image, (540, 20))

        my_image = pygame.image.load(DATA['enemy_1']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (300, 310))
        screen.blit(scaled_image, (520, 580))

        my_image = pygame.image.load(DATA['enemy_2']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (280, 300))
        screen.blit(scaled_image, (30, 570))

        self.buttons = [pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect((335, 310), (180, 130)),
                            text='START',
                            manager=self.manager),
                        pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect((375, 540), (100, 60)),
                            text='EXIT',
                            manager=self.manager),
                        pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect((355, 455), (140, 70)),
                            text='RULE',
                            manager=self.manager)]

    @staticmethod
    def blit_header(screen: pygame.Surface, text: str, size: int, coords: tuple) -> None:
        font = pygame.font.Font(None, size)
        text = font.render(text, True, (255, 255, 255))
        pygame.draw.rect(screen, (153, 153, 153), (*coords, text.get_width(), text.get_height()))
        screen.blit(text, coords)

    @staticmethod
    def blit_text(surface: pygame.Surface, text: str, pos: tuple[int, int],
                  text_size: int = TEXT_SIZE, text_color: pygame.Color = pygame.Color('white')) -> None:
        font = pygame.font.Font(None, text_size)
        words = [word.split() for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        max_width -= 50
        x, y = pos
        for line in words:
            word_height = 0
            for word in line:
                word_surface = font.render(word, True, text_color)
                word_width, word_height = word_surface.get_size()
                word_height += 5
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    def rules(self, screen: pygame.Surface) -> None:
        for i in self.buttons:
            i.hide()

        ret = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300 + 100, 860), (70, 20)),
            text='return',
            manager=self.manager)
        self.buttons = [ret]

        background = pygame.Surface(screen.get_size())
        background.fill(pygame.Color(COLOR))
        screen.blit(background, (0, 0))

        self.blit_header(screen, LEXICON['rules'], HEADER_TEXT_SIZE, (350, 20))
        self.blit_header(screen, LEXICON['single_game'], TEXT_SIZE, (50, 45))
        self.blit_text(screen, LEXICON['single_rules'], (20, 70))

        self.blit_header(screen, LEXICON['multi_game'], TEXT_SIZE, (50, 245))
        self.blit_text(screen, LEXICON['multi_rules'], (20, 270))

        self.blit_header(screen, LEXICON['control'], TEXT_SIZE, (50, 430))
        self.blit_text(screen, LEXICON['control_hero_1'], (20, 460))
        self.blit_text(screen, LEXICON['control_hero_2'], (20, 490))

        my_image = pygame.image.load(DATA['player_1']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (130, 150))
        screen.blit(scaled_image, (50, 600))
        self.blit_text(screen, LEXICON['hero_1'], (50, 770))

        my_image = pygame.image.load(DATA['player_2']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (145, 150))
        screen.blit(scaled_image, (250, 600))
        self.blit_text(screen, LEXICON['hero_2'], (300, 770))

        my_image = pygame.image.load(DATA['enemy_1']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, (145, 150))
        screen.blit(scaled_image, (450, 600))
        self.blit_text(screen, LEXICON['enemy'], (525, 770))

        YellowCoin((17.8, 15.5)).render(screen)
        GreenCoin((17.8, 16.5)).render(screen)
        BlueCoin((17.8, 17.5)).render(screen)
        self.blit_text(screen, LEXICON['coins'], (700, 770))
        pygame.display.update()

    def remove_all(self, screen: pygame.Surface) -> None:
        for i in self.buttons:
            i.hide()
        self.buttons = []

        background = pygame.Surface((850, 900))
        background.fill(pygame.Color(COLOR))
        screen.blit(background, (0, 0))
        pygame.display.update()

    def get_second_switchers(self) -> list[pygame_gui.elements.UIButton]:
        return [
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 10), (100, 50)),
                text='1',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 10), (100, 50)),
                text='2',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 10), (100, 50)),
                text='3',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((310 + 200, 10), (100, 50)),
                text='4',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((410 + 200, 10), (100, 50)),
                text='5',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 100), (100, 50)),
                text='6',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 100), (100, 50)),
                text='7',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 100), (100, 50)),
                text='8',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((310 + 200, 100), (100, 50)),
                text='9',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((410 + 200, 100), (100, 50)),
                text='10',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 200), (100, 50)),
                text='11',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 200), (100, 50)),
                text='12',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 200), (100, 50)),
                text='13',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((310 + 200, 200), (100, 50)),
                text='14',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((410 + 200, 200), (100, 50)),
                text='15',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 300), (100, 50)),
                text='16',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 300), (100, 50)),
                text='17',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 300), (100, 50)),
                text='18',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 400), (100, 50)),
                text='1',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 400), (100, 50)),
                text='2',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 400), (100, 50)),
                text='3',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((310 + 200, 400), (100, 50)),
                text='4',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((410 + 200, 400), (100, 50)),
                text='5',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 500), (100, 50)),
                text='6',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 500), (100, 50)),
                text='7',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 500), (100, 50)),
                text='8',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((310 + 200, 500), (100, 50)),
                text='9',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((410 + 200, 500), (100, 50)),
                text='10',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 600), (100, 50)),
                text='11',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 600), (100, 50)),
                text='12',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 600), (100, 50)),
                text='13',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((310 + 200, 600), (100, 50)),
                text='14',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((410 + 200, 600), (100, 50)),
                text='15',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((10 + 200, 700), (100, 50)),
                text='16',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((110 + 200, 700), (100, 50)),
                text='17',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((210 + 200, 700), (100, 50)),
                text='18',
                manager=self.manager),
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((300 + 100, 760), (70, 20)),
                text='EXIT',
                manager=self.manager)
        ]

    def choose_level(self, screen: pygame.Surface, time_de: float) -> None:
        for i in self.buttons:
            i.hide()
        self.buttons = []

        background = pygame.Surface((650 + 200, 900))
        background.fill(pygame.Color(COLOR))
        pygame.display.update()
        self.manager.update(time_de)
        self.buttons = self.get_second_switchers()

        my_image = pygame.image.load(DATA['choose_bg']).convert_alpha()
        scaled_image = pygame.transform.scale(my_image, screen.get_size())
        screen.blit(scaled_image, (0, 0))

        self.blit_text(screen, LEXICON['1_player'], (15, 100), 50)
        self.blit_text(screen, LEXICON['2_players'], (15, 500), 50)
        pygame.draw.line(screen, (58, 0, 211), (0, 380), (1000, 380), 4)
        self.manager.draw_ui(screen)
        pygame.display.update()

    @staticmethod
    def logo_playing(screen: pygame.Surface) -> None:
        run = True
        x_pos = 0
        pixels_per_second = 20
        clock = pygame.time.Clock()
        my_image = pygame.image.load(DATA['player_1']).convert_alpha()
        go_without_actors = False
        first_coord = 10
        second_coord = 0
        actors_appears = False
        go_with_actors = False

        while run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

            screen.fill((82, 0, 135))
            if int(x_pos) <= 380:
                screen.blit(my_image, (int(x_pos), 100))
                x_pos += pixels_per_second * clock.tick() / 50
            else:
                screen.blit(my_image, (380, 300))
                go_without_actors = True

            if go_without_actors:
                pygame.draw.rect(screen, (82, 0, 135), (0, 0, 810, 880))
                if 380 - first_coord > 150:
                    scaled_image = pygame.transform.scale(my_image, (380 - first_coord, 400 - first_coord))
                    first_coord += 10
                    screen.blit(scaled_image, (380, 100 - second_coord))
                    second_coord -= 10
                else:
                    screen.blit(scaled_image, (380, 100 - second_coord))
                    actors_appears = True

            if actors_appears:
                war_image = pygame.image.load(DATA['enemy']).convert_alpha()
                war_image = pygame.transform.scale(war_image, (220 - 70, 310 - 70))
                war1_image = pygame.image.load(DATA['enemy_1']).convert_alpha()
                war1_image = pygame.transform.scale(war1_image, (262 - 70, 310 - 70))
                war2_image = pygame.image.load(DATA['enemy_2']).convert_alpha()
                war2_image = pygame.transform.scale(war2_image, (232 - 70, 330 - 70))
                war3_image = pygame.image.load(DATA['logo_player']).convert_alpha()
                war3_image = pygame.transform.scale(war3_image, (262 - 70, 320 - 70))
                screen.blit(war_image, (90, 50))
                screen.blit(war1_image, (480, 60))
                screen.blit(war2_image, (110, 510))
                screen.blit(war3_image, (550, 500))
                go_with_actors = True

            if go_with_actors:
                pygame.draw.rect(screen, (82, 0, 135), (0, 0, 1910, 1070))
                war_image = pygame.image.load(DATA['enemy']).convert_alpha()
                war_image = pygame.transform.scale(war_image, (220 - 70, 310 - 70))
                war1_image = pygame.image.load(DATA['enemy_1']).convert_alpha()
                war1_image = pygame.transform.scale(war1_image, (262 - 70, 310 - 70))
                war2_image = pygame.image.load(DATA['enemy_2']).convert_alpha()
                war2_image = pygame.transform.scale(war2_image, (232 - 70, 330 - 70))
                war3_image = pygame.image.load(DATA['logo_player']).convert_alpha()
                war3_image = pygame.transform.scale(war3_image, (262 - 70, 320 - 70))
                screen.blit(war_image, (90, 50))
                screen.blit(war1_image, (480, 60))
                screen.blit(war2_image, (110, 510))
                screen.blit(war3_image, (550, 500))
                screen.blit(scaled_image, (int(x_pos), 100 - second_coord))
                x_pos += pixels_per_second * clock.tick() / 50

            pygame.display.flip()

    def game_process(self, screen: pygame.Surface, time_de: float) -> None:
        for i in self.buttons:
            i.hide()
        self.buttons = [pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300 + 100, 860), (70, 20)),
            text='return',
            manager=self.manager)]

        self.manager.update(time_de)
        self.manager.draw_ui(screen)
        pygame.display.update()
