# OracleObjectProtectionRequestParams

Specifies the request parameters specific to Oracle object protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_auto_kill_timeout_secs** | **int** | Time in seconds after which the full backup of the database in given backup job should be auto-killed. | [optional] 
**incr_auto_kill_timeout_secs** | **int** | Time in seconds after which the incremental backup of the database in given backup job should be auto-killed. | [optional] 
**log_auto_kill_timeout_secs** | **int** | Time in seconds after which the log backup of the database in given backup job should be auto-killed. | [optional] 
**objects** | [**List[OracleObjectProtectionInfo]**](OracleObjectProtectionInfo.md) | Specifies the list of object ids to be protected. | 
**persist_mountpoints** | **bool** | Specifies whether the mountpoints created while backing up Oracle DBs should be persisted.Defaults to true if value is null to handle the backward compatibility for the upgrade case. | [optional] [default to True]
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.oracle_object_protection_request_params import OracleObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleObjectProtectionRequestParams from a JSON string
oracle_object_protection_request_params_instance = OracleObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(OracleObjectProtectionRequestParams.to_json())

# convert the object into a dict
oracle_object_protection_request_params_dict = oracle_object_protection_request_params_instance.to_dict()
# create an instance of OracleObjectProtectionRequestParams from a dict
oracle_object_protection_request_params_from_dict = OracleObjectProtectionRequestParams.from_dict(oracle_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


