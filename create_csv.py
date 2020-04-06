'''
Extract XML to CSV
'''

import os
import argparse
import csv



def get_csv():
  '''
  read xml and store the path in csv
  args:
    arguments : conatain the paths
  return:
    stored the path in CSV
  '''
  ann_path = '/home/raj/Downloads/raccoon_dataset-master/images/'
  csv_out = '/home/raj/quantiphi/object-detection/Yolo/data/imagedataset'
  paths = []
  for ann in sorted(os.listdir(ann_path)):
    paths.append(ann_path+ann)
  
  data = zip(paths)
  
  with open(csv_out+'dataset.csv', 'w') as fp:
    writer = csv.writer(fp)
    writer.writerows(data)
  fp.close()


def main():
  '''
  main function
  '''
  get_csv()
  

if __name__ == '__main__':
  main()
