import pygame

TILE_SIZE: int = 40
COLOR: tuple[int, int, int] = (174, 96, 170)
WAR_EVENT_TYPE: int = 30

SIZE: tuple[int, int] = 850, 900
WIDTH: int = 850
HEIGHT: int = 900

HEADER_TEXT_SIZE: int = 40
TEXT_SIZE: int = 25
ALIGNMENT: int = 50

PLAYER_1_KEYS: dict[str, int] = {'UP': pygame.K_UP, 'DOWN': pygame.K_DOWN, 'LEFT': pygame.K_LEFT,
                                 'RIGHT': pygame.K_RIGHT}
PLAYER_2_KEYS: dict[str, int] = {'UP': pygame.K_w, 'DOWN': pygame.K_s, 'LEFT': pygame.K_a, 'RIGHT': pygame.K_d}

DATA: dict[str, str] = {
    'start_bg': "assets/images/fon5.jpg",
    'choose_bg': "assets/images/fon6.jpg",
    'player_1': "assets/images/hero4.png",
    'player_2': 'assets/images/hero.png',
    'logo_player': "assets/images/hero3.png",
    'enemy': "assets/images/war.png",
    'enemy_1': "assets/images/war1.png",
    'enemy_2': "assets/images/war2.png",
    'levels': "assets/levels.json",
    'music': "assets/audio/background.wav",
    'victory_music': "assets/audio/victory.wav",
    'defeat_music': "assets/audio/defeat.wav",
    'maps_dir': 'assets/maps'
}

LEXICON: dict[str, str] = {
    'rules': 'Правила:',
    'single_game': 'Одиночная игра:',
    'single_rules': 'Вы играете за Героя. В каждом уровне вам нужно от изначального положения добраться до серой клетки так, чтобы враг не успел вас убить и вы успели собрать все желтые монеты. Герой может ходить только по светло-розовым клеткам. Также в этой игре есть синие и зеленые монеты, влияющие на скорость ходьбы врага. Если вы собрали зеленую монету, то он ускорится, а если синюю, то замедлится.',
    'multi_rules': 'Вы играете за двух Героев: светлого и темного. В каждом уровне вам нужно быстрее соперника от изначального положения добраться до серой клетки. Герои могут ходить только по светло-розовым клеткам.',
    'multi_game': 'Игра на двоих:',
    'control': 'Управление:',
    'control_hero_1': 'Управление Герой 1(светлый) – стрелочки.',
    'control_hero_2': 'Управление Герой 2(тёмный): W - вверх, A - влево, S - вниз, D - вправо.',
    'hero_1': 'Герой(Герой 1)',
    'hero_2': 'Герой 2',
    'enemy': 'Враг',
    'coins': 'Монеты',
    '1_player': '1 PLAYER',
    '2_players': '2 PLAYERS',
    'name': 'Quarterback',
    'victory_text': "WON! :)",
    'defeat_text': 'LOST! :( TRY AGAIN',
    'draw_text': "BOTH WON! :)",
    '1_victory_text': '1 WON! :)',
    '2_victory_text': '2 WON! :)'
}
