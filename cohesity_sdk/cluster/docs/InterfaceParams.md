# InterfaceParams

Parameters of an interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the interface. | 
**network_params** | [**InterfaceNetworkParams**](InterfaceNetworkParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.interface_params import InterfaceParams

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceParams from a JSON string
interface_params_instance = InterfaceParams.from_json(json)
# print the JSON string representation of the object
print(InterfaceParams.to_json())

# convert the object into a dict
interface_params_dict = interface_params_instance.to_dict()
# create an instance of InterfaceParams from a dict
interface_params_from_dict = InterfaceParams.from_dict(interface_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


