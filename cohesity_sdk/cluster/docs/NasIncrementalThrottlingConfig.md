# NasIncrementalThrottlingConfig

Specifies the throttling configuration during incremental backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_metadata_fetch_percentage** | **int** | Specifies the percentage value of maximum concurrent metadata to be fetched during incremental backup of the source. | [optional] 
**max_read_write_percentage** | **int** | Specifies the percentage value of maximum concurrent read/write during incremental backup of the source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.nas_incremental_throttling_config import NasIncrementalThrottlingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NasIncrementalThrottlingConfig from a JSON string
nas_incremental_throttling_config_instance = NasIncrementalThrottlingConfig.from_json(json)
# print the JSON string representation of the object
print(NasIncrementalThrottlingConfig.to_json())

# convert the object into a dict
nas_incremental_throttling_config_dict = nas_incremental_throttling_config_instance.to_dict()
# create an instance of NasIncrementalThrottlingConfig from a dict
nas_incremental_throttling_config_from_dict = NasIncrementalThrottlingConfig.from_dict(nas_incremental_throttling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


