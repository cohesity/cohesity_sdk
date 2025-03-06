# OracleDataGuardInfo

Dataguard info about Oracle database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Specifies the role of the Oracle DataGuard database. | [optional] 
**standby_type** | **str** | Specifies the type of the standby oracle database. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.oracle_data_guard_info import OracleDataGuardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OracleDataGuardInfo from a JSON string
oracle_data_guard_info_instance = OracleDataGuardInfo.from_json(json)
# print the JSON string representation of the object
print(OracleDataGuardInfo.to_json())

# convert the object into a dict
oracle_data_guard_info_dict = oracle_data_guard_info_instance.to_dict()
# create an instance of OracleDataGuardInfo from a dict
oracle_data_guard_info_from_dict = OracleDataGuardInfo.from_dict(oracle_data_guard_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


