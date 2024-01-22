import pygame
import sys

from settings import Settings

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建环境资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """游戏主循环"""
        while True:
            #侦听键盘及鼠标的行为
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #每次更新屏幕前先绘制背景颜色,否则默认黑色
            self.screen.fill(self.settings.bg_color)

            # 更新屏幕
            pygame.display.flip()

            #维持预定的帧率稳定
            self.clock.tick(60)

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

