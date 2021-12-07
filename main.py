# -*- encoding=utf8 -*-
__author__ = "whosyourdaddy"
__title__ = "网易云音乐测试用例"
__desc__ = """
网易云音乐app，测试练习demo（含详细注释） 
1.录制运行视频，用例完成后自动生成报告
2.进入网易云音乐首页
3.找到陈小春的指定歌曲（我没那种命）
4.获取网络热歌榜的所有歌名
"""

# 引用的相关所有api
from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.recorder import *
from airtest.core.android.adb import *

# 连接设备，bde5aec3是设备名（小米10），logdir=是设置的log存放路径,
auto_setup(__file__, devices=['android://127.0.0.1:5037/16186395'], logdir=r'D:\apks\log')


# 进入网易云的方法
def enter_music():
    # 点击不同意
    poco("android.widget.FrameLayout").offspring("com.netease.cloudmusic:id/quit").click()
    # 休眠1秒
    sleep(1)
    # 判断下面这个绝对路径的图片是否存在，msg是报告中的断言参数提示信息
    assert_not_exists(
        Template(r"C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\tpl1630575904738.png"),
        '不同意并退出')
    # 启动这个app，包名可通过adb命令获取，adb shell dumpsys window|grep mCurrent 获取当前启动的应用包名
    start_app('com.netease.cloudmusic')
    sleep(1)
    # 点击同意
    poco("android.widget.FrameLayout").offspring("com.netease.cloudmusic:id/agree").click()
    sleep(2)
    # 点击授权
    poco("com.netease.cloudmusic:id/permissionGrant").click()
    # 等待同意这个控件出现，设定的是60秒超时后报错
    # poco("com.netease.cloudmusic:id/agree").wait_for_appearance(timeout=60)
    # 等待图片出现
    # wait(Template(r'C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\tpl1630584938526.png'))
    # sleep(1)
    # 点击允许
    # poco("com.android.packageinstaller:id/permission_allow_button").click()

    # 点击授权（各个设备的原生态授权类型不一致，故需适配各个类型的设备）
    poco("android.widget.FrameLayout").offspring("com.lbe.security.miui:id/permission_allow_button").click()
    # 二次点击允许
    # poco("com.android.packageinstaller:id/permission_allow_button").click()
    # poco("com.lbe.security.miui:id/permission_allow_foreground_only_button").click()

    # 等待加载logo出现，等待120s若超时则报错
    wait(Template(r'C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\1.png'),
         timeout=120)
    # 等待勾选的同意协议对话框出现
    # poco("com.netease.cloudmusic:id/agreeCheckbox").wait_for_appearance()
    # 点击勾选当前页面授权信息的同意
    poco("com.netease.cloudmusic:id/agreeCheckbox").click()
    # 点击立即体验
    poco("com.netease.cloudmusic:id/trial").click()
    sleep(5)
    # 点击开屏的广告，[0.503, 0.685]是具体的绝对坐标
    poco("android.widget.ImageView").click([0.503, 0.685])
    sleep(3)
    # 点击返回上一层
    poco("转到上一层级").click()
    # 判断以下图片是否存在，若存在则判断成功进入网易云
    assert_exists(
        Template(r'C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\tpl1630587179240.png'))


# 查找音乐的方法
def find_music():
    # 点击顶部导航栏
    poco("com.netease.cloudmusic:id/searchBar").click()
    sleep(5)
    # 输入文本 陈小春
    text('陈小春')
    # 判断指定的图片是否存在，若找到指定的图片则报告中提示信息：找到陈小春的歌单
    assert_exists(
        Template(r'C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\tpl1630587565760.png'),
        '找到陈小春的歌单')
    # 点击播放
    poco("com.netease.cloudmusic:id/actionView").click()
    # 点击返回上级
    poco("转到上一层级").click()
    # 当条件是True时（True这个条件默认都是真的），执行下面的操作
    while True:
        # 判断如果不存在以下指定的歌曲图片，threshold这个参数是指图片适配的精准度
        if not exists(Template(
                r'C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\tpl1630652067668.png',
                threshold=0.7)):
            # 底部导航栏从右向左活动切到下一首
            poco.swipe([0.624, 0.944], [0.255, 0.944])
        # 如果存在上面的图则进入下面的代码体
        else:
            # 打印文本（不会显示在报告中，会显示在运行时的log中供调试脚本）
            print('已找到目标歌曲')
            sleep(1)
            # 点击打开歌曲专辑详情
            poco("com.netease.cloudmusic:id/iv_smallAlbumCover").click()
            sleep(1)
            # 点击爱心，加入收藏
            poco("com.netease.cloudmusic:id/likeBtn").click()
            # 跳出当前循环体
            break

    # 执行四次循环，注3不代表3次，循环是下标0，1，2
    for i in range(3):
        # 点击手机硬按键的返回
        keyevent('BACK')
    sleep(1)


