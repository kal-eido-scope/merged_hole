import filecmp,copy,sys
import os,json

OR = 'new_hole_crawler_2.0'
PG = 'new_hole_crawler_pg_2.0'
ME = 'merged'
IMG = 'data\img'
JSON = 'data\json'
MOV = 'data\mov'
LOG = 'data\log'
def get_cur_pid(pathi)->int:
    json_list = []
    for file_name in os.listdir(pathi):
        json_list.append(int(os.path.splitext(file_name)[0]))
    if json_list:
        json_list.sort()
        return json_list[-1]


def json_diff():
    json_diff = {}
    dir1 = os.path.join(OR,JSON)
    dir2 = os.path.join(PG,JSON)
    max1 = get_cur_pid(dir1)
    max2 = get_cur_pid(dir2)
    for i in range(1,max1+1):
        fn1 = os.path.join(dir1,'%06d.json'%i)
        fn2 = os.path.join(dir2,'%06d.json'%i)
        if os.path.exists(fn1):
            if os.path.exists(fn2):
                flag = filecmp.cmp(fn1,fn2)
                if flag:
                    json_diff[i] = 'same'
                    print('%d same'%i)
                else:
                    json_diff[i] = 'different'
                    print('%d different'%i)
            else:
                json_diff[i] = 'dir1'
                print('%d dir1'%i)
        else:
            if os.path.exists(fn2):
                json_diff[i] = 'dir2'
                print('%d dir2'%i)
            else:
                json_diff[i] = 'neither'
                print('%d neither'%i)
    if max1<max2:
        for i in range(max1,max2+1):
            json_diff[i] = 'dir2'
            print('%d dir2'%i)
    
    with open('json_diff.json','wb+')as f:
        f.write(json.dumps(json_diff,ensure_ascii=False,indent=4).encode('utf-8'))
    return json_diff

def img_diff():
    img_diff = {}
    dir1 = os.path.join(OR,IMG)
    dir2 = os.path.join(PG,IMG)
    img_or = os.listdir(dir1)
    img_or2 = sorted(img_or,key = lambda x:int(x))
    img_pg = os.listdir(dir2)
    img_pg_temp = img_pg.copy()
    for img_pid in img_or2:
        if img_pid in img_pg:
            temp = {}
            img_pg_temp.remove(img_pid)
            img_or_pid_all = os.path.join(dir1,img_pid)
            img_pg_pid_all = os.path.join(dir2,img_pid)
            imgs_2 = os.listdir(img_pg_pid_all)
            imgs_2_temp = imgs_2.copy()
            for imgn1 in os.listdir(img_or_pid_all):
                img1 = os.path.join(img_or_pid_all,imgn1)
                if imgn1 in imgs_2:
                    imgs_2_temp.remove(imgn1)
                    img2 = os.path.join(img_pg_pid_all,imgn1)
                    flag = filecmp.cmp(img1,img2)
                    if flag:
                        temp[imgn1] = 'same'
                    else:
                        temp[imgn1] = 'different'
                else:
                    temp[imgn1] = 'dir1'
            if imgs_2_temp:
                for item in imgs_2_temp:
                    temp[item] = 'dir2'
            img_diff[img_pid] = temp
            print('%s both'%img_pid)
        else:
            img_diff[img_pid] = 'dir1'
            print('%s dir1'%img_pid)
    if img_pg_temp:
        img_pg_temp2 = sorted(img_pg_temp,key=lambda x:int(x))
        for img_pid_temp in img_pg_temp2:
            temp = {}
            img2_temp = os.path.join(dir2,img_pid_temp)
            for imgn2 in os.listdir(img2_temp):
                temp[imgn2] = 'dir2'
            img_diff[img_pid_temp] = temp
        print('%s dir2'%img_pid_temp)
    return img_diff
    with open('img_diff.json','wb+')as f:
        f.write(json.dumps(img_diff,ensure_ascii=False,indent=4).encode('utf-8'))

def mov_diff():
    img_diff = {}
    dir1 = os.path.join(OR,MOV)
    dir2 = os.path.join(PG,MOV)
    img_or = os.listdir(dir1)
    img_or2 = sorted(img_or,key = lambda x:int(x))
    img_pg = os.listdir(dir2)
    img_pg_temp = img_pg.copy()
    for img_pid in img_or2:
        if img_pid in img_pg:
            temp = {}
            img_pg_temp.remove(img_pid)
            img_or_pid_all = os.path.join(dir1,img_pid)
            img_pg_pid_all = os.path.join(dir2,img_pid)
            imgs_2 = os.listdir(img_pg_pid_all)
            imgs_2_temp = imgs_2.copy()
            for imgn1 in os.listdir(img_or_pid_all):
                img1 = os.path.join(img_or_pid_all,imgn1)
                if imgn1 in imgs_2:
                    imgs_2_temp.remove(imgn1)
                    img2 = os.path.join(img_pg_pid_all,imgn1)
                    flag = filecmp.cmp(img1,img2)
                    if flag:
                        temp[imgn1] = 'same'
                    else:
                        temp[imgn1] = 'different'
                else:
                    temp[imgn1] = 'dir1'
            if imgs_2_temp:
                for item in imgs_2_temp:
                    temp[item] = 'dir2'
            img_diff[img_pid] = temp
            print('%s both'%img_pid)
        else:
            img_diff[img_pid] = 'dir1'
            print('%s dir1'%img_pid)
    if img_pg_temp:
        img_pg_temp2 = sorted(img_pg_temp,key=lambda x:int(x))
        for img_pid_temp in img_pg_temp2:
            temp = {}
            img2_temp = os.path.join(dir2,img_pid_temp)
            for imgn2 in os.listdir(img2_temp):
                temp[imgn2] = 'dir2'
            img_diff[img_pid_temp] = temp
        print('%s dir2'%img_pid_temp)
    return img_diff
    with open('mov_diff.json','wb+')as f:
        f.write(json.dumps(img_diff,ensure_ascii=False,indent=4).encode('utf-8'))

