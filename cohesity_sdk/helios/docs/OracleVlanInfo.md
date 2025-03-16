# OracleVlanInfo

Specifies details about capturing Cohesity cluster VLAN info for Oracle workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | Specifies the gateway of this VLAN. | [optional] 
**id** | **int** | Specifies the Id of this VLAN. | [optional] 
**ip_list** | **List[str]** | Specifies the list of Ips in this VLAN. | [optional] 
**subnet_ip** | **str** | Specifies the subnet Ip for this VLAN. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.oracle_vlan_info import OracleVlanInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OracleVlanInfo from a JSON string
oracle_vlan_info_instance = OracleVlanInfo.from_json(json)
# print the JSON string representation of the object
print(OracleVlanInfo.to_json())

# convert the object into a dict
oracle_vlan_info_dict = oracle_vlan_info_instance.to_dict()
# create an instance of OracleVlanInfo from a dict
oracle_vlan_info_from_dict = OracleVlanInfo.from_dict(oracle_vlan_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


