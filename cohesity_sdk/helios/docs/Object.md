# Object

Specifies information about an object.

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
**permissions** | [**PermissionInfo**](PermissionInfo.md) |  | [optional] 
**protection_stats** | [**List[ObjectProtectionStatsSummary]**](ObjectProtectionStatsSummary.md) | Specifies the count and size of protected and unprotected objects for the size. | [optional] 
**elastifile_params** | **object** | Specifies the parameters for Elastifile object. | [optional] 
**flashblade_params** | **object** | Specifies the parameters for Flashblade object. | [optional] 
**generic_nas_params** | **object** | Specifies the parameters for GenericNas object. | [optional] 
**gpfs_params** | **object** | Specifies the parameters for GPFS object. | [optional] 
**group_params** | **object** | Specifies the parameters for M365 Group object. | [optional] 
**isilon_params** | **object** | Specifies the parameters for Isilon object. | [optional] 
**mongo_db_params** | **object** | Specifies the parameters for MongoDB object. | [optional] 
**mssql_params** | **object** | Specifies the parameters for Msssql object. | [optional] 
**netapp_params** | **object** | Specifies the parameters for NetApp object. | [optional] 
**oracle_params** | **object** | Specifies the parameters for Oracle object. | [optional] 
**physical_params** | **object** | Specifies the parameters for Physical object. | [optional] 
**sharepoint_params** | **object** | Specifies the parameters for Sharepoint object. | [optional] 
**uda_params** | **object** | Specifies the parameters for UDA object. | [optional] 
**view_params** | **object** | Specifies the parameters for a View. | [optional] 
**vmware_params** | [**VmwareObjectEntityParams**](VmwareObjectEntityParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object import Object

# TODO update the JSON string below
json = "{}"
# create an instance of Object from a JSON string
object_instance = Object.from_json(json)
# print the JSON string representation of the object
print(Object.to_json())

# convert the object into a dict
object_dict = object_instance.to_dict()
# create an instance of Object from a dict
object_from_dict = Object.from_dict(object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


