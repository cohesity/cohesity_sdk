# ViewClients

Specifies a list of View Clients.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**List[ViewClient]**](ViewClient.md) | Specifies the list of Clients. | [optional] 

## Example

```python
from cohesity_sdk.models.view_clients import ViewClients

# TODO update the JSON string below
json = "{}"
# create an instance of ViewClients from a JSON string
view_clients_instance = ViewClients.from_json(json)
# print the JSON string representation of the object
print(ViewClients.to_json())

# convert the object into a dict
view_clients_dict = view_clients_instance.to_dict()
# create an instance of ViewClients from a dict
view_clients_from_dict = ViewClients.from_dict(view_clients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


