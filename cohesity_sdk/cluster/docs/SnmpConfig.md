# SnmpConfig

SNMP configuration for this cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_port** | **int, none_type** | AgentPort is the TCP port SNMP agent is using. | [optional] 
**operation** | **str, none_type** | Operation is the operation of configuring SNMP services. | [optional] 
**read_user** | [**SnmpUser**](SnmpUser.md) |  | [optional] 
**server** | **str, none_type** | Server is the IP address of Network Management System. | [optional] 
**system_info** | [**SnmpSysInfo**](SnmpSysInfo.md) |  | [optional] 
**trap_port** | **int, none_type** | TrapPort is the TCP port SNMP agent is using. | [optional] 
**trap_user** | [**SnmpUser**](SnmpUser.md) |  | [optional] 
**version** | **str, none_type** | SnmpVersion is the SNMP version to talk with SNMP agent. It is SNMP V2 or SNMP V3. | [optional] 
**vip** | **str, none_type** | Vip is the IP address SNMP agent and SNMP Trap Daemon will use. It should be one of the VIPs assigned to the cluster. | [optional] 
**write_user** | [**SnmpUser**](SnmpUser.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


