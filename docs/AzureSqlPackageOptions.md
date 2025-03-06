# AzureSqlPackageOptions

Specifies the SQL package parameters which are specific to Azure related Object Protection & Recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression** | **str** | Specifies the compression option supported by SQL package export command during Azure SQL backup. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_sql_package_options import AzureSqlPackageOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlPackageOptions from a JSON string
azure_sql_package_options_instance = AzureSqlPackageOptions.from_json(json)
# print the JSON string representation of the object
print(AzureSqlPackageOptions.to_json())

# convert the object into a dict
azure_sql_package_options_dict = azure_sql_package_options_instance.to_dict()
# create an instance of AzureSqlPackageOptions from a dict
azure_sql_package_options_from_dict = AzureSqlPackageOptions.from_dict(azure_sql_package_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


