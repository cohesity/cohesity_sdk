# ReplicationObjectsList

Specifies the Replication Objects Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_objects** | [**List[ReplicationObjectDetails]**](ReplicationObjectDetails.md) | Specifies a list of Replication Objects. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_objects_list import ReplicationObjectsList

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationObjectsList from a JSON string
replication_objects_list_instance = ReplicationObjectsList.from_json(json)
# print the JSON string representation of the object
print(ReplicationObjectsList.to_json())

# convert the object into a dict
replication_objects_list_dict = replication_objects_list_instance.to_dict()
# create an instance of ReplicationObjectsList from a dict
replication_objects_list_from_dict = ReplicationObjectsList.from_dict(replication_objects_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


