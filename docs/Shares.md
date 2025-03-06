# Shares

Specifies a list of Shares.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str** | Specifies the pagination cookie. | [optional] 
**shares** | [**List[Share]**](Share.md) | Specifies the list of shares. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.shares import Shares

# TODO update the JSON string below
json = "{}"
# create an instance of Shares from a JSON string
shares_instance = Shares.from_json(json)
# print the JSON string representation of the object
print(Shares.to_json())

# convert the object into a dict
shares_dict = shares_instance.to_dict()
# create an instance of Shares from a dict
shares_from_dict = Shares.from_dict(shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


