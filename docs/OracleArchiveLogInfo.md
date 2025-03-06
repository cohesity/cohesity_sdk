# OracleArchiveLogInfo

Specifies information related to archive log restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_log_restore_dest** | **str** | Specifies destination where archive logs are to be restored. | [optional] 
**range_info_vec** | [**List[OracleRangeMetaInfo]**](OracleRangeMetaInfo.md) | Specifies an array of oracle restore ranges. | [optional] 
**range_type** | **str** | Specifies the type of range. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.oracle_archive_log_info import OracleArchiveLogInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OracleArchiveLogInfo from a JSON string
oracle_archive_log_info_instance = OracleArchiveLogInfo.from_json(json)
# print the JSON string representation of the object
print(OracleArchiveLogInfo.to_json())

# convert the object into a dict
oracle_archive_log_info_dict = oracle_archive_log_info_instance.to_dict()
# create an instance of OracleArchiveLogInfo from a dict
oracle_archive_log_info_from_dict = OracleArchiveLogInfo.from_dict(oracle_archive_log_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


