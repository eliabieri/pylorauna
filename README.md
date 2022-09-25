# Sauna Lorrainebad API Wrapper 🧖🏽‍♀️
In Bern, CH there's a super sweet sauna down at the Aare.  
Their current capacity can be seen on their [website](https://saunalorrainebad.ch) or through this little API wrapper.

## Example usage
```python
from pylorauna.lorauna import LoraunaClient

client = LoraunaClient()
data = client.get_data()
print(data.capacity_message)
# $ Mir hei no bis Endi Oktober Summerpouse.
```