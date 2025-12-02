# AppServerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_entity** | [**Object**](Object.md) |  | [optional] 
**root_entity** | [**Object**](Object.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.app_server_info import AppServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppServerInfo from a JSON string
app_server_info_instance = AppServerInfo.from_json(json)
# print the JSON string representation of the object
print(AppServerInfo.to_json())

# convert the object into a dict
app_server_info_dict = app_server_info_instance.to_dict()
# create an instance of AppServerInfo from a dict
app_server_info_from_dict = AppServerInfo.from_dict(app_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


