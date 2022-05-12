import filecmp
import os,json

OR = 'new_hole_crawler_2.0'
PG = 'new_hole_crawler_pg_2.0'
IMG = 'data\img'
JSON = 'data\json'
MOV = 'data\mov'
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
            img_or_pid_all = os.path.join(dir1,img_pid)
            img_pg_pid_all = os.path.join(dir2,img_pid)
            temp = {}
            for imgn in os.listdir(img_or_pid_all):
                temp[imgn] = 'dir1'
            img_diff[img_pid] = temp
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
            img_or_pid_all = os.path.join(dir1,img_pid)
            img_pg_pid_all = os.path.join(dir2,img_pid)
            temp = {}
            for imgn in os.listdir(img_or_pid_all):
                temp[imgn] = 'dir1'
            img_diff[img_pid] = temp
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
    with open('mov_diff.json','wb+')as f:
        f.write(json.dumps(img_diff,ensure_ascii=False,indent=4).encode('utf-8'))

def main():
    #json_diff()
    img_diff()
    mov_diff()
if __name__ == '__main__':
    main()