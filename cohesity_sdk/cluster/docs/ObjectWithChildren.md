# ObjectWithChildren

Specifies information of the object and its children objects.

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
**elastifile_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeObjectParams**](FlashbladeObjectParams.md) |  | [optional] 
**generic_nas_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**gpfs_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**group_params** | [**GroupObjectEntityParams**](GroupObjectEntityParams.md) |  | [optional] 
**isilon_params** | [**IsilonObjectParams**](IsilonObjectParams.md) |  | [optional] 
**mongo_db_params** | [**MongoDBObjectParams**](MongoDBObjectParams.md) |  | [optional] 
**mssql_params** | [**MssqlObjectEntityParams**](MssqlObjectEntityParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectParams**](NetappObjectParams.md) |  | [optional] 
**oracle_params** | [**OracleObjectEntityParams**](OracleObjectEntityParams.md) |  | [optional] 
**physical_params** | [**PhysicalObjectEntityParams**](PhysicalObjectEntityParams.md) |  | [optional] 
**sharepoint_params** | [**SharepointObjectEntityParams**](SharepointObjectEntityParams.md) |  | [optional] 
**uda_params** | [**UdaObjectParams**](UdaObjectParams.md) |  | [optional] 
**view_params** | [**ViewObjectParams**](ViewObjectParams.md) |  | [optional] 
**vmware_params** | [**VmwareObjectEntityParams**](VmwareObjectEntityParams.md) |  | [optional] 
**objects** | [**List[ObjectWithChildren]**](ObjectWithChildren.md) | Specifies a list of child nodes for this specific node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_with_children import ObjectWithChildren

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectWithChildren from a JSON string
object_with_children_instance = ObjectWithChildren.from_json(json)
# print the JSON string representation of the object
print(ObjectWithChildren.to_json())

# convert the object into a dict
object_with_children_dict = object_with_children_instance.to_dict()
# create an instance of ObjectWithChildren from a dict
object_with_children_from_dict = ObjectWithChildren.from_dict(object_with_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


