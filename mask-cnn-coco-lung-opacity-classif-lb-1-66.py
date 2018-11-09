# Fork V8 Mask-RCNN and COCO transfer learning by Henrique Mendonça/Andy Harless
# Fork Lung Opacity Classification Transfer Learning by Kevin Mader

import pandas as pd

sub = pd.read_csv('checkpoints/submission.csv')
probs = pd.read_csv('checkpoints/image_level_class_probs.csv', usecols=[0,1])

sub = pd.merge(sub, probs, on='patientId')
sub.loc[sub['Lung Opacity']<0.16,'PredictionString'] = None
sub.drop(['Lung Opacity'],1,inplace=True)

sub.to_csv('subprobs16.csv', index=False)
