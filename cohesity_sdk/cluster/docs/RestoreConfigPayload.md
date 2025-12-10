# RestoreConfigPayload

Specifies the config payload of restore config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_path** | [**ObjectPath**](ObjectPath.md) |  | [optional] 
**s3_config** | [**S3RestoreConfig**](S3RestoreConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.restore_config_payload import RestoreConfigPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreConfigPayload from a JSON string
restore_config_payload_instance = RestoreConfigPayload.from_json(json)
# print the JSON string representation of the object
print(RestoreConfigPayload.to_json())

# convert the object into a dict
restore_config_payload_dict = restore_config_payload_instance.to_dict()
# create an instance of RestoreConfigPayload from a dict
restore_config_payload_from_dict = RestoreConfigPayload.from_dict(restore_config_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


