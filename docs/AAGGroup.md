# AAGGroup

Specifies the details of a AAG Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fci_clusters** | [**List[FCICluster]**](FCICluster.md) | Specifies the list of FCI clusters which belongs to the given AAG Group. | [optional] 
**id** | **str** | Specifies the unique identifier of the AGGGroup. | [optional] 
**name** | **str** | Specifies the name of the AAG Group. | [optional] 
**resource_info** | [**AppResource**](AppResource.md) |  | [optional] 
**servers** | [**List[SQLServer]**](SQLServer.md) | Specifies the list of SQL servers which belongs to the given AAG Group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aag_group import AAGGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AAGGroup from a JSON string
aag_group_instance = AAGGroup.from_json(json)
# print the JSON string representation of the object
print(AAGGroup.to_json())

# convert the object into a dict
aag_group_dict = aag_group_instance.to_dict()
# create an instance of AAGGroup from a dict
aag_group_from_dict = AAGGroup.from_dict(aag_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


