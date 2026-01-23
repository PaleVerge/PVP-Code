with open('/mnt/4FC1289514E05A01/newfolder/好东西.txt', 'r', encoding='utf-8') as f1,\
    open('好东西2.0.txt','w', encoding='utf-8') as f2:
        for line in f1:
            line=line.strip()
            line=line.replace('无名杀', '宝宝杀（乐）')
            print(line)
            f2.write(line + '\n')