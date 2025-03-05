# OracleSbtHostParams

Specifies details about capturing Oracle SBT host info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sbt_library_path** | **str** | Specifies the path of sbt library. | [optional] 
**view_fs_path** | **str** | Specifies the Cohesity view path. | [optional] 
**vip_list** | **List[str]** | Specifies the list of Cohesity primary VIPs. | [optional] 
**vlan_info_list** | [**List[OracleVlanInfo]**](OracleVlanInfo.md) | Specifies the Vlan information for Cohesity cluster. | [optional] 

## Example

```python
from cohesity_sdk.models.oracle_sbt_host_params import OracleSbtHostParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleSbtHostParams from a JSON string
oracle_sbt_host_params_instance = OracleSbtHostParams.from_json(json)
# print the JSON string representation of the object
print(OracleSbtHostParams.to_json())

# convert the object into a dict
oracle_sbt_host_params_dict = oracle_sbt_host_params_instance.to_dict()
# create an instance of OracleSbtHostParams from a dict
oracle_sbt_host_params_from_dict = OracleSbtHostParams.from_dict(oracle_sbt_host_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


