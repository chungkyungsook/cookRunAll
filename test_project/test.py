import sys
import pygame

#게임 화면 크기
WINDOW_WIDTH   = 1200
WINDOW_HEIGHT  = 870

#색상
WHITE  = (255,255,255)

#속도와 질량 기본 값
VELOCITY = 7    #속도
MASS     = 2    #질량

class Characters:

    def __init__(self):
        self.image  = ""
        self.dx     = 0
        self.dy     = 0
        self.rect   = ""    #이미지 사각형 이미지 크기와 같은 사각형 객체 만들기
        self.isJump = 0
        self.twoJumpNo = 0  # 뛰다_바꾸다
        self.v      = VELOCITY # 속도
        self.m      = MASS     # 질량

    def load_image(self,image):
        #플레이어 캐릭터
        self.image        = pygame.image.load(image)
        #크기 지정
        self.image        = pygame.transform.scale(self.image,(230,230))
        self.rect         = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH/5  #800/2
        self.rect.bottom  = WINDOW_HEIGHT   #500

    # 그림 바꿔주기 함수
    def chan_image(self,image):
        self.image        = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (200, 200))
        # SCREEN.blit(self.image, [self.rect.x, self.rect.y])

    #점프 상태 확인하는 메서드
    def jump(self,j):
        self.isJump = j

    '''update'''
    def update(self):
        f = 0.7;
        # isJump 값이 0보다 큰지 확인
        if self.isJump > 0:
            # isJump 값이 2일 경우 속도를 리셋
            # 점프 한 상태에서 다시 점프를 위한 값

            # 이 코드를 주석처리하면 이중점프를 못한다.
            if self.isJump == 2:
                self.v = VELOCITY

            # 역학공식 계산 (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                F = (f * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                F = -(f * self.m * (self.v * self.v))

            # 좌표 수정 : 위로 올라가기 위해서는 y 좌표를 줄여준다.
            self.rect.y -= round(F)

            # 속도 줄여줌
            self.v -= 3

            # 바닥에 닿았을때, 변수 리셋
            if self.rect.bottom > WINDOW_HEIGHT:
                self.rect.bottom = WINDOW_HEIGHT
                self.isJump    = 0         #점프 판단
                self.twoJumpNo = 0      #점프 2단 이상 막기
                self.v = VELOCITY

    '''update'''

    # 자동차를 스크린에 그리기
    def draw_Characters(self):
        SCREEN.blit(self.image, [self.rect.x ,self.rect.y]) #이미지 복사해서 넣기


def main():
    global SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT

    #pygame 초기화 및 스크린 생성
    pygame.init()   # PyGame 라이브러리를 초기화
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('TEST')

    clock = pygame.time.Clock()

    #플레이어 자동차 생성
    player  = Characters()
    
    #그림
    # test = '../CookieRunGame/images/one.jpg'
    # test2 = '../CookieRunGame/images/two.jpg'
    # test3 = '../CookieRunGame/images/the.jpg'
    # test4 = '../CookieRunGame/images/fo.jpg'
    jump_img = '../CookieRunGame/images/jump.png'
    test = '../CookieRunGame/images/am01.png'
    test2 = '../CookieRunGame/images/am02.png'
    test3 = '../CookieRunGame/images/am03.png'
    test4 = '../CookieRunGame/images/am04.png'
    jump_img = '../CookieRunGame/images/jump.png'

    # jump_img = '../CookieRunGame/images/jump.png'
    player.load_image(test)  # 플레이어 캐릭터

    playing  = True
    leg_swap = 0;
    while playing:

        # 키가 눌린 상태 체크
        keys = pygame.key.get_pressed()
        # 스페이스키가 눌려있고, isJump가 2라면 1로 변경한다.
        # 이 작업을 해주지 않으면 스페이스가 눌려있는 상태면 플레이어가 계속 위로 올라가게 된다.
        if (keys[pygame.K_SPACE]):
            if player.isJump == 2:
                player.jump(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            # 화살표 키를 이용해서 플레이어의 움직임 거리를 조정해준다.
            # 키를 떼면 움직임 거리를 0으로 한다.
            if event.type == pygame.KEYDOWN:
                # 스페이스키를 눌렀을 때,
                # 0이면 바닥인 상태 : 1로 변경
                # 1이면 점프를 한 상태 : 2로 변경, 점프한 위치에서 다시 점프를 하게 된다. 즉, 이중점프
                if event.key == pygame.K_SPACE:
                    if player.twoJumpNo != 1:  #2단 점프
                        if player.isJump == 0:
                            player.jump(1)
                        elif player.isJump == 1:
                            player.jump(2)
                            player.twoJumpNo = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0

        # 배경색을 흰색으로
        SCREEN.fill(WHITE)

        ''' 게임 코드 작성 '''
        player.update()

        # ''' 게임 코드 끝 '''
        '''어몽어스 그리기'''
        if player.isJump == 0: # 바닥 일 때
            if leg_swap == 0:
                player.chan_image(test)  # 플레이어 캐릭터 이미지 바꾸기
                leg_swap = 1;

            elif leg_swap == 1:
                player.chan_image(test2)
                leg_swap = 2;

            elif leg_swap == 2:
                player.chan_image(test3)
                leg_swap = 3;

            elif leg_swap == 3:
                player.chan_image(test4)
                leg_swap = 0;
        else : # 1단 점프프
            player.chan_image(jump_img)
            if player.twoJumpNo == 1:
                player.chan_image(test)

        # 플레이어 캐릭터 화면에 그려주기
        player.draw_Characters()
        pygame.display.flip()  # 게임판 다시그리기

        # 초당 프레임 설정
        clock.tick(10)

if __name__ == '__main__':
    main()
