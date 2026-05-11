```python
import random  
import pygame  
  
TRAP_COUNT = 3  # 陷阱数量  
GRID_COUNT = 8  # 迷宫大小 (N x N)SCREEN_WINDOW = 1000  
CELL_SIZE = (SCREEN_WINDOW - 100) // GRID_COUNT  
MAZE_SIZE = CELL_SIZE * GRID_COUNT  
OFFSET_Y = 60  # 顶部文字区域高度  
  
# 颜色定义  
COLOR_BG = (245, 245, 245)  
COLOR_TEXT = (44, 62, 80)  
COLOR_LINE = (189, 195, 199)  
COLOR_AGENT = (52, 152, 219)  # 蓝色  
COLOR_GOAL = (46, 204, 113)  # 绿色  
COLOR_TRAP = (231, 76, 60)  # 红色  
  
  
## 初始化游戏界面  
class MazeGUI:  
    def __init__(self, traps, goal):  
        pygame.init()  
        self.screen = pygame.display.set_mode((MAZE_SIZE, MAZE_SIZE + OFFSET_Y))  
        pygame.display.set_caption("秘境寻宝")  
        self.font = pygame.font.SysFont("SimHei", 20)  
        self.clock = pygame.time.Clock()  
        self.traps = traps  
        self.goal = goal  
  
    def draw(self, position, episode, step):  
        self.screen.fill(COLOR_BG)  
  
        # 1. 状态信息  
        info = self.font.render(f"episode: {episode + 1} | step: {step} | trap: {len(self.traps)}", True, COLOR_TEXT)  
        self.screen.blit(info, (10, 15))  
  
        # 2. 网格和元素  
        for r in range(GRID_COUNT):  
            for c in range(GRID_COUNT):  
                rect = (c * CELL_SIZE, r * CELL_SIZE + OFFSET_Y, CELL_SIZE, CELL_SIZE)  
                pygame.draw.rect(self.screen, COLOR_LINE, rect, 1)  # 画边框  
  
                # 画陷阱  
                if (r, c) in self.traps:  
                    pygame.draw.rect(self.screen, COLOR_TRAP, (rect[0] + 4, rect[1] + 4, CELL_SIZE - 8, CELL_SIZE - 8))  
                # 画终点  
                elif (r, c) == self.goal:  
                    pygame.draw.rect(self.screen, COLOR_GOAL, (rect[0] + 4, rect[1] + 4, CELL_SIZE - 8, CELL_SIZE - 8))  
  
        # 3. 画探险家  
        if position != 'terminal':  
            r, c = eval(position)  
            center = (c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + OFFSET_Y + CELL_SIZE // 2)  
            pygame.draw.circle(self.screen, COLOR_AGENT, center, CELL_SIZE // 3)  
  
        pygame.display.flip()  
  
def init_environment():  
    """初始化陷阱和终点坐标"""  
    all_positions = [(r, c) for r in range(GRID_COUNT) for c in range(GRID_COUNT)]  
    all_positions.remove((0, 0))  # 起点不能是陷阱  
    goal = (GRID_COUNT - 1, GRID_COUNT - 1)  
    all_positions.remove(goal)  # 终点不能是陷阱  
  
    # 随机选出陷阱  
    traps = random.sample(all_positions, min(TRAP_COUNT, len(all_positions)))  
    # traps = [(2, 1), (3,4), (1,6)]  
    return traps, goal  
  
# 与环境交互，获取下一个状态和奖励  
def get_env_feedback(current_state, action, goal, traps):  
    # current_state是字符串"(0, 0)"，用eval函数解析，r_idx表示当前状态的行索引，c_idx表示当前状态的列索引  
    r_idx, c_idx = eval(current_state)  
  
    # 根据动作决定下一个位置的坐标  
    if action == 'up':  
        r_idx = max(0, r_idx - 1)  
    elif action == 'down':  
        r_idx = min(GRID_COUNT - 1, r_idx + 1)  
    elif action == 'left':  
        c_idx = max(0, c_idx - 1)  
    elif action == 'right':  
        c_idx = min(GRID_COUNT - 1, c_idx + 1)  
  
    next_state = (r_idx, c_idx)  
  
    is_terminated = False  
    if next_state == goal:  
        # 得到宝藏  
        reward = 1  
        is_terminated = True  
    elif next_state in traps:  
        # 遇到陷阱  
        reward = -1  
        is_terminated = True  
    else:  
        # 普通步骤  
        # reward = 0  
        # reward = -0.01  # 扣太少，可能导致原地踏步  
        reward = -0.1  
  
    return str(next_state), reward, is_terminated
    
```