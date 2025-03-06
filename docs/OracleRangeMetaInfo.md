# OracleRangeMetaInfo

Specifies Range related information for an oracle db

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_of_range** | **int** | Specifies ending value of the range in time (usecs), SCN or sequence no. | [optional] 
**incarnation_id** | **int** | Specifies incarnation id associated with the oracle db for which the restore range belongs. Only applicable for ranges of type SCN and sequence no. | [optional] 
**protection_group_id** | **str** | Specifies id of the Protection Group corresponding to this oracle range | [optional] 
**reset_log_id** | **int** | Specifies resetlogs identifier associated with the oracle range. Only applicable for ranges of type SCN and sequence no. | [optional] 
**start_of_range** | **int** | Specifies starting value of the range in time (usecs), SCN or sequence no. | [optional] 
**thread_id** | **int** | Specifies thread id associated with the oracle db for which the restore range belongs. Only applicable for ranges of type sequence no. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.oracle_range_meta_info import OracleRangeMetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OracleRangeMetaInfo from a JSON string
oracle_range_meta_info_instance = OracleRangeMetaInfo.from_json(json)
# print the JSON string representation of the object
print(OracleRangeMetaInfo.to_json())

# convert the object into a dict
oracle_range_meta_info_dict = oracle_range_meta_info_instance.to_dict()
# create an instance of OracleRangeMetaInfo from a dict
oracle_range_meta_info_from_dict = OracleRangeMetaInfo.from_dict(oracle_range_meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


