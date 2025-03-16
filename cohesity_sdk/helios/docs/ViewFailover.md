# ViewFailover

Specifies the failover status of a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_failover_ready** | **bool** | Specifies if the view is ready for failover. | [optional] 
**remote_cluster_id** | **int** | Specifies the remote cluster id. | [optional] 
**remote_cluster_incarnation_id** | **int** | Specifies the remote cluster incarnation id. | [optional] 
**remote_view_id** | **int** | Specifies the remote view id. | [optional] 
**view_uid** | **str** | View uid. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_failover import ViewFailover

# TODO update the JSON string below
json = "{}"
# create an instance of ViewFailover from a JSON string
view_failover_instance = ViewFailover.from_json(json)
# print the JSON string representation of the object
print(ViewFailover.to_json())

# convert the object into a dict
view_failover_dict = view_failover_instance.to_dict()
# create an instance of ViewFailover from a dict
view_failover_from_dict = ViewFailover.from_dict(view_failover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