def write_json(fn0:str,js:dict):
    with open(fn0,'wb+') as f:
        f.write(json.dumps(js,ensure_ascii=False).encode('utf-8'))

def merge_diff_json(js1:dict,js2:dict,pid:str,logs:dict)->dict:
    dt1 = copy.deepcopy(js1)
    dt2 = copy.deepcopy(js2)
    dt2_comments = copy.deepcopy(dt2['data']['comments'])
    new_comments = []
    if dt1['data']['timestamp'] != dt2['data']['timestamp']:
        logs[pid] = 'not the same'
        return {}
    if dt1['data']['comments']:
        for cm1 in dt1['data']['comments']:
            new_comments.append(cm1)
            if cm1 in dt2['data']['comments']:
                dt2_comments.remove(cm1)
        if dt2_comments:
            for cm2_rest in dt2_comments:
                new_comments.append(cm2_rest)
    else:
        if dt2['data']['comments']:
            new_comments=dt2['data']['comments']
    final_comments = sorted(new_comments,key = lambda x:x['cid'])
    dt2['data']['comments'] = final_comments
    if final_comments:
        dt2['data']['last_comment_time'] = final_comments[-1]['timestamp']
        dt2['data']['n_comments'] = len(final_comments)
    return dt2

def merge_json(json_dif:dict):
    dir0 = os.path.join(ME,JSON)
    os.makedirs(os.path.join(ME,JSON),exist_ok=True)
    dir1 = os.path.join(OR,JSON)
    dir2 = os.path.join(PG,JSON)
    logs = {}
    try:
        for pid,value in json_dif.items():
            if int(pid)<37602:
                continue
            fn0 = os.path.join(dir0,'%06d.json'%int(pid))
            fn1 = os.path.join(dir1,'%06d.json'%int(pid))
            fn2 = os.path.join(dir2,'%06d.json'%int(pid))
            if value == 'same':
                with open(fn1,'r',encoding='utf-8')as f:
                    temp = json.loads(f.read())
                write_json(fn0,temp)
            elif value == 'dir1':
                with open(fn1,'r',encoding='utf-8')as f:
                    temp = json.loads(f.read())
                write_json(fn0,temp)
            elif value == 'dir2':
                with open(fn2,'r',encoding='utf-8')as f:
                    temp = json.loads(f.read())
                write_json(fn0,temp)
            elif value == 'different':
                with open(fn1,'r',encoding='utf-8')as f:
                    js1 = json.loads(f.read())
                with open(fn2,'r',encoding='utf-8')as f:
                    js2 = json.loads(f.read())
                temp = merge_diff_json(js1,js2,pid,logs)
                if temp:
                    write_json(fn0,temp)
            print('%s finished'%pid)
    except Exception as e:
        print(pid)
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])
        print(e.__traceback__.tb_lineno)
    log_path = os.path.join(ME,LOG)
    os.makedirs(log_path,exist_ok=True)
    logging_path = os.path.join(log_path,'merge_log.json')
    with open(logging_path,'wb+')as f:
        f.write(json.dumps(logs,ensure_ascii=False).encode('utf-8'))
def find_mismatch():
    json_err = []
    dir1 = os.path.join(OR,JSON)
    dir2 = os.path.join(PG,JSON)
    max1 = get_cur_pid(dir1)
    max2 = get_cur_pid(dir2)
    for i in range(1,max1+1):
        if i == 37603:
            continue
        fn1 = os.path.join(dir1,'%06d.json'%i)
        fn2 = os.path.join(dir2,'%06d.json'%i)
        if os.path.exists(fn1):
            if os.path.exists(fn2):
                try:
                    with open(fn1,'r',encoding='utf-8')as f1:
                        t1 = json.load(f1)
                    with open(fn2,'r',encoding='utf-8')as f2:
                        t2 = json.load(f2)
                    if t1['data']['timestamp']!=t2['data']['timestamp']:
                        if t1['code'] != -1:
                            json_err.append(i)
                except:
                    print(i)
    print(json_err)
def main():
    #find_mismatch()
    #json_dif = json_diff()
    with open('json_diff.json','r',encoding='utf-8')as f:
        json_dif = json.load(f)
    merge_json(json_dif)
    #img_dif = img_diff()
    #mov_dif = mov_diff()
if __name__ == '__main__':
    main()