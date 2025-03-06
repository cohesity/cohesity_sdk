# MSSQLFileProtectionGroupHostParams

Specifies the host specific parameters for a host container in this protection group. Objects specified here should only be MSSQL root containers and will not be protected unless they are also specified in the 'objects' list. This list is just for specifying source level settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_source_side_deduplication** | **bool** | Specifies whether or not to disable source side deduplication on this source. The default behavior is false unless the user has set &#39;performSourceSideDeduplication&#39; to true. | [optional] 
**host_id** | **int** | Specifies the id of the host container on which databases are hosted. | 
**host_name** | **str** | Specifies the name of the host container on which databases are hosted. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.mssql_file_protection_group_host_params import MSSQLFileProtectionGroupHostParams

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLFileProtectionGroupHostParams from a JSON string
mssql_file_protection_group_host_params_instance = MSSQLFileProtectionGroupHostParams.from_json(json)
# print the JSON string representation of the object
print(MSSQLFileProtectionGroupHostParams.to_json())

# convert the object into a dict
mssql_file_protection_group_host_params_dict = mssql_file_protection_group_host_params_instance.to_dict()
# create an instance of MSSQLFileProtectionGroupHostParams from a dict
mssql_file_protection_group_host_params_from_dict = MSSQLFileProtectionGroupHostParams.from_dict(mssql_file_protection_group_host_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


