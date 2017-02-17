import matplotlib.pyplot as plt
import numpy as np

def ShowMeans(means, number=0):
  """Show the cluster centers as images."""
  plt.figure(number)
  plt.clf()
  for i in xrange(means.shape[1]):
    plt.subplot(1, means.shape[1], i+1)
    plt.imshow(means[:, i].reshape(48, 48), cmap=plt.cm.gray)
  plt.draw()
  raw_input('Press Enter.')

def ShowMeans2(means, number=0):
  """Show the cluster centers as images."""
  plt.figure(number)
  plt.clf()
  for i in xrange(means.shape[3]):
    plt.subplot(1, means.shape[3], i+1)
    plt.imshow(means[:,:,0,i], cmap=plt.cm.gray)
  plt.draw()
  raw_input('Press Enter.')

def plotProb(prob, target):
  """Show the cluster centers as images."""
  plt.xticks([1, 2, 3, 4, 5, 6, 7], ['1-Anger', '2-Disgust', '3-Fear', '4-Happy', '5-Sad', '6-Surprise', '7-Neutral'])
  plt.bar([1, 2, 3, 4, 5, 6, 7], prob,align='center')
#  plt.axis([0.5, 7.5, 0, 1.2])
  plt.title('Probability distribution for a sample {}'.format(target))
  plt.ylabel('Probability')
  plt.xlabel('Emotion')
  plt.show()