configuration = {
    'origin_string' : r'myRIO-1950',
    'replace_string' : 'elRIO'
}
logfiles = open('C:/Users/Administrator/Desktop/replace_log.txt','w')

import datetime
import os
logfiles.write('\nExecution date: %s\nCurrent dir: %s\n\n'%(str(datetime.datetime.now()), os.getcwd()))


def replace_contents(file_name, config):
    try:
        s = file(file_name).read()
        f = open(file_name,'wb+')
        import re
        res = re.sub(config['origin_string'], config['replace_string'], s);
        f.write(res)
        f.close()
        logfiles.write('%s\n'%file_name)
    except Exception as e:
        print e

def main():
    sub_folders = [os.getcwd()]
    while len(sub_folders)>0:
        cur_folder = sub_folders.pop(0)
        # print cur_folder
        for file_name in os.listdir(cur_folder):
            full_file_name = os.path.join(cur_folder,file_name)
            if os.path.isdir(full_file_name):
                if file_name[0] != '.':
                    sub_folders.append(full_file_name)
            else:
                if file_name[-4:]=='.ini':
                    replace_contents(full_file_name, configuration)

if __name__ == '__main__':
    main()
