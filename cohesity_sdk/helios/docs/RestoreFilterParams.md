# RestoreFilterParams

Specifies the additional filtering params for recoveries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_types** | **List[str]** | Specifies the recovery types to filter recoveries. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.restore_filter_params import RestoreFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreFilterParams from a JSON string
restore_filter_params_instance = RestoreFilterParams.from_json(json)
# print the JSON string representation of the object
print(RestoreFilterParams.to_json())

# convert the object into a dict
restore_filter_params_dict = restore_filter_params_instance.to_dict()
# create an instance of RestoreFilterParams from a dict
restore_filter_params_from_dict = RestoreFilterParams.from_dict(restore_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


