import torch as T
import torch.nn as nn
import torch.nn.functional as F

class RNN(nn.Module):
    # input_size = number of features in X
    # hidden_size = number of feature in hidden state
    # num_layers = number of chained units
    def __init__(self, input_size, hidden_size, num_layers, batch_size, seq_len) -> None:
        super().__init__()
        self.num_layer = num_layers
        self.hidden_size = hidden_size
        self.batch_size = batch_size
        self.rnn = nn.RNN(input_size=input_size, hidden_size=hidden_size,\
                          num_layers=num_layers, batch_first=True)
        self.fc1 = nn.Linear(self.batch_size * self.hidden_size, 1024)
        self.fc2 = nn.Linear(1024, self.batch_size * self.hidden_size)

    def forward(self, x):
        h_0 = T.zeros((self.num_layer, self.batch_size, self.hidden_size))

        rnn_out, h_n = self.rnn(x, h_0)
        last_hidden = h_n[-1]

        x = F.relu(last_hidden.flatten()) # added this line, you can activate also the last hidden layer, for better performance
        x = F.relu(self.fc1(x))
        return self.fc2(x)

        # return rnn_out, h_n, last_hidden


model = RNN(9, 5, 10, 32, 20)

data = T.rand((32, 20, 9))

pred = model(data)

print(pred.resize(model.batch_size, model.hidden_size))
