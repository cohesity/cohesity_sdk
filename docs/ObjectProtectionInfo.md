# ObjectProtectionInfo

Specifies the object info on cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id where this object belongs to. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id where this object belongs to. | [optional] 
**is_deleted** | **bool** | Specifies whether the object is deleted. Deleted objects can&#39;t be protected but can be recovered or unprotected. | [optional] 
**last_run_status** | **str** | Specifies the status of the object&#39;s last protection run. | [optional] 
**object_backup_configuration** | [**List[ProtectionSummary]**](ProtectionSummary.md) | Specifies a list of object protections. | [optional] 
**object_id** | **int** | Specifies the object id. | [optional] 
**protection_groups** | [**List[ObjectProtectionGroupSummary]**](ObjectProtectionGroupSummary.md) | Specifies a list of protection groups protecting this object. | [optional] 
**region_id** | **str** | Specifies the region id where this object belongs to. | [optional] 
**source_id** | **int** | Specifies the source id. | [optional] 
**tenant_ids** | **List[str]** | List of Tenants the object belongs to. | [optional] 
**view_id** | **int** | Specifies the view id for the object. | [optional] 

## Example

```python
from cohesity_sdk.models.object_protection_info import ObjectProtectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectProtectionInfo from a JSON string
object_protection_info_instance = ObjectProtectionInfo.from_json(json)
# print the JSON string representation of the object
print(ObjectProtectionInfo.to_json())

# convert the object into a dict
object_protection_info_dict = object_protection_info_instance.to_dict()
# create an instance of ObjectProtectionInfo from a dict
object_protection_info_from_dict = ObjectProtectionInfo.from_dict(object_protection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


