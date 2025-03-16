# SwiftParams

Specifies the parameters to update a Swift configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keystone_id** | **int** | Specifies the associated Keystone configuration Id. | [optional] 
**operator_roles** | **List[str]** | Specifies a list of roles that can operate on Cohesity Swift service. | [optional] 
**tenant_id** | **str** | Specifies the tenant Id who will use this Swift configuration. | 

## Example

```python
from cohesity_sdk.cluster.models.swift_params import SwiftParams

# TODO update the JSON string below
json = "{}"
# create an instance of SwiftParams from a JSON string
swift_params_instance = SwiftParams.from_json(json)
# print the JSON string representation of the object
print(SwiftParams.to_json())

# convert the object into a dict
swift_params_dict = swift_params_instance.to_dict()
# create an instance of SwiftParams from a dict
swift_params_from_dict = SwiftParams.from_dict(swift_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


