from os import path
import pathlib
import datetime
import sys
sys.path.append('D:\\Workspace\\Python_Work\\Temp_Orange_Automation')
from Driver.DriverScript import driver
from Application_Functions.LogUtility import random_id

PathOfScreenShots = 'D:\\Workspace\\Python_Work\\Temp_Orange_Automation\\HTML_Report\\ScreenShots'
PathOfReportFolder = 'D:\\Workspace\\Python_Work\\Temp_Orange_Automation\\HTML_Report'
var_folder = str(datetime.datetime.now())

var_folder1 = var_folder.replace(':','-')
var_folder2 = var_folder1.replace('.','-')

ReportFileName = str('HTML_Report_')+var_folder2+str('.html')
ReportFilePath = str(PathOfReportFolder)+'\\'+ReportFileName


def report_log(action,expected,actual,status):
    try:
        file = open(ReportFilePath, 'a')
        if status.lower() == 'Pass'.lower():
            all_information = '<!-- Test step name-->' \
            '<tr>' \
            '<td>' + action + '</td>' \
            '<td>' + expected + '</td>' \
            '<td>' + actual + '</td>' \
            '<td bgcolor="###00FF00">' + status + '</td>' \
            '</tr>'
            file.write(all_information+'\n')

        elif status.lower() == 'Fail'.lower():
            var_screenshot = random_id(5,'png')
            screen_shot_location = PathOfScreenShots+'\\'+var_screenshot
            driver.save_screenshot(screen_shot_location)
            all_information = '<!-- Test step name-->' \
            '<tr>' \
            '<td>' + action + '</td>' \
            '<td>' + expected + '</td>' \
            '<td>' + actual + '</td>' \
            '<td bgcolor="FF0000"><a href='+screen_shot_location+'>'+status+'</a> </td>' \
            '</tr>'
            file.write(all_information + '\n')

        file.close()
    except(NameError,FileNotFoundError) as er:
        print('Error message-',er)


def inserttestcase(testcase):
    file = open(ReportFilePath, 'a')
    all_information = '<table style="width:90%";>' \
    '<tr>' \
    '<h4><th bgcolor="##CCCCFF"; colspan="4";>' + testcase + '</th></h4>' \
    '</tr>' \
    '<tr>' \
    '<th width="20%">Action</th>' \
    '<th width="30%">Expected</th>' \
    '<th width="30%">Actual</th>' \
    '<th>Status</th>' \
    '</tr>'
    file.write(all_information + '\n')
    file.close()

def startreport():
    if path.exists(ReportFilePath) != True:
        file = open(ReportFilePath, 'w')
        file.close()

    file = open(ReportFilePath, 'a')
    all_information = '<html>' \
    '<head>' \
    '<style>p.indent{ pading-left: 1.8em}</style>' \
    '<style>' \
    'table, th, td {' \
    'border: 1px solid black;' \
    'border-collapse: collapse;' \
    'margin-left: auto;margin-right: auto;' \
    '}' \
    'th, td {' \
    'padding: 4px;' \
    'text-align: left;' \
    '}' \
    '</style>' \
    '</head>' \
    '<body>' \
    '<!-- Report description-->' \
    '<div class="container">' \
    '<h1 style="font-family:courier;">&nbsp;&nbsp;&nbsp;Automation with Selenium and Python</h1>' \
    '<h3 style="color:blue;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Orange HRM</h3>' \
    '<p style="padding-right: 5px;"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Start time:</strong> </p>' \
    '<p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;End time:</strong></p>' \
    '<p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Summary:</strong></p>'

    file.write(all_information + '\n')
    file.close()


def endreport():
    file = open(ReportFilePath, 'a')
    all_information = '</div>' \
    '</body>' \
    '</html>'
    file.write(all_information + '\n')
    file.close()


def capturescreenshot():
    file = open(ReportFilePath,'a')
    var_screenshot = random_id(5, 'jpg')
    screen_shot_location = PathOfScreenShots + '\\' + var_screenshot
    driver.save_screenshot(screen_shot_location)
    all_information = '<tr>' \
    '<td colspan = "3"; > Captured screenshot </td >' \
    '<td bgcolor = "CCEEEE" ><a href ='+screen_shot_location+'>' \
    'Click here </a></td>' \
    '</tr>'

    file.write(all_information + '\n')
    file.close()
