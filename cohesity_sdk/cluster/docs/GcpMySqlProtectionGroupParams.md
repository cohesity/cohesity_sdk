# GcpMySqlProtectionGroupParams

Specifies the parameters which are specific to Google MySQL related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_mysql_tag_ids** | **List[List[int]]** | Array of arrays of MySQL Tag Ids that specify db instances to Exclude. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**mysql_tag_ids** | **List[List[int]]** | Array of arrays of MySQL Tag Ids that specify db instances to Protect. | [optional] 
**objects** | [**List[GcpMySqlProtectionGroupObjectParams]**](GcpMySqlProtectionGroupObjectParams.md) | Specifies the MySQL databases to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_my_sql_protection_group_params import GcpMySqlProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMySqlProtectionGroupParams from a JSON string
gcp_my_sql_protection_group_params_instance = GcpMySqlProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(GcpMySqlProtectionGroupParams.to_json())

# convert the object into a dict
gcp_my_sql_protection_group_params_dict = gcp_my_sql_protection_group_params_instance.to_dict()
# create an instance of GcpMySqlProtectionGroupParams from a dict
gcp_my_sql_protection_group_params_from_dict = GcpMySqlProtectionGroupParams.from_dict(gcp_my_sql_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


