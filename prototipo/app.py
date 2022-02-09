from turtle import st
import pygame
from system import System
commands = {'up': False, 'down': False, 'right': False, 'left': False}
system = System(600, 'teste', 60)
system.initialize()