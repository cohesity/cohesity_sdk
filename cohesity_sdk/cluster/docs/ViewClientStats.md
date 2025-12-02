# ViewClientStats

Specifies the View Client stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_ip** | **str** | Specifies the client IP. | [optional] 
**stats** | [**List[ClientStats]**](ClientStats.md) | Specifies the list of Client stats. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_client_stats import ViewClientStats

# TODO update the JSON string below
json = "{}"
# create an instance of ViewClientStats from a JSON string
view_client_stats_instance = ViewClientStats.from_json(json)
# print the JSON string representation of the object
print(ViewClientStats.to_json())

# convert the object into a dict
view_client_stats_dict = view_client_stats_instance.to_dict()
# create an instance of ViewClientStats from a dict
view_client_stats_from_dict = ViewClientStats.from_dict(view_client_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


