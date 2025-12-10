# ViewTargetParamsForRecoverPhysical

Specifies the recovery target configuration if physical snapshots are being recovered as a Cohesity view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos_policy** | [**NasQosPolicy**](NasQosPolicy.md) |  | [optional] 
**view_name** | **str** | Specifies the name of the view. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_target_params_for_recover_physical import ViewTargetParamsForRecoverPhysical

# TODO update the JSON string below
json = "{}"
# create an instance of ViewTargetParamsForRecoverPhysical from a JSON string
view_target_params_for_recover_physical_instance = ViewTargetParamsForRecoverPhysical.from_json(json)
# print the JSON string representation of the object
print(ViewTargetParamsForRecoverPhysical.to_json())

# convert the object into a dict
view_target_params_for_recover_physical_dict = view_target_params_for_recover_physical_instance.to_dict()
# create an instance of ViewTargetParamsForRecoverPhysical from a dict
view_target_params_for_recover_physical_from_dict = ViewTargetParamsForRecoverPhysical.from_dict(view_target_params_for_recover_physical_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


