import lorem
import os

# class ChangerLog:
#     def __init__(self):
#         self.file_name = []
    
#     def add_element(self, pth:str):
#         self.file_name.append(pth)

def printer_path(pth:str, lv:int=0, status:bool=True):
    msg = '{0}|{3}{1} {2}'.format(' '*lv, '' if status else '[x]', pth.split(os.sep)[-1], '-'*lv)
    print(msg)
    return msg

def folder_navigator(pth: str, lv:int=0):
    
    for _ in os.listdir(pth):
        element = os.sep.join([pth, _])

        if os.path.isfile(element):
            combo(element, lv)
        else:
            printer_path(element, lv)
            folder_navigator(element, lv+2)

def write_file(fn: str, lv: list):
    with open(fn, 'wb') as f:
        f.writelines(lv)

def read_file(fn: str) -> list:
    with open(fn, 'rb') as c:
        lines = c.readlines()
    return lines

def replacer(lv: list) -> list:
    return [ lorem.get_sentence().encode() for _ in range(len(lv)*5)]

def combo(fpn: str, lv: int=0):
    try:
        bSuccess = True
        l = read_file(fpn)
        l = replacer(l)
        write_file(fpn, l)
    except Exception as e:
        bSuccess = False
        print(e)
    finally:
        printer_path(fpn, lv, bSuccess)

def run(pth: str):
    print('- - - START REPLACE SCRIPT - - -')
    folder_navigator(pth)
    print('- - - END  REPLACE  SCRIPT - - -')

# test_pth = os.sep.join([os.getcwd(), 'prova'])
# print('Avvio script su path:', test_pth)
# run(test_pth)

if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser(description='Some test')
    # parser.add_argument('--h', dest='h dest', help='print help message')
    import sys
    args = sys.argv
    if len(args) > 1:
        execute_path = sys.argv[1]
        if os.path.isdir(execute_path):
            run(execute_path)
        elif os.path.isfile(execute_path):
            combo(execute_path)
        else:
            print('[ERROR] input value is not correct')
    else:
        print('[ERROR] no input values')