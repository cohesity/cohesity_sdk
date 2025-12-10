# ClusterOperationTypeAndId

Operation type and id of the cluster operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** | Operation Id of cluster operation.  | 
**operation_type** | **str** | Operation type of cluster operation created for the request.  | 

## Example

```python
from cohesity_sdk.cluster.models.cluster_operation_type_and_id import ClusterOperationTypeAndId

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperationTypeAndId from a JSON string
cluster_operation_type_and_id_instance = ClusterOperationTypeAndId.from_json(json)
# print the JSON string representation of the object
print(ClusterOperationTypeAndId.to_json())

# convert the object into a dict
cluster_operation_type_and_id_dict = cluster_operation_type_and_id_instance.to_dict()
# create an instance of ClusterOperationTypeAndId from a dict
cluster_operation_type_and_id_from_dict = ClusterOperationTypeAndId.from_dict(cluster_operation_type_and_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


