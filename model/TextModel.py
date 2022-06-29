import torch.nn as nn

class TextModel(nn.Module):
    def __init__(self):
        super(TextModel, self).__init__()
        self.fc1 = nn.Linear(30, 150)
        self.batch1 = nn.BatchNorm1d(150)
        self.fc2 = nn.Linear(150, 15)
        self.batch2 = nn.BatchNorm1d(15)
        self.fc3 = nn.Linear(15, 3)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.8)
      
    def forward(self, x):
        x = self.fc1(x)
        x = self.batch1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.batch2(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc3(x)
        return x