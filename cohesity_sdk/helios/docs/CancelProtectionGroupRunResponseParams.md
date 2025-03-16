# CancelProtectionGroupRunResponseParams

Specifies the response of a cancel action on protection runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Specifies a unique run id of the Protection Group run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cancel_protection_group_run_response_params import CancelProtectionGroupRunResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CancelProtectionGroupRunResponseParams from a JSON string
cancel_protection_group_run_response_params_instance = CancelProtectionGroupRunResponseParams.from_json(json)
# print the JSON string representation of the object
print(CancelProtectionGroupRunResponseParams.to_json())

# convert the object into a dict
cancel_protection_group_run_response_params_dict = cancel_protection_group_run_response_params_instance.to_dict()
# create an instance of CancelProtectionGroupRunResponseParams from a dict
cancel_protection_group_run_response_params_from_dict = CancelProtectionGroupRunResponseParams.from_dict(cancel_protection_group_run_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


