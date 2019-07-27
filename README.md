### ASR_metrics
Compute CER and WER

### Installation
```python
pip3 install ASR-metrics
```
### Uses

```python
$ python3
>>> from ASR_metrics import utils as metrics
>>> s1 = "When Amangkurat I took the throne of Mataram in 1646"
>>> s2 = "When Amangkurat I took of throne of Matara in 1646"
>>> metrics.calculate_cer(s1,s2)
0.09302325581395349
>>> metrics.calculate_wer(s1,s2)
0.2

````
