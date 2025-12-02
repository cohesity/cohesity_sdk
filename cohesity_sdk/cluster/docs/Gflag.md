# Gflag

Specifies the attributes of a service gflag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear** | **bool** | If Clear is set to true, the GFlag is removed | [optional] [default to False]
**name** | **str** | Specifies the name of the gflag. | [optional] 
**product_model** | **str** | Specifies product model this gflag set on. | [optional] 
**reason** | **str** | Specifies the reason for setting the gflag. | [optional] 
**timestamp** | **int** | Specifies timestamp when gflag was set. | [optional] 
**value** | **str** | Specifies the value of the gflag. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gflag import Gflag

# TODO update the JSON string below
json = "{}"
# create an instance of Gflag from a JSON string
gflag_instance = Gflag.from_json(json)
# print the JSON string representation of the object
print(Gflag.to_json())

# convert the object into a dict
gflag_dict = gflag_instance.to_dict()
# create an instance of Gflag from a dict
gflag_from_dict = Gflag.from_dict(gflag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


