# Recoveries

Specifies list of Recoveries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recoveries** | [**List[Recovery]**](Recovery.md) | Specifies list of Recoveries. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recoveries import Recoveries

# TODO update the JSON string below
json = "{}"
# create an instance of Recoveries from a JSON string
recoveries_instance = Recoveries.from_json(json)
# print the JSON string representation of the object
print(Recoveries.to_json())

# convert the object into a dict
recoveries_dict = recoveries_instance.to_dict()
# create an instance of Recoveries from a dict
recoveries_from_dict = Recoveries.from_dict(recoveries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


