import pygame,sys,coordinate,time
pygame.init()
size = width, height = 500,700
screen = pygame.display.set_mode(size)  # 显示窗口
image = pygame.image.load('5_last_term/page_02.jpg')
weight, height = image.get_size()

def play_clip(file,start,last):
    print (file)
    pygame.mixer.music.load (file)
    pygame.mixer.music.play (0, start )
    #time.sleep (last)
    #pygame.mixer.music.stop ( )
def chk_mousepos(term,unit,page,x,y):
    data = coordinate.date[term][unit][page]['coordinate']
    for j in data:
        print(j[0],j[1],j[2],j[3])
        if j[0] <= x and j[1] <= y and j[2] >= x and j[3] >=y:
            print('在范围内')
            return True
    return False

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos ( )
            print (x,y)
            in_pos = chk_mousepos('5_last_term','unit1','page_02',x,y)
            print (in_pos)
            if in_pos :
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    play_clip("5_last_term/unit1.mp3",5.6,5.7)



        image_trans = pygame.transform.smoothscale (image,(500,500//3*4))
        screen.blit(image_trans,(0,50))
        pygame.display.update ( )

pygame.quit()

#TODO:没有导航条，还没实现上一页下一页。
#TODO:播放音频经常失效，无声，原因未知。
#TODO:没有实现音频片段播放，只能暂时手动暂停。
#TODO:准备将音配切片方式实现。