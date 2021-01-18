## RISParser

A simple python module for parsing files in standard RIS format.  The api follows the same basic pattern as the core csv module (reader/writer/DictReader/DictWriter, etc.). See the example below

```python
import ris_parser as ris

with open('filename.ris') as f:
    reader = ris.DictReader(f)
    for entry in reader:
        print(entry)
```
