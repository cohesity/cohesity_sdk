# ResourceInfo

This object represents information about a resource type present in the kubernetes cluster as well as a list containing the instances of that resource type present/selected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | API group name of the resource (excluding the version). (Eg. apps, kubevirt.io). | [optional] 
**is_cluster_scoped** | **bool** | Boolean indicating whether the resource is cluster scoped or not. This field is ignored for resource selection during recovery. | [optional] 
**kind** | **str** | The kind of the resource type. (Eg. VirtualMachine) | [optional] 
**name** | **str** | The name of the resource. This field is ignored for resource selection during recovery. | [optional] 
**resource_list** | [**List[ResourceInstance]**](ResourceInstance.md) | Array of the instances of the resource with group, version and kind mentioned above. | [optional] 
**version** | **str** | The version under the API group for the resource. This field is ignored for resource selection during recovery. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.resource_info import ResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceInfo from a JSON string
resource_info_instance = ResourceInfo.from_json(json)
# print the JSON string representation of the object
print(ResourceInfo.to_json())

# convert the object into a dict
resource_info_dict = resource_info_instance.to_dict()
# create an instance of ResourceInfo from a dict
resource_info_from_dict = ResourceInfo.from_dict(resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


