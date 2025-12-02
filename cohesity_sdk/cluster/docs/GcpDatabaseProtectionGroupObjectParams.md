# GcpDatabaseProtectionGroupObjectParams

Specifies the object parameters to create GCP database Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the database. | 
**name** | **str** | Specifies the name of the database. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_database_protection_group_object_params import GcpDatabaseProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpDatabaseProtectionGroupObjectParams from a JSON string
gcp_database_protection_group_object_params_instance = GcpDatabaseProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(GcpDatabaseProtectionGroupObjectParams.to_json())

# convert the object into a dict
gcp_database_protection_group_object_params_dict = gcp_database_protection_group_object_params_instance.to_dict()
# create an instance of GcpDatabaseProtectionGroupObjectParams from a dict
gcp_database_protection_group_object_params_from_dict = GcpDatabaseProtectionGroupObjectParams.from_dict(gcp_database_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


