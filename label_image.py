import cv2
import csv


font = cv2.FONT_HERSHEY_SIMPLEX    #font
org = (5, 15)  # org 
fontScale = 0.5   # fontScale 
color = (255, 0, 0) # Blue color in BGR 
thickness = 2 # Line thickness of 2 px 

train_csv_path = "/home/raj/Downloads/9d34462453e311ea/dataset/train.csv"
image_directory_path = '/home/raj/Desktop/9d34462453e311ea/dataset/Train Images/'
labeled_images_output_path = '/home/raj/Downloads/9d34462453e311ea/dataset/labeled_images/'

with open(train_csv_path, "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for line in reader:
        print(line)
        img_path = line[0]
        label = line[1]
        img = cv2.imread(image_directory_path + img_path)
        img = cv2.putText(img, label , org, font,  
                fontScale, color, thickness, cv2.LINE_AA)
        
        cv2.imwrite(labeled_images_output_path + img_path, img)