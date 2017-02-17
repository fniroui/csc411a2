import numpy as plt
import matplotlib.pyplot as plt

#For learning rate
# plt.xticks([1 ,2, 3, 4, 5, ],['0.001','0.05','0.01','0.1','1.0'])
# plt.plot([1 ,2, 3, 4, 5, ],[1.84815 , 1.10297 , 0.82335, 0.43665 , 1.86420  ], 'bo', label='Training')
# plt.plot([1 ,2, 3, 4, 5, ], [1.85101 , 1.10436, 0.87704 , 0.63323, 1.86102   ], 'go', label='Validation')
# plt.axis([0, 5.5, 0, 2])
# plt.legend(loc=4)
# plt.title('Cross-Entropy for different Learning Rates $\epsilon$ for CNN')
# plt.ylabel('Error')
# plt.xlabel('Learning Rate $\epsilon$')
# plt.show()


#For momentum
# plt.xticks([1 ,2, 3, 4],['0.0','0.3','0.6','0.9'])
# plt.plot([1 ,2, 3, 4],[0.43665 ,  0.35368 ,0.21042,1.86147  ], 'bo', label='Training')
# plt.plot([1 ,2, 3, 4],[0.63323  , 0.69299  ,0.80755  ,1.85794  ], 'go', label='Validation')
# plt.axis([0, 4.5, 0.0, 2.0])
# plt.legend(loc=0)
# plt.title('Cross-Entropy for different Momentum for NN')
# #plt.title('Accuracy for different Momentum for CNN')
# plt.ylabel('Error')
# #plt.ylabel('Accuracy')
# plt.xlabel('Momentum')
# plt.show()

# #For Batch Size
# plt.xticks([1 ,2, 3, 4, 5],['1','10','100','500','1000'])
# plt.plot([1 ,2, 3, 4, 5],[1.88155 ,1.25564 ,0.43665 ,1.11511 ,3.02981 ], 'bo', label='Training')
# plt.plot([1 ,2, 3, 4, 5],[1.88067 ,1.71583 ,0.63323 ,1.07845 ,2.84858 ], 'go', label='Validation')
# plt.axis([0, 5.5, 0.0, 3.2])
# plt.legend(loc=0)
# plt.title('Cross-Entropy for different batch sizes for CNN')
# #plt.title('Accuracy for different batch sizes for CNN')
# plt.ylabel('Error')
# #plt.ylabel('Accuracy')
# plt.xlabel('Batch Size')
# plt.show()

#For 3.3
plt.xticks([1 ,2, 3],['[2 16]','[15 16]','[30 16]'])
plt.plot([1 ,2, 3],[0.28542 , 0.74748 ,0.28542 ], 'bo', label='Training')
plt.plot([1 ,2, 3],[0.27924 ,0.70883  ,0.27924  ], 'go', label='Validation')
plt.axis([0.5, 3.5, 0, 0.8])
plt.legend(loc=0)
#plt.title('Cross-Entropy for different number of filters in the first layer of CNN')
plt.title('Accuracy for different number of filters in the first layer of CNN')
#plt.ylabel('Error')
plt.ylabel('Accuracy')
plt.xlabel('Number of Units')
plt.show()