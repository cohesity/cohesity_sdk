# CancellationTimeoutParams

Specifies timeouts for different backup types (kFull, kRegular etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_type** | **str** | The scheduled backup type(kFull, kRegular etc.) | [optional] 
**timeout_mins** | **int** | Specifies the timeout in mins | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cancellation_timeout_params import CancellationTimeoutParams

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationTimeoutParams from a JSON string
cancellation_timeout_params_instance = CancellationTimeoutParams.from_json(json)
# print the JSON string representation of the object
print(CancellationTimeoutParams.to_json())

# convert the object into a dict
cancellation_timeout_params_dict = cancellation_timeout_params_instance.to_dict()
# create an instance of CancellationTimeoutParams from a dict
cancellation_timeout_params_from_dict = CancellationTimeoutParams.from_dict(cancellation_timeout_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


