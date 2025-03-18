# UdaParams

Specifies the recovery options specific to Universal Data Adapter environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_uda_params** | [**RecoverUdaParams**](RecoverUdaParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.uda_params import UdaParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaParams from a JSON string
uda_params_instance = UdaParams.from_json(json)
# print the JSON string representation of the object
print(UdaParams.to_json())

# convert the object into a dict
uda_params_dict = uda_params_instance.to_dict()
# create an instance of UdaParams from a dict
uda_params_from_dict = UdaParams.from_dict(uda_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


