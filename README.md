<h2 align="center">
  <br>
  <img src="./docs/source/branding/riacore.png" alt="Radio Intelligence Apps">
</h2>

<h3 align="center">Radio Intelligence Apps, By <a href="https://www.qoherent.ai/">Qoherent</a></h3>

<h4 align="center">Let's build intelligent radios together 📡🚀</h4>

<p align="center">
  <!-- PyPI -->
  <a href="https://pypi.org/project/ria">
    <img src="https://img.shields.io/pypi/v/ria"/>
  </a>
  <!-- License -->
  <a href="https://www.gnu.org/licenses/agpl-3.0">
    <img src="https://img.shields.io/badge/License-AGPLv3-blue.svg" />
  </a>
  <!-- Status -->
  <a href="https://pypi.org/project/ria">
    <img src="https://img.shields.io/pypi/status/ria"/>
  </a>
  <!-- Docs -->
  <a href="http://docs.radiointelligence.io/">
    <img src="https://img.shields.io/badge/docs-ria--core-blue"/>
  </a>
</p>


# RIA Core

RIA Core is the foundational, open-source core of [RIA Hub](https://riahub.ai/), an extensive AI development 
platform tailored for [software-defined radio](https://en.wikipedia.org/wiki/Software-defined_radio) (SDR).

RIA Core drives the creation of [intelligent radios](https://www.qoherent.ai/intelligentradio/), unlocking 
solutions in an increasingly congested, contested, and complex wireless spectrum. Learn more about RIA Core on 
our website [here](https://www.qoherent.ai/radiointelligenceapps-project/).


## 🌟 Key Features

- Synthesize modulated radio frequency (RF) recordings based on signals generated in Python, 
[GNU Radio](https://www.gnuradio.org/), or [MATLAB](https://www.mathworks.com/products/matlab.html), 
expediting prototyping and experimentation.


- Visualize and inspect recordings with [IQengine](https://iqengine.org/browser), simplifying data exploration.


- Curate RF datasets from [SigMF](https://github.com/sigmf/SigMF) recordings and 
store them in [HDF5](https://github.com/HDFGroup/hdf5) format, streamlining data management 
and enhancing accessibility.


- Accelerate model development with off-the-shelf deep learning models, tailored for radio applications, 
freeing up more time for research and development.


## 🚀 Want More RIA?

- Experience the complete, GUI-based AI development experience offered by 
[RIA Hub](https://www.qoherent.ai/radiointelligenceapps-hub/). This comprehensive solution provides an intuitive 
and feature-rich environment, empowering developers to explore, create, and optimize AI applications for SDR.


- [RIA RAN](https://www.qoherent.ai/radiointelligenceapps-ran/) allows seamless integration of high-performance ML 
inference software directly onto an open-source [gNodeB](https://inseego.com/resources/5g-glossary/what-is-gnb/), 
empowering radio engineers to leverage AI for sensing and communications.


## 🛠️ Getting Started

RIA Core is available at [PyPI](https://pypi.org/project/ria), and can be installed with pip:
```sh
pip install ria
```

Interfacing with your local SDR hardware may require additional drivers and configurations.

Please refer to the [documentation](http://docs.radiointelligence.io/) for more information on getting
started with RIA Core.


## 🐳 Docker Support

Coming soon: Docker support for building images for both CPU and GPU targets.


## 💻 Usage

RIA Core consists of importable modules and a set of command-line bindings, 
allowing you to execute key functionality from the command line.

For example, if we wanted to curate a dataset from a collection of SigMF recordings, apply an artificial IQ 
Imbalance, and save to file as a machine-learning ready dataset, we could do this from the command line with:
```sh
ria curate --recordings 'data/recordings' --output 'data/datasets/out.h5' --phase_imbalance $pi
```

Alternatively, we could achieve the same in Python with:
```python
from math import pi
from ria import curate
from ria.impairments import iq_imblance

# Curate a radio dataset from a collection of SigMF recordings.
dataset = curate(recordings='data/recordings')

# Apply an artificial IQ Imbalance.
dataset = iq_imblance(dataset=dataset, phase_imbalance=pi)

# Save the dataset to file.
dataset.to_h5('data/datasets/out.h5')
```

We can proceed to train a 4G LTE / 5G NR classifier using this dataset, and save the trained model to file
in ONNX format:
```sh
ria train --train_dataset 'data/datasets/out.h5' --model 'LTE_NR_CLassifier' --batchsize 4 --to_onnx 'models/classifier.onnx'
```

Equivalently, in Python:
```python
from ria.models import LTE_NR_CLassifier
from pytorch_lightning import Trainer
from torch.utils.data import DataLoader

# A custom RIA model, optimized for radio classification!
lte_nr_classifier = LTE_NR_CLassifier()  

# RIA datasets are compatible with the Torch DataLoader...
train_loader = DataLoader(dataset, batch_size=4)

# ...and can be trained using a PyTorch Lightning Trainer! 
trainer = Trainer()
trainer.fit(model=lte_nr_classifier, train_dataloaders=train_loader)

# Save model as ONNX graph
lte_nr_classifier.to_onnx("models/classifier.onnx")
```

If RIA's syntax feels familiar, that's because RIA is built on [PyTorch](https://pytorch.org/docs/stable/data.html) 
and [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/)! 

Additional back-ends can be made available. Please [contact us](https://www.qoherent.ai/contact/) for further details.


## 🤝 Contribution

We welcome contributions from the community! Whether it's a bug fix, new feature, or improvement, your 
input is valuable. If you would like to contribute directly to RIA, you will be invited to sign a contributor 
agreement, email us at [info@qoherent.ai](info@qoherent.ai) for more information.

If you have a larger project in mind, please [contact us](https://www.qoherent.ai/contact/) directly,
we'd love to collaborate with you. 🚀

If you are having issues, please let us know by posting the issue on our GitHub issue tracker 
[here](https://github.com/qoherent/ria/issues).

Qoherent is dedicated to fostering a friendly, safe, and inclusive environment for everyone.
Kindly review and adhere to our [Code of Conduct](.github/CODE_OF_CONDUCT.md).


## 🖊️ Authorship

RIA Core is developed and maintained by [Qoherent](https://www.qoherent.ai/), with the invaluable support of 
[many independent contributors](https://github.com/qoherent/ria/graphs/contributors).

If you are doing research with RIA, please cite our project:

> [1] Qoherent Inc., "Radio Intelligence Apps," 2024. [Online]. Available: https://github.com/qoherent/ria

If you like what we're doing, don't forget to give the project a star! ⭐


## 📄 License

RIA Core is **free and open-source**, released under [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html).

Alternative licensing options are available. Please [contact us](https://www.qoherent.ai/contact/) for further details.
