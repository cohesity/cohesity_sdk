# RestoreConfig

Specifies the restore config of the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**RestoreConfigPayload**](RestoreConfigPayload.md) |  | [optional] 
**last_updated_timestamp_sec** | **int** | Specifies the timestamp fo the last update made to this config. | [optional] 
**service_name** | **str** | Specifies the service name of the restore config. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.restore_config import RestoreConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreConfig from a JSON string
restore_config_instance = RestoreConfig.from_json(json)
# print the JSON string representation of the object
print(RestoreConfig.to_json())

# convert the object into a dict
restore_config_dict = restore_config_instance.to_dict()
# create an instance of RestoreConfig from a dict
restore_config_from_dict = RestoreConfig.from_dict(restore_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


