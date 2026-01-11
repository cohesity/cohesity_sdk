# UpdateFirewallRequest

Specifies the parameters to configure firewall settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**FirewallEntry**](FirewallEntry.md) |  | 
**update_attachment** | **bool, none_type** | If true, updates the firewall attachments. | defaults to False
**update_ipset** | **bool, none_type** | If true, updates the firewall IP sets. | defaults to False
**update_profile** | **bool, none_type** | If true, updates the firewall profiles. | defaults to False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


