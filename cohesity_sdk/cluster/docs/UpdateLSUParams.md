# UpdateLSUParams

Specifies the parameter to update an LSU.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the LSU name. | [optional] 
**nbu_domain** | **str** | Specifies the NBU Domain this LSU is associated with. | [optional] 
**worm_config** | [**WormConfig**](WormConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_lsu_params import UpdateLSUParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLSUParams from a JSON string
update_lsu_params_instance = UpdateLSUParams.from_json(json)
# print the JSON string representation of the object
print(UpdateLSUParams.to_json())

# convert the object into a dict
update_lsu_params_dict = update_lsu_params_instance.to_dict()
# create an instance of UpdateLSUParams from a dict
update_lsu_params_from_dict = UpdateLSUParams.from_dict(update_lsu_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


