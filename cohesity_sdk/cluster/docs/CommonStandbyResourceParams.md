# CommonStandbyResourceParams

Specifies the params for standby resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_point_objective_secs** | **int** | Specifies the recovery point objective time user expects for this standby resource. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_standby_resource_params import CommonStandbyResourceParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonStandbyResourceParams from a JSON string
common_standby_resource_params_instance = CommonStandbyResourceParams.from_json(json)
# print the JSON string representation of the object
print(CommonStandbyResourceParams.to_json())

# convert the object into a dict
common_standby_resource_params_dict = common_standby_resource_params_instance.to_dict()
# create an instance of CommonStandbyResourceParams from a dict
common_standby_resource_params_from_dict = CommonStandbyResourceParams.from_dict(common_standby_resource_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


