# SnmpUser

SNMP User Info for this cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_password** | **str** | AuthPassword is the authentication password for SNMP V3 users. | [optional] 
**auth_protocol** | **str** | AuthPrototol is the authentication protocol for SNMP V3 users. | [optional] 
**context_name** | **str** | ContextName is the context used for SNMP V3. | [optional] 
**engine_id** | **str** | EngineID is the SNMP V3 Engine ID used by trap users. | [optional] 
**priv_password** | **str** | PrivPassword is the privacy password for SNMP V3 users. | [optional] 
**priv_protocol** | **str** | PrivPrototol is the privacy protocol for SNMP V3 users. | [optional] 
**security_level** | **str** | SecurityLevel is the SNMP V3 security level. It can be authNoPriv, noPriv, and authPriv. | [optional] 
**user_name** | **str** | UserName is the user name to access SNMP V2 or SNMP V3 agent. | [optional] 
**user_type** | **str** | UserType is the SNMP user type, can be read-only user, read/write user, or trap users. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.snmp_user import SnmpUser

# TODO update the JSON string below
json = "{}"
# create an instance of SnmpUser from a JSON string
snmp_user_instance = SnmpUser.from_json(json)
# print the JSON string representation of the object
print(SnmpUser.to_json())

# convert the object into a dict
snmp_user_dict = snmp_user_instance.to_dict()
# create an instance of SnmpUser from a dict
snmp_user_from_dict = SnmpUser.from_dict(snmp_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


