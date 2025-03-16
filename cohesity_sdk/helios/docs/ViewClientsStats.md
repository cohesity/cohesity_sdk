# ViewClientsStats

Specifies a list of View Client stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_clients_stats** | [**List[ViewClientStats]**](ViewClientStats.md) | Specifies the list of View Client stats. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_clients_stats import ViewClientsStats

# TODO update the JSON string below
json = "{}"
# create an instance of ViewClientsStats from a JSON string
view_clients_stats_instance = ViewClientsStats.from_json(json)
# print the JSON string representation of the object
print(ViewClientsStats.to_json())

# convert the object into a dict
view_clients_stats_dict = view_clients_stats_instance.to_dict()
# create an instance of ViewClientsStats from a dict
view_clients_stats_from_dict = ViewClientsStats.from_dict(view_clients_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


