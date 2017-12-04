import torch 
from torch.autograd import Variable
import torch.nn as nn 
import torch.nn.functional as F 
import math


class YoloClassifier(nn.Module):

    def __init__(self,convs,class_size,batch_size):
        super(YoloClassifier,self).__init__()
        self.class_size = class_size
        self.batch_size = batch_size
        self.convs = convs
        self.classifier = nn.Conv2d(1024,class_size, kernel_size=3, padding=1)
        self._initialize_weights()
    
    def forward(self,x):
        x = self.convs(x)
        x = self.classifier(x)
        #print(x.size())
        batch_size = x.size()[0]
        #print(batch_size)
        x = x.view(batch_size,self.class_size,-1)
        x = torch.mean(x,dim=2)
        x = nn.LogSoftmax()(x)
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                m.weight.data.normal_(0, 0.01)
                m.bias.data.zero_()

