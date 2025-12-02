# SnmpConfig

SNMP configuration for this cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_port** | **int** | AgentPort is the TCP port SNMP agent is using. | [optional] 
**operation** | **str** | Operation is the operation of configuring SNMP services. | [optional] 
**read_user** | [**SnmpUser**](SnmpUser.md) |  | [optional] 
**server** | **str** | Server is the IP address of Network Management System. | [optional] 
**system_info** | [**SnmpSysInfo**](SnmpSysInfo.md) |  | [optional] 
**trap_port** | **int** | TrapPort is the TCP port SNMP agent is using. | [optional] 
**trap_user** | [**SnmpUser**](SnmpUser.md) |  | [optional] 
**version** | **str** | SnmpVersion is the SNMP version to talk with SNMP agent. It is SNMP V2 or SNMP V3. | [optional] 
**vip** | **str** | Vip is the IP address SNMP agent and SNMP Trap Daemon will use. It should be one of the VIPs assigned to the cluster. | [optional] 
**write_user** | [**SnmpUser**](SnmpUser.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.snmp_config import SnmpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpConfig from a JSON string
snmp_config_instance = SnmpConfig.from_json(json)
# print the JSON string representation of the object
print(SnmpConfig.to_json())

# convert the object into a dict
snmp_config_dict = snmp_config_instance.to_dict()
# create an instance of SnmpConfig from a dict
snmp_config_from_dict = SnmpConfig.from_dict(snmp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


