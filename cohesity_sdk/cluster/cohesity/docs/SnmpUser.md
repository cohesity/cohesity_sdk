# SnmpUser

SNMP User Info for this cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_password** | **str, none_type** | AuthPassword is the authentication password for SNMP V3 users. | [optional] 
**auth_protocol** | **str, none_type** | AuthPrototol is the authentication protocol for SNMP V3 users. | [optional] 
**context_name** | **str, none_type** | ContextName is the context used for SNMP V3. | [optional] 
**engine_id** | **str, none_type** | EngineID is the SNMP V3 Engine ID used by trap users. | [optional] 
**priv_password** | **str, none_type** | PrivPassword is the privacy password for SNMP V3 users. | [optional] 
**priv_protocol** | **str, none_type** | PrivPrototol is the privacy protocol for SNMP V3 users. | [optional] 
**security_level** | **str, none_type** | SecurityLevel is the SNMP V3 security level. It can be authNoPriv, noPriv, and authPriv. | [optional] 
**user_name** | **str, none_type** | UserName is the user name to access SNMP V2 or SNMP V3 agent. | [optional] 
**user_type** | **str, none_type** | UserType is the SNMP user type, can be read-only user, read/write user, or trap users. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


