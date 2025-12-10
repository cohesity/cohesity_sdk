# ListAppServersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_info** | [**PaginationParams**](PaginationParams.md) |  | [optional] 
**app_servers** | [**List[AppServerInfo]**](AppServerInfo.md) | Specifies the list of structs for listing app VMs along with its auxiliary hierarchy e.g. SQL VMs along with instances. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.list_app_servers_response import ListAppServersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAppServersResponse from a JSON string
list_app_servers_response_instance = ListAppServersResponse.from_json(json)
# print the JSON string representation of the object
print(ListAppServersResponse.to_json())

# convert the object into a dict
list_app_servers_response_dict = list_app_servers_response_instance.to_dict()
# create an instance of ListAppServersResponse from a dict
list_app_servers_response_from_dict = ListAppServersResponse.from_dict(list_app_servers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


