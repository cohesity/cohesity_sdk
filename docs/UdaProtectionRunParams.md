# UdaProtectionRunParams

Specifies the parameters for Universal Data Adapter protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externally_triggered_run_params** | [**UdaExternallyTriggeredRunParams**](UdaExternallyTriggeredRunParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.uda_protection_run_params import UdaProtectionRunParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaProtectionRunParams from a JSON string
uda_protection_run_params_instance = UdaProtectionRunParams.from_json(json)
# print the JSON string representation of the object
print(UdaProtectionRunParams.to_json())

# convert the object into a dict
uda_protection_run_params_dict = uda_protection_run_params_instance.to_dict()
# create an instance of UdaProtectionRunParams from a dict
uda_protection_run_params_from_dict = UdaProtectionRunParams.from_dict(uda_protection_run_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