# 爬取网络热歌榜的方法
def Crawling_music():
    # 点击poco中获取文本是’排行榜‘的控件
    poco(text='排行榜').click()
    sleep(2)
    # 循环体（判断为True，True的话默认情况下都是True，即死循环）
    while True:
        # 判断热歌榜的图片不存在
        if not exists(Template(
                r'C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\tpl1630656406828.png')):
            # 不存在的话界面向下滑动，[0.531, 0.733], [0.531, 0.225]；第一个是x轴，第二个是y轴，从[0.531, 0.733]起始向[0.531, 0.225]滑动
            poco.swipe([0.531, 0.733], [0.531, 0.225])
        # 如果存在
        else:
            # 打印文本到log中
            print('找到网络热歌榜')
            sleep(2)
            # 点击网络热歌榜文本的地方
            poco(text='热歌榜').click()
            # 跳出循环
            break
    # 断言网络热歌榜的图是否存在，在报告中断言判断的地方打印’进入热歌榜‘
    assert_exists(
        Template(r'C:\Users\Administrator\PycharmProjects\pythonProject\HelloWorld\airtestimg\20210908192851.png'),
        '进入热歌榜')
    # 定义一个空数组用于存放排行榜的歌名
    titles = []
    # 定义数组目前的长度和最终的长度
    # current_count, last_count = len(titles), len(titles)

    # 死循环
    while True:
        # last_count这个变量=titles这个数组的长度
        last_count = len(titles)
        # for循环，声明一个变量title，在poco控件的这个数列范围内
        for title in poco("android.widget.LinearLayout").offspring("com.netease.cloudmusic:id/musicInfoList").child(
                "com.netease.cloudmusic:id/musicListItemContainer"):
            # 声明一个变量a，等于歌名循环
            a = title.offspring("com.netease.cloudmusic:id/songName")
            # 判断如果歌名的这个对应的控件存在
            if not a.exists():
                # 跳出当前if判断
                continue
            # 声明一个变量name，等于a这个控件的具体文本值，get_text()方法是获取文本
            name = a.get_text()
            # 判断name不在titles（之前声明的空数列）当这个条件为True时
            if not name in titles:
                # 则在titles这个数组后面增加这个歌名的文本，append是数组后直接增加的意思
                titles.append(name)
                # log(name)
                # 在log输出中打印name
                print(name)
        # 声明一个current_count的参数等于titles的长度
        current_count = len(titles)
        # 从[0.5, 0.7]滑动到[0.5, 0.1]，持续时间是2秒
        poco.swipe([0.5, 0.7], [0.5, 0.1], duration=2)
        sleep(1)

        # 当两者数值相等，即current_count不再增加时，表明当前所有歌曲已读取完毕
        if current_count == last_count:
            # 打印在报告中
            log('总共爬取' + str(last_count) + "首歌曲的名称")
            # 打印在log中
            print('总共爬取' + str(last_count) + '首歌曲的名称~')
            # 打印在报告中
            log('全部歌名:' + str(titles))
            # 跳出死循环
            break


# 尝试以下方法，一般是try（尝试代码），catch（若代码报错则进入catch中进行报错处理），finally（不管代码执行成功与否都会执行的代码体）
try:
    # 给adb这个变量赋值
    adb = ADB(serialno='16186395')
    # 实例化recorder
    recorder = Recorder(adb)
    # 调用start_recording()这个方法，录像启动的方法
    recorder.start_recording()
    # 清除'com.netease.cloudmusic'这个app，等于初始化这个app，确保测试环境的纯净，
    # 'com.netease.cloudmusic'这个值的获取方式通过adb命令：adb shell dumpsys window|grep mCurrent 获取当前启动的应用包名
    clear_app('com.netease.cloudmusic')
    # 启动'com.netease.cloudmusic'这个app
    start_app('com.netease.cloudmusic')
    sleep(5)
    # poco初始化
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    # 执行方法，即测试用例
    enter_music()
    find_music()
    Crawling_music()
    # 关闭'com.netease.cloudmusic'这个app
    stop_app('com.netease.cloudmusic')
    # 录像结束后存放在output=r'D:\apks\log\music.mp4'路径下
    recorder.stop_recording(output=r'D:\apks\log\music.mp4')

# 不管上述方法执行成功与否都会执行finally下的代码体
finally:
    # 生成airtest配套的测试报告
    simple_report(__file__, logpath=r'D:\apks\log', output=r'D:\apks\log\log.html')
