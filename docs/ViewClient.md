# ViewClient

Specifies a View Client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_time_usecs** | **int** | Specifies the time how long the client has connected to the server. | [optional] 
**gid** | **int** | Specifies the GID of the client user. | [optional] 
**ip** | **str** | Specifies the client ip. | [optional] 
**node_ip** | **str** | Specifies the node ip which the client is connected to. | [optional] 
**protocol** | **str** | Specifies the protocol the client uses. | [optional] 
**server_ip** | **str** | Specifies the server ip which the client is connected to. | [optional] 
**smb_dialect_version** | **int** | Specifies the dialect version for SMB client. | [optional] 
**uid** | **int** | Specifies the UID of the client user. | [optional] 
**user_domain** | **str** | Specifies the user domain of the client. | [optional] 
**username** | **str** | Specifies the username of the client. | [optional] 
**view_id** | **int** | Specifies the id of the View which the client is connected to. | [optional] 
**view_name** | **str** | Specifies the name of the View which the client is connected to. | [optional] 
**view_path** | **str** | Specifies the path of the View which the client is connected to. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_client import ViewClient

# TODO update the JSON string below
json = "{}"
# create an instance of ViewClient from a JSON string
view_client_instance = ViewClient.from_json(json)
# print the JSON string representation of the object
print(ViewClient.to_json())

# convert the object into a dict
view_client_dict = view_client_instance.to_dict()
# create an instance of ViewClient from a dict
view_client_from_dict = ViewClient.from_dict(view_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


