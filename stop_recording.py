from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.recorder import *
from airtest.core.android.adb import *

auto_setup(__file__,devices=['android://127.0.0.1:5037/16186395'],logdir=r'D:\apks\log')

adb = ADB(serialno='16186395')
recorder = Recorder(adb)
recorder.stop_recording(output=r'D:\apks\log\music.mp4')