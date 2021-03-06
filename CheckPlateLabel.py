
# IMG_FILE_PATH = "C:\Users\pc\Desktop\Dataset_for_LPR-master\Black-box_01"
LABEL_FILE_PATH = "C:/Users/pc/Desktop/보도육교2/보도육교2_part5/"
PLATE_FILE_PATH = "C:/Users/pc/Desktop/보도육교2/보도육교2_plate/"

currIdx = 599
currSubIdx = 0
currFile = 'DSCF1' + str('%03d' % currIdx) + str('_%d' % currSubIdx if currSubIdx != 0 else '')

for i in range(160):
    for j in range(5):
        label_count = 0
        try:
            f = open(file=LABEL_FILE_PATH + currFile + '.txt', mode='r', encoding='utf-8')
            for line in f:
                if line[0] == '9':
                    label_count += 1
            # print('label', currFile, label_count)
            f.close()
        except:
            # print("no label file name such", currFile)
            print(end="")
            # currIdx += 1

        plate_count = 0
        try:
            f = open(file=PLATE_FILE_PATH + currFile + '.txt', mode='r')
            plate_count = len(f.readlines())
            # print('plate', currFile, plate_count)
            f.close()
        except:
            # print("no plate file name such", currFile)
            print(end="")

        if plate_count != label_count:
            print('label', currFile, label_count)
            print('plate', currFile, plate_count)
            print(currFile, '\n')
        currSubIdx += 1
        currFile = 'DSCF1' + str('%03d' % currIdx) + str('_%d' % currSubIdx if currSubIdx != 0 else '')
    currSubIdx = 0
    currIdx += 1
print(currFile, 'done')