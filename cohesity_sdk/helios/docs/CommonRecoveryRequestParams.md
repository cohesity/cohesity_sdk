# CommonRecoveryRequestParams

Specifies the common request parameters to create a Recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the Recovery. | 
**snapshot_environment** | **str** | Specifies the type of environment of snapshots for which the Recovery has to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.common_recovery_request_params import CommonRecoveryRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonRecoveryRequestParams from a JSON string
common_recovery_request_params_instance = CommonRecoveryRequestParams.from_json(json)
# print the JSON string representation of the object
print(CommonRecoveryRequestParams.to_json())

# convert the object into a dict
common_recovery_request_params_dict = common_recovery_request_params_instance.to_dict()
# create an instance of CommonRecoveryRequestParams from a dict
common_recovery_request_params_from_dict = CommonRecoveryRequestParams.from_dict(common_recovery_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


