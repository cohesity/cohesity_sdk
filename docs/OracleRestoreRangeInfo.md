# OracleRestoreRangeInfo

Specifies Restore Ranges related to an Oracle Database

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scn_range_info** | [**List[OracleRangeMetaInfo]**](OracleRangeMetaInfo.md) | Specifies an array of SCN based oracle restore ranges. | [optional] 
**sequence_range_info** | [**List[OracleRangeMetaInfo]**](OracleRangeMetaInfo.md) | Specifies an array of time based oracle restore ranges. | [optional] 
**time_range_info** | [**List[OracleRangeMetaInfo]**](OracleRangeMetaInfo.md) | Specifies an array of time based oracle restore ranges. | [optional] 

## Example

```python
from cohesity_sdk.models.oracle_restore_range_info import OracleRestoreRangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OracleRestoreRangeInfo from a JSON string
oracle_restore_range_info_instance = OracleRestoreRangeInfo.from_json(json)
# print the JSON string representation of the object
print(OracleRestoreRangeInfo.to_json())

# convert the object into a dict
oracle_restore_range_info_dict = oracle_restore_range_info_instance.to_dict()
# create an instance of OracleRestoreRangeInfo from a dict
oracle_restore_range_info_from_dict = OracleRestoreRangeInfo.from_dict(oracle_restore_range_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


