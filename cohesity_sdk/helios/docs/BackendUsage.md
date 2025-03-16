# BackendUsage

Specifies the TiB usage statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_current_storage_account_usage_bytes** | **int** | The current azure storage account usage from the start of the month. | [optional] 
**current_s3_glacier_usage_bytes** | **int** | The current s3 glacier usage from the start of the month. | [optional] 
**current_s3_usage_bytes** | **int** | The current s3 usage from the start of the month. | [optional] 
**region_id** | **str** | The current region for which usage is calculated. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.backend_usage import BackendUsage

# TODO update the JSON string below
json = "{}"
# create an instance of BackendUsage from a JSON string
backend_usage_instance = BackendUsage.from_json(json)
# print the JSON string representation of the object
print(BackendUsage.to_json())

# convert the object into a dict
backend_usage_dict = backend_usage_instance.to_dict()
# create an instance of BackendUsage from a dict
backend_usage_from_dict = BackendUsage.from_dict(backend_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


