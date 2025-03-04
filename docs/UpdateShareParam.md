# UpdateShareParam

Specifies the parameter to update a Share.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_subnet_whitelist** | [**List[Subnet]**](Subnet.md) | List of external client subnet IPs that are allowed to access the share. | [optional] 
**enable_filer_audit_logging** | **bool** | This field is currently deprecated. Specifies if Filer Audit Logging is enabled for this Share. | [optional] 
**file_audit_logging_state** | **str** | Specifies the state of File Audit logging for this Share. Inherited: Audit log setting is inherited from the  View. Enabled: Audit log is enabled for this Share. Disabled: Audit log is disabled for this Share. | [optional] 
**smb_config** | [**AliasSmbConfig**](AliasSmbConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.update_share_param import UpdateShareParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShareParam from a JSON string
update_share_param_instance = UpdateShareParam.from_json(json)
# print the JSON string representation of the object
print(UpdateShareParam.to_json())

# convert the object into a dict
update_share_param_dict = update_share_param_instance.to_dict()
# create an instance of UpdateShareParam from a dict
update_share_param_from_dict = UpdateShareParam.from_dict(update_share_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


