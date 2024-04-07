import json
import warnings

import pygame_gui

from src.factories import *
from src.game_instance import GameInstance
from src.globals import *
from src.lab import Lab
from src.screen_mode import ScreenMode

warnings.filterwarnings("ignore")


class AppInstance:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(SIZE)
        self.manager = pygame_gui.UIManager(SIZE)
        self.new_game = ScreenMode(self.manager)

        self.players_factory = PlayerFactory()
        self.enemy_factory = EnemyFactory()
        self.yellow_coins_factory = YellowCoinFactory()
        self.green_coins_factory = GreenCoinFactory()
        self.blue_coins_factory = BlueCoinFactory()

        self.time = 1
        self.speed = 0
        self.clock = pygame.time.Clock()

        self.running = True
        self.cur_state = 'start_screen'
        self.music = pygame.mixer.Sound(DATA['music'])

        with open(DATA['levels']) as f:
            self.levels = json.load(f)

        self.map_name = None
        self.position = None
        self.w_position = None
        self.finish_id = None
        self.mode = None
        self.m_position = None
        self.bm_position = None
        self.gm_position = None

    def start(self) -> None:
        self.music.play(0)
        self.new_game.start_screen(self.screen)
        while self.running:
            self.run()
        pygame.quit()

    def rules_print(self) -> None:
        self.new_game.rules(self.screen)
        self.cur_state = 'rules_screen'

    def rules_screen(self, event: pygame.event.Event, time_de: float) -> bool:
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_START_PRESS\
                                          and event.ui_element == self.new_game.buttons[0]:
            self.cur_state = 'start_screen'
            self.new_game.remove_all(self.screen)
            self.new_game.start_screen(self.screen)
            self.manager.update(time_de)
            self.manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(15)
            return True
        return False

    def logo_playing(self, time_de: float) -> None:
        pygame.display.set_caption(LEXICON['name'])
        self.new_game.remove_all(self.screen)
        self.new_game.logo_playing(self.screen)

        self.new_game.choose_level(self.screen, time_de)
        self.cur_state = 'choose_level'
        self.clock.tick(15)
        self.music.stop()

    def start_screen(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.new_game.buttons[1]:
                self.running = False
            elif event.ui_element == self.new_game.buttons[2]:
                self.cur_state = 'rules_print'
            elif event.ui_element == self.new_game.buttons[0]:
                self.cur_state = 'logo_playing'

    def choose_level(self, event: pygame.event.Event, time_de: float) -> None:
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_START_PRESS:
            for i, switch in enumerate(self.new_game.buttons):
                if i == 36:
                    self.running = False
                    break

                if event.ui_element == switch:
                    self.map_name = self.levels[str(i)]['map_name']
                    self.position = tuple(self.levels[str(i)]['player_pos'])
                    self.w_position = tuple(self.levels[str(i)]['enemy_pos'])
                    self.finish_id = tuple(self.levels[str(i)]['finish_pos'])
                    self.mode = int(self.levels[str(i)]['mode'])
                    self.m_position = list(map(tuple, self.levels[str(i)]['yellow_coins_pos']))
                    self.bm_position = list(map(tuple, self.levels[str(i)]['blue_coins_pos']))
                    self.gm_position = list(map(tuple, self.levels[str(i)]['green_coins_pos']))
                    self.cur_state = 'game_process'
                    self.new_game.game_process(self.screen, time_de)
                    break

    def game_end(self, event: pygame.event.Event, time_de: float) -> None:
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_START_PRESS\
                                          and event.ui_element == self.new_game.buttons[0]:
            self.new_game.remove_all(self.screen)
            self.new_game.choose_level(self.screen, time_de)
            self.cur_state = 'choose_level'

    def single_player(self) -> None:
        hero = self.players_factory.create(self.position, DATA['player_1'])
        war = self.enemy_factory.create(self.w_position, DATA['enemy_1'])
        lab = Lab(self.map_name)
        money = []
        for i in self.m_position:
            money.append(self.yellow_coins_factory.create(i))
        for i in self.gm_position:
            money.append(self.green_coins_factory.create(i))
        for i in self.bm_position:
            money.append(self.blue_coins_factory.create(i))

        game = GameInstance(True, lab, hero, war, money)
        hero.update(lab, PLAYER_1_KEYS)
        self.position = hero.get_position()
        self.time += 1

        if 0 < self.speed < 25:
            self.speed += 1
            war.update(lab, self.position, self.time, 10)
        elif -25 < self.speed < 0:
            self.speed += 1
            war.update(lab, self.position, self.time, 5)
        elif self.position in self.m_position:
            self.speed = 0
            war.update(lab, self.position, self.time)
            self.m_position.remove(self.position)
        elif self.position in self.gm_position:
            self.speed = -24
            war.update(lab, self.position, self.time)
            self.gm_position.remove(self.position)
        elif self.position in self.bm_position:
            self.speed = 1
            war.update(lab, self.position, self.time)
            self.bm_position.remove(self.position)
        else:
            self.speed = 0
            war.update(lab, self.position, self.time)

        self.w_position = war.get_position()
        game.render(self.screen)

        if self.position == self.finish_id and self.m_position == []:
            self.music = pygame.mixer.Sound(DATA['victory_music'])
            self.music.play(0)

            font = pygame.font.Font(None, 50)
            text = font.render(LEXICON['victory_text'], 1, (201, 0, 190))
            text_x = 810 // 2 - text.get_width() // 2
            text_y = 880 // 2 - text.get_height() // 2
            self.new_game.blit_header(self.screen, LEXICON['victory_text'], 50, (text_x, text_y))
            self.cur_state = 'game_end'

        if self.position == self.w_position:
            self.music = pygame.mixer.Sound(DATA['defeat_music'])
            self.music.play(0)

            font = pygame.font.Font(None, 50)
            text = font.render(LEXICON['defeat_text'], 1, (201, 0, 190))
            text_x = 810 // 2 - text.get_width() // 2
            text_y = (880 // 2 - text.get_height() // 2)
            self.new_game.blit_header(self.screen, LEXICON['defeat_text'], 50, (text_x, text_y))
            self.cur_state = 'game_end'

    def multi_player(self) -> None:
        hero = self.players_factory.create(self.position, DATA['player_1'])
        hero_2 = self.players_factory.create(self.w_position, DATA['player_2'])
        lab = Lab(self.map_name)
        game_2 = GameInstance(False, lab, hero, hero_2, [])
        hero.update(lab, PLAYER_1_KEYS)
        self.position = hero.get_position()
        hero_2.update(lab, PLAYER_2_KEYS)
        self.time += 1
        self.w_position = hero_2.get_position()
        game_2.render(self.screen)

        if self.position == self.finish_id:
            if self.finish_id == self.w_position:
                self.music = pygame.mixer.Sound(DATA['victory_music'])
                self.music.play(0)

                font = pygame.font.Font(None, 50)
                text = font.render(LEXICON['draw_text'], 1, (201, 0, 190))
                text_x = 810 // 2 - text.get_width() // 2
                text_y = 880 // 2 - text.get_height() // 2
                self.new_game.blit_header(self.screen, LEXICON['draw_text'], 50, (text_x, text_y))

            else:
                self.music = pygame.mixer.Sound(DATA['victory_music'])
                self.music.play(0)

                font = pygame.font.Font(None, 50)
                text = font.render(LEXICON['1_victory_text'], 1, (201, 0, 190))
                text_x = 810 // 2 - text.get_width() // 2
                text_y = 880 // 2 - text.get_height() // 2
                self.new_game.blit_header(self.screen, LEXICON['1_victory_text'], 50, (text_x, text_y))

            self.cur_state = 'game_end'

        elif self.finish_id == self.w_position:
            self.music = pygame.mixer.Sound(DATA['victory_music'])
            self.music.play(0)

            font = pygame.font.Font(None, 50)
            text = font.render(LEXICON['2_victory_text'], 1, (201, 0, 190))
            text_x = 810 // 2 - text.get_width() // 2
            text_y = 880 // 2 - text.get_height() // 2
            self.new_game.blit_header(self.screen, LEXICON['2_victory_text'], 50, (text_x, text_y))
            self.cur_state = 'game_end'

    def run(self) -> None:
        time_de = self.clock.tick(60) / 1000.0
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                break

            if self.cur_state == 'rules_print':
                self.rules_print()

            if self.cur_state == 'rules_screen':
                if self.rules_screen(event, time_de):
                    continue

            if self.cur_state == 'logo_playing':
                self.logo_playing(time_de)
                continue

            if self.cur_state == 'start_screen':
                self.start_screen(event)

            if self.cur_state == 'choose_level':
                self.choose_level(event, time_de)

            if self.cur_state in ['game_process', 'game_end']:
                self.game_end(event, time_de)

            self.manager.process_events(event)

        if self.cur_state == 'game_process':
            if self.mode != 1:
                self.single_player()
            else:
                self.multi_player()

        self.manager.update(time_de)
        self.manager.draw_ui(self.screen)
        pygame.display.update()
        self.clock.tick(15)


if __name__ == '__main__':
    app = AppInstance()
    app.start()
