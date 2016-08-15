#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *


MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.onGround = False

        self.right = False
        self.left = False
        self.up = False

    def update(self, platforms):
        if self.left:
            self.xvel = -MOVE_SPEED
        if self.right:
            self.xvel = MOVE_SPEED

        if not (self.left or self.right):
            self.xvel = 0

        if self.up:
            if self.onGround:
                self.yvel = -JUMP_POWER

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.yvel = 0
                    self.onGround = True
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
