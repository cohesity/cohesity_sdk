# GcpMySqlProtectionGroupObjectParams

Specifies the object parameters to create Google MySQL Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the database. | 
**name** | **str** | Specifies the name of the database. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_my_sql_protection_group_object_params import GcpMySqlProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMySqlProtectionGroupObjectParams from a JSON string
gcp_my_sql_protection_group_object_params_instance = GcpMySqlProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(GcpMySqlProtectionGroupObjectParams.to_json())

# convert the object into a dict
gcp_my_sql_protection_group_object_params_dict = gcp_my_sql_protection_group_object_params_instance.to_dict()
# create an instance of GcpMySqlProtectionGroupObjectParams from a dict
gcp_my_sql_protection_group_object_params_from_dict = GcpMySqlProtectionGroupObjectParams.from_dict(gcp_my_sql_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


