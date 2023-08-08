import zlib # for compress & decompress files
import json
import xlrd # for excel working
import os.path #for working with directories and files


def set_settings(folder, settings, primary_scales, secondary_scales,
                 save_signals, alarm_signals):
    
    compressed_data = open('Maplists/' + folder + '/MapList.js', 'rb').read()
    header = compressed_data[:4]
    body = compressed_data[4:]
    
    decompressed_body = zlib.decompress(body)
    data = json.loads(decompressed_body)
    
    # relay settings
    for group_key, group_val in data['list'][1].items():
        for function in group_val['jobs']:
            for setting in function['opt']:
                if setting['name'] in  settings.keys():
                    setting['val'] = settings[setting['name']]

    # delay settings
    for group_key, group_val in data['list'][2].items():
        for item in group_val:
            if item['name'] in settings.keys():
                item['time'] = settings[item['name']]

    # state settings
    for group_key, group_val in data['list'][3].items():
        for item in group_val:
            if item['name'] in settings.keys():
                item['state'] = settings[item['name']]    

    # Scale settings
    for i, value in enumerate(primary_scales):
        data['list'][9]['prime-scale'][i] = value
    
    for i, value in enumerate(secondary_scales):
        data['list'][9]['scale'][i] = value   
    
    # Alarm settings
    for i in range(4, 9): # List items where signals are stored
        for group_key, group_val in data['list'][i].items():
            for pin in group_val:
                s = group_key + '.' + pin['name']
                if s in save_signals:
                    pin['save'] = True
                elif 'save' in pin.keys():
                    pin.pop('save')
                if s in alarm_signals:
                    pin['alarm'] = True
                elif 'alarm' in pin.keys():
                    pin.pop('alarm')
    
    decompressed_body = json.dumps(data)

    body = zlib.compress(decompressed_body.encode('utf-8'))
    compressed_data = header + body
    
    f = open('Maplists/' + folder + '/MapList.js', 'wb')
    f.write(compressed_data)
    f.close()

def update_settings(subfolder, service_name):
    workbook = xlrd.open_workbook(subfolder + '/Settings.xls')
    worksheet = workbook.sheet_by_name('Лист1')
    
    settings = {}
    line = 1
    while ((line < worksheet.nrows) and (worksheet.cell(line, 1).value != '')):
        settings[worksheet.cell(line, 1).value] = worksheet.cell(line, 2).value
        line += 1
    
    primary_scales = []
    line = 1
    while ((line < worksheet.nrows) and (worksheet.cell(line, 4).value != '')):
        primary_scales.append(worksheet.cell(line, 4).value)
        line += 1
    
    secondary_scales = []
    line = 1
    while ((line < worksheet.nrows) and (worksheet.cell(line, 6).value != '')):
        secondary_scales.append(worksheet.cell(line, 6).value)
        line += 1
    
    line = 1
    save_signals = []
    while ((line < worksheet.nrows) and (worksheet.cell(line, 7).value != '')):
        save_signals.append(worksheet.cell(line, 7).value)
        line += 1    
    
    line = 1
    alarm_signals = []
    while ((line < worksheet.nrows) and (worksheet.cell(line, 9).value != '')):
        alarm_signals.append(worksheet.cell(line, 9).value)
        line += 1     
    
    set_settings(service_name, settings, primary_scales, secondary_scales,
                 save_signals, alarm_signals)
    
index = '2.2'
subfolder = 'P0XX1' # location of experiment files
service_name = 'P0XX2' # location of device service file


dirs = os.listdir()
for dir_ in dirs:
    if index in dir_:
        update_settings(dir_ + '/' + subfolder, service_name)