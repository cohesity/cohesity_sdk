# ResourceInfo

This object represents information about a resource type present in the kubernetes cluster as well as a list containing the instances of that resource type present/selected.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str, none_type** | API group name of the resource (excluding the version). (Eg. apps, kubevirt.io). | [optional] 
**is_cluster_scoped** | **bool, none_type** | Boolean indicating whether the resource is cluster scoped or not. This field is ignored for resource selection during recovery. | [optional] 
**kind** | **str, none_type** | The kind of the resource type. (Eg. VirtualMachine) | [optional] 
**name** | **str, none_type** | The name of the resource. This field is ignored for resource selection during recovery. | [optional] 
**resource_list** | [**[ResourceInstance], none_type**](ResourceInstance.md) | Array of the instances of the resource with group, version and kind mentioned above. | [optional] 
**version** | **str, none_type** | The version under the API group for the resource. This field is ignored for resource selection during recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


