# FilterIpConfig

Specifies the list of IP addresses that are allowed or denied during recovery. Allowed IPs and Denied IPs cannot be used together.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied_ip_addresses** | **[str], none_type** | Specifies the IP addresses that should not be used during recovery recovery. Cannot be set if allowedIpAddresses is set. | [optional] 
**allowed_ip_addresses** | **[str], none_type** | Specifies the IP addresses that should be used exclusively during recovery. Cannot be set if deniedIpAddresses is set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


