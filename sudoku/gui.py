from validate import Solve
import validate
from populateSudoku import getSudoku
from codecs import backslashreplace_errors
from turtle import bgcolor
from colorama import Back
import pygame
pygame.init()


Width = 512
Height = 512
w = Width/9

grid = getSudoku()
originalGrid = [[grid[i][j]
                 for j in range(len(grid[0]))] for i in range(len(grid[0]))]
solvedGrid = [[grid[i][j]
               for j in range(len(grid[0]))] for i in range(len(grid[0]))]

Solve(solvedGrid)
print(solvedGrid)


original_element_color = (52, 52, 52)
correct_element_color = (0, 255, 52)
wrong_element_color = (255, 0, 0)
numberFont = pygame.font.SysFont(None, 50)


bg = pygame.image.load('Sudoku.png')
print(bg)
bg = pygame.transform.scale(bg, (Width, Height))


# class Background(pygame.sprite.Sprite):
#     def __init__(self, image):
#         pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
#         self.image = image  # setting the image
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = (0, 0)


def insertNum(win, position):
    i, j = int(position[1])-1, int(position[0])-1
    i = int(i//w)
    j = int(j//w)
    print(i, j)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:  # pressing a key
                if(originalGrid[i][j] != 0):  # if unmodifable number
                    return
                if(event.key == 48):  # if 0, clear
                    grid[i][j] = event.key - 48
                    # pygame.draw.rect(win, (255, 0, 0),
                    #                  (j*w + 5, i*w + 5, 50-5, 50-5))  # 5 is the buffer
                    # pygame.display.update()
                    reDraw(win, grid)

                    return
                if(0+48 < event.key < 10+48):
                    # pygame.draw.rect(win, (0, 0, 255),
                    #                  (j*w + 5, i*w + 5, 50-5, 50-5))  # 5 is the buffer
                    # value = numberFont.render(
                    #     str(event.key-48), True, correct_element_color)
                    # win.blit(value, ((j)*w+20, (i)*w+20))
                    grid[i][j] = (event.key-48)

                    reDraw(win, grid)
                    return


def reDraw(win, grid):
    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    w = Width/9
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10):

                color = ""
                if(grid[i][j] == originalGrid[i][j]):
                    color = original_element_color
                elif (grid[i][j] == solvedGrid[i][j]):
                    color = correct_element_color
                else:
                    color = wrong_element_color

                value = numberFont.render(
                    str(grid[i][j]), True, color)

                win.blit(value, ((j)*w+20, (i)*w+20))

    pygame.display.update()


def main():

    win = pygame.display.set_mode((Width, Height))

    pygame.display.set_caption("Sudoku")

    reDraw(win, grid)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left click on mouse
                pos = pygame.mouse.get_pos()
                insertNum(win, (pos[0], pos[1]))


main()
