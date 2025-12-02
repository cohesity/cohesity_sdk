# FCICluster

Specifies the details of a Failover Cluster Instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Error**](Error.md) |  | [optional] 
**id** | **str** | Specifies the unique identifier of the FCI. | [optional] 
**is_selected_by_default** | **bool** | Indicates to the UI whether this FCI cluster should be selected by default | [optional] 
**name** | **str** | Specifies the name of the FCI. | [optional] 
**resource_info** | [**AppResource**](AppResource.md) |  | [optional] 
**servers** | [**List[SQLServer]**](SQLServer.md) | Specifies the list of SQL servers which belongs to the given FCI.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fci_cluster import FCICluster

# TODO update the JSON string below
json = "{}"
# create an instance of FCICluster from a JSON string
fci_cluster_instance = FCICluster.from_json(json)
# print the JSON string representation of the object
print(FCICluster.to_json())

# convert the object into a dict
fci_cluster_dict = fci_cluster_instance.to_dict()
# create an instance of FCICluster from a dict
fci_cluster_from_dict = FCICluster.from_dict(fci_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


