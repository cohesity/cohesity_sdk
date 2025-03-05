# UdaExternallyTriggeredRunParams

Specifies the parameters for an externally triggered run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_args** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies a map of custom arguments to be supplied to the plugin. | [optional] 
**control_node** | **str** | Specifies the IP or FQDN of the source host where this backup will run. | [optional] 

## Example

```python
from cohesity_sdk.models.uda_externally_triggered_run_params import UdaExternallyTriggeredRunParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaExternallyTriggeredRunParams from a JSON string
uda_externally_triggered_run_params_instance = UdaExternallyTriggeredRunParams.from_json(json)
# print the JSON string representation of the object
print(UdaExternallyTriggeredRunParams.to_json())

# convert the object into a dict
uda_externally_triggered_run_params_dict = uda_externally_triggered_run_params_instance.to_dict()
# create an instance of UdaExternallyTriggeredRunParams from a dict
uda_externally_triggered_run_params_from_dict = UdaExternallyTriggeredRunParams.from_dict(uda_externally_triggered_run_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


