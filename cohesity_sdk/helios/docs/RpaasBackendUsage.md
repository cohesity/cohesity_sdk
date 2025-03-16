# RpaasBackendUsage

Specifies the RPaaS usage statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_usecs** | **int** | Specifies the timestamp for the usage. | [optional] 
**usage_bytes** | **int** | The usage for the timestamp. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rpaas_backend_usage import RpaasBackendUsage

# TODO update the JSON string below
json = "{}"
# create an instance of RpaasBackendUsage from a JSON string
rpaas_backend_usage_instance = RpaasBackendUsage.from_json(json)
# print the JSON string representation of the object
print(RpaasBackendUsage.to_json())

# convert the object into a dict
rpaas_backend_usage_dict = rpaas_backend_usage_instance.to_dict()
# create an instance of RpaasBackendUsage from a dict
rpaas_backend_usage_from_dict = RpaasBackendUsage.from_dict(rpaas_backend_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


