def sam():
    model_path = './data/utils/my_model.pb'
    peop_counter = People_Counter(path=model_path)
    threshold = 0.4
    no=1
    for n in pbar(glob.glob("./data/images/test/*.jpg")):
        count=0
        img = cv2.imread(n)
        img = cv2.resize(img, (640, 480))

        boxes, scores, classes, num = peop_counter.detect(img)

        for i in range(len(boxes)):
            if classes[i] == 1 and scores[i] > threshold:
                box = boxes[i]
                cv2.rectangle(img,(box[1],box[0]),(box[3],box[2]),(255,0,0),2)
                count+=1
        cv2.putText(img,'Count = '+str(count),(10,400),cv2.FONT_HERSHEY_SIMPLEX, 1.25,(255,255,0),2,cv2.LINE_AA)
        cv2.imwrite("./results/result%04i.jpg" %no, img)
        no+=1
    return "\n\t\t\tSuccessfully saved all results!\n"
