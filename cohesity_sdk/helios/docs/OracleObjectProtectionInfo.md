# OracleObjectProtectionInfo

Specifies the object identifier for Object based Oracle Protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_params** | [**List[OracleProtectionGroupDbParams]**](OracleProtectionGroupDbParams.md) | Specifies the properties of the Oracle databases. | [optional] 
**object_id** | **int** | Specifies the id of the host on which databases are hosted | 

## Example

```python
from cohesity_sdk.helios.models.oracle_object_protection_info import OracleObjectProtectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OracleObjectProtectionInfo from a JSON string
oracle_object_protection_info_instance = OracleObjectProtectionInfo.from_json(json)
# print the JSON string representation of the object
print(OracleObjectProtectionInfo.to_json())

# convert the object into a dict
oracle_object_protection_info_dict = oracle_object_protection_info_instance.to_dict()
# create an instance of OracleObjectProtectionInfo from a dict
oracle_object_protection_info_from_dict = OracleObjectProtectionInfo.from_dict(oracle_object_protection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


