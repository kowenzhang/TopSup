from PIL import Image
from common import screenshot, ocr, methods
import time
import configparser
from pbcgetanswer import find_match

if __name__ == '__main__':
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('./config/configure.conf', encoding='utf-8')

    while True:
        # 截图
        t = time.perf_counter()
        screenshot.check_screenshot()

        # end_time = time.clock()
        # print(end_time - t)

        img = Image.open("./screenshot.png")

        # 文字识别,可选 Tesseract 和 Baidu ,请在 config/configure.conf 中进行相应配置

        # ocr_img: 需要分别截取题目和选项区域，使用 Tesseract
        # ocr_img_tess： 题目和选项一起截，使用 Tesseract
        # ocr_img_baidu： 题目和选项一起截，使用 baidu ocr，需配置 key

        # question, choices = ocr.ocr_img(img, config)
        question = ocr.ocr_pbc_question(img, config)
        # question, choices = ocr.ocr_img_baidu(img, config)

        # end_time2 = time.clock()
        # print(end_time2 - end_time)

        # 用不同方法输出结果，取消某个方法在前面加上#

        # # 打开浏览器方法搜索问题
        # methods.run_algorithm(0, question, choices)
        # # 将问题与选项一起搜索方法，并获取搜索到的结果数目
        # methods.run_algorithm(1, question, choices)
        # # 用选项在问题页面中计数出现词频方法
        # methods.run_algorithm(2, question, choices)

        # 多线程
        find_match(question)

        t1 = time.perf_counter()
        print('用时: {0}'.format(t1 - t))

        go = input('输入回车继续运行,输入 n 回车结束运行: ')
        if go == 'n':
            break

        print('------------------------')