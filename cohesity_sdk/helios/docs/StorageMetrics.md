# StorageMetrics

Metrics related to storage collected during the backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression_ratio** | **float** | Specifies the compression ratio (entropy) of data in this run. | [optional] 
**data_read_bytes** | **int** | Specifies the bytes of data read for this run. | [optional] 
**data_written_bytes** | **int** | Specifies the bytes of data written for this run. | [optional] 
**unmorphed_usage_bytes** | **int** | Specifies the bytes of data deduped for this run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.storage_metrics import StorageMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of StorageMetrics from a JSON string
storage_metrics_instance = StorageMetrics.from_json(json)
# print the JSON string representation of the object
print(StorageMetrics.to_json())

# convert the object into a dict
storage_metrics_dict = storage_metrics_instance.to_dict()
# create an instance of StorageMetrics from a dict
storage_metrics_from_dict = StorageMetrics.from_dict(storage_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


