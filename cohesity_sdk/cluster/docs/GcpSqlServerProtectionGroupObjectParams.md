# GcpSqlServerProtectionGroupObjectParams

Specifies the object parameters to create Google SQL Server Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the database. | 
**name** | **str** | Specifies the name of the database. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_sql_server_protection_group_object_params import GcpSqlServerProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSqlServerProtectionGroupObjectParams from a JSON string
gcp_sql_server_protection_group_object_params_instance = GcpSqlServerProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(GcpSqlServerProtectionGroupObjectParams.to_json())

# convert the object into a dict
gcp_sql_server_protection_group_object_params_dict = gcp_sql_server_protection_group_object_params_instance.to_dict()
# create an instance of GcpSqlServerProtectionGroupObjectParams from a dict
gcp_sql_server_protection_group_object_params_from_dict = GcpSqlServerProtectionGroupObjectParams.from_dict(gcp_sql_server_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


