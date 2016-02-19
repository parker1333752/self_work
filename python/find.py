configuration = {
    #'find_string' : r'(myRIO.\S+)|(myRIO$)',
    'find_string' : r'(elRIO)',
}
logfiles = open('C:/Users/Administrator/Desktop/replace_log.txt','w')

import datetime
import os
logfiles.write('\nExecution date: %s\nCurrent dir: %s\n\n'%(str(datetime.datetime.now()), os.getcwd()))

outputs = {}

def find_contents(file_name, config):
    try:
        f = file(file_name)
        import re
        s = f.readline()
        line_num = 1
        while not s == '':
            for x in re.findall(config['find_string'], s):
                if x not in outputs:
                    outputs[x] = {}
                if file_name not in outputs[x]:
                    outputs[x][file_name] = []
                outputs[x][file_name].append((line_num, s))
            s = f.readline()
            line_num += 1

        f.close()
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
                    find_contents(full_file_name, configuration)


if __name__ == '__main__':
    main()
    for x in outputs:
        if type(x) == tuple:
            logfiles.write('\npattern: "%s"\n'%(x[0] or x[1]))
        else:
            logfiles.write('\npattern: "%s"\n'%(x))

        for file_name in outputs[x]:
            logfiles.write('\t%s:\n'%(file_name))
            for line in outputs[x][file_name]:
                s = line[1]
                if s[-1] == '\n':
                    s = s[:-1]
                logfiles.write('\t\t[line %s]%s\n'%(line[0],s))
