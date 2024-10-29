# Code Citations

## License: MIT

<https://github.com/kmcken/DeclineCurveAnalysis/tree/905ce3c9188eaf5731bf73d38b9c374fd92a36f2/main.py>

```python

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler
```

## License: unknown

<https://github.com/Farama-Foundation/Minari/tree/fb4ffb8788b7d66e86a8bc8f282c5f89c2bdd15f/docs/tutorials/using_datasets/behavioral_cloning.py>

```python
.fc3 = nn.Linear(128, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
```

## License: unknown

<https://github.com/karanwxliaa/MultiOmics-Research/tree/034a417d8e1d8f0547ab361871207604491b64f2/STAGATE/arch2/model.py>

```python
fc3 = nn.Linear(128, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

```

## License: unknown

<https://github.com/reXne/gym_simulation/tree/a96f630bcdd7a8156e34b7f13c028a8d18ddb3ed/src/train/example_3.py>

```python
, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, output_dim)

    def forward(self, x):
        x = torch.
```
