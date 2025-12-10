# UpdateGflagParameters

Specifies the parameters for updating service gflags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_now** | **bool** | Specifies whether to apply the change immediately. If set to true, the gflag change will work without restarting the service. | [optional] 
**reason** | **str** | Specifies the reason for clearing gflags. | [optional] 
**service_flags** | [**ServiceGflags**](ServiceGflags.md) |  | [optional] 
**skip_existence_check** | **bool** | Skips the KUndefinedFlagPrefix validation check and allows the user to set undefined gflags, effective after service restart/upgrade | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_gflag_parameters import UpdateGflagParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGflagParameters from a JSON string
update_gflag_parameters_instance = UpdateGflagParameters.from_json(json)
# print the JSON string representation of the object
print(UpdateGflagParameters.to_json())

# convert the object into a dict
update_gflag_parameters_dict = update_gflag_parameters_instance.to_dict()
# create an instance of UpdateGflagParameters from a dict
update_gflag_parameters_from_dict = UpdateGflagParameters.from_dict(update_gflag_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


