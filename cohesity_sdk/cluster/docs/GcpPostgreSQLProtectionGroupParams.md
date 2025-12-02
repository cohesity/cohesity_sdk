# GcpPostgreSQLProtectionGroupParams

Specifies the parameters which are specific to Google PostgreSQL related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_postgresql_tag_ids** | **List[List[int]]** | Array of arrays of PostgreSQL Tag Ids that specify db instances to Exclude. | [optional] 
**objects** | [**List[GcpDatabaseProtectionGroupObjectParams]**](GcpDatabaseProtectionGroupObjectParams.md) | Specifies the PostgreSQL databases to be included in the Protection Group. | [optional] 
**postgresql_tag_ids** | **List[List[int]]** | Array of arrays of PostgreSQL Tag Ids that specify db instances to Protect. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_postgre_sql_protection_group_params import GcpPostgreSQLProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPostgreSQLProtectionGroupParams from a JSON string
gcp_postgre_sql_protection_group_params_instance = GcpPostgreSQLProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(GcpPostgreSQLProtectionGroupParams.to_json())

# convert the object into a dict
gcp_postgre_sql_protection_group_params_dict = gcp_postgre_sql_protection_group_params_instance.to_dict()
# create an instance of GcpPostgreSQLProtectionGroupParams from a dict
gcp_postgre_sql_protection_group_params_from_dict = GcpPostgreSQLProtectionGroupParams.from_dict(gcp_postgre_sql_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


