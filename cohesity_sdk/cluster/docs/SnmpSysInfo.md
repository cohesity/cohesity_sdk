# SnmpSysInfo

SNMP System Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | Contact is the system contact. | [optional] 
**description** | **str** | Description is the system description. | [optional] 
**engine_id_type** | **int** | EngineIdType is the system egineId typeß. | [optional] 
**location** | **str** | Location is the system location. | [optional] 
**name** | **str** | Name is the system name. | [optional] 
**object_id** | **str** | Object id is the system object id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.snmp_sys_info import SnmpSysInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpSysInfo from a JSON string
snmp_sys_info_instance = SnmpSysInfo.from_json(json)
# print the JSON string representation of the object
print(SnmpSysInfo.to_json())

# convert the object into a dict
snmp_sys_info_dict = snmp_sys_info_instance.to_dict()
# create an instance of SnmpSysInfo from a dict
snmp_sys_info_from_dict = SnmpSysInfo.from_dict(snmp_sys_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


