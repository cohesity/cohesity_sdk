# ViewAliasInfo

View Alias Info is returned as part of list views.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_name** | **str** | Alias name. | [optional] 
**client_subnet_whitelist** | [**List[Subnet]**](Subnet.md) | List of external client subnet IPs that are allowed to access the share. | [optional] 
**enable_filer_audit_log** | **bool** | This field is currently deprecated. Specifies whether to enable filer audit log on this view alias. This is only used if filer audit logging is enabled in cluster config. | [optional] 
**file_audit_logging_state** | **str** | Specifies the state of File Audit logging for this Share. Supported types: [Inherited, Enabled, Disabled]. Inherited: Audit log setting is inherited from the  View. Enabled: Audit log is enabled for this Share. Disabled: Audit log is disabled for this Share. | [optional] 
**smb_config** | [**AliasSmbConfig**](AliasSmbConfig.md) |  | [optional] 
**view_path** | **str** | View path for the alias. | [optional] 

## Example

```python
from cohesity_sdk.models.view_alias_info import ViewAliasInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ViewAliasInfo from a JSON string
view_alias_info_instance = ViewAliasInfo.from_json(json)
# print the JSON string representation of the object
print(ViewAliasInfo.to_json())

# convert the object into a dict
view_alias_info_dict = view_alias_info_instance.to_dict()
# create an instance of ViewAliasInfo from a dict
view_alias_info_from_dict = ViewAliasInfo.from_dict(view_alias_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


