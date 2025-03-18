# ProtectedObjectInfo

Specifies the details of a protected object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str** | Specifies the environment of the object. | [optional] 
**id** | **int** | Specifies object id. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**source_id** | **int** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str** | Specifies registered source name to which object belongs. | [optional] 
**child_objects** | [**List[ObjectSummary]**](ObjectSummary.md) | Specifies child object details. | [optional] 
**global_id** | **str** | Specifies the global id which is a unique identifier of the object. | [optional] 
**logical_size_bytes** | **int** | Specifies the logical size of object in bytes. | [optional] 
**object_hash** | **str** | Specifies the hash identifier of the object. | [optional] 
**object_type** | **str** | Specifies the type of the object. | [optional] 
**os_type** | **str** | Specifies the operating system type of the object. | [optional] 
**protection_type** | **str** | Specifies the protection type of the object if any. | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**uuid** | **str** | Specifies the uuid which is a unique identifier of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**windows_cluster_summary** | [**ObjectTypeWindowsClusterParams**](ObjectTypeWindowsClusterParams.md) |  | [optional] 
**last_run** | [**ObjectProtectionRunSummary**](ObjectProtectionRunSummary.md) |  | [optional] 
**object_backup_configuration** | [**ProtectedObjectBackupConfig**](ProtectedObjectBackupConfig.md) |  | [optional] 
**permissions** | [**List[TenantInfo]**](TenantInfo.md) | Specifies the list of tenants that have permissions for this accessing given protected object. | [optional] 
**protection_group_configurations** | [**List[ProtectedObjectGroupBackupConfig]**](ProtectedObjectGroupBackupConfig.md) | Specifies the protection info associated with every object. There can be multiple instances of protection info since the same object can be protected in multiple protection groups. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protected_object_info import ProtectedObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectInfo from a JSON string
protected_object_info_instance = ProtectedObjectInfo.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectInfo.to_json())

# convert the object into a dict
protected_object_info_dict = protected_object_info_instance.to_dict()
# create an instance of ProtectedObjectInfo from a dict
protected_object_info_from_dict = ProtectedObjectInfo.from_dict(protected_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


