# SecurityConfigMetaData

Specifies the meta data related to security config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_management_enabled** | **bool** | Specifies whether session management is enabled.  When true, sessionConfiguration from SecurityConfig will be used for for managing user sessions. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.security_config_meta_data import SecurityConfigMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigMetaData from a JSON string
security_config_meta_data_instance = SecurityConfigMetaData.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigMetaData.to_json())

# convert the object into a dict
security_config_meta_data_dict = security_config_meta_data_instance.to_dict()
# create an instance of SecurityConfigMetaData from a dict
security_config_meta_data_from_dict = SecurityConfigMetaData.from_dict(security_config_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


