#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config
import d2game
import d2gui

def main():
    config.RES_DIR = "{}/../res".format(os.path.dirname(os.path.abspath(__file__)))

    gui = d2gui.GUI()
    g = d2game.Game()

    gui.set_game(g)
    g.run(gui.entities)

    while g.is_running():
        gui.process_events()
        g.turn()
        gui.draw()
    g.quit()

if __name__ == "__main__":
    main()
