import torch.nn as nn 

cfg = {
    'yolo_full': [32,'M', 64, 'M', 128,64,128,'M', 256,128, 256,'M',512,256,512,256,512,'M',1024,512,1024,512,1024],
    'tiny_yolo': [16,'M',32,'M',64,'M',128,'M',256,'M',512,'M',1024,1024],
    'small_classifier':[32,64,64,'M']
}

filter_size = {
    'yolo_full': [3,'M',3,'M',3,1,3,'M',3,1,3,'M',3,1,3,1,3,'M',3,1,3,1,3],
    'tiny_yolo': [3,'M',3,'M',3,'M',3,'M',3,'M',3,'M',3,3],
    'small_classifier':[3,3,3,'M']
}



def make_layers(cfg,filter_size, batch_norm=True,in_channels=3):
    layers = []
   
    i  = 0
    for v in cfg:
        
        if v == 'M':
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            pad = 0
            if(filter_size[i] == 3):
                pad = 1
                    
            conv2d = nn.Conv2d(in_channels, v, kernel_size=filter_size[i], padding=pad)
            if batch_norm:
                layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
            else:
                layers += [conv2d, nn.ReLU(inplace=True)]
            in_channels = v
        i += 1
    return nn.Sequential(*layers)


def net(network,in_channels=3):
    return make_layers(cfg[network],filter_size[network],batch_norm=True,in_channels=in_channels)