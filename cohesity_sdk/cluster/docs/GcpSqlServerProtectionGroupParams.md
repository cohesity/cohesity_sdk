# GcpSqlServerProtectionGroupParams

Specifies the parameters which are specific to Google SQL Server related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool** | This flag controls whether SQL backup auto-creates bucket or uses the provided bucket name. | [optional] 
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for Cloud SQL backup. | 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[GcpSqlServerProtectionGroupObjectParams]**](GcpSqlServerProtectionGroupObjectParams.md) | Specifies the SQL Server databases to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_sql_server_protection_group_params import GcpSqlServerProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSqlServerProtectionGroupParams from a JSON string
gcp_sql_server_protection_group_params_instance = GcpSqlServerProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(GcpSqlServerProtectionGroupParams.to_json())

# convert the object into a dict
gcp_sql_server_protection_group_params_dict = gcp_sql_server_protection_group_params_instance.to_dict()
# create an instance of GcpSqlServerProtectionGroupParams from a dict
gcp_sql_server_protection_group_params_from_dict = GcpSqlServerProtectionGroupParams.from_dict(gcp_sql_server_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


