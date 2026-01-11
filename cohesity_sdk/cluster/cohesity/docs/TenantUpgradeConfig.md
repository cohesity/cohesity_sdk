# TenantUpgradeConfig

Specifies the tenant config for upgrading connections.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Specifies the ID of the tenant. | [optional] 
**tenant_patch_package_url** | **str, none_type** | \&quot;Specifies the patch package url to be used for patching the connections for a specific tenant. If this is provided, it will override the defaultPatchPackage URL. This URL will be used to download the package by connector. It can be http or https and must be IPv4 address or hostname (must be resolvable by connector). | [optional] 
**tenant_upgrade_package_url** | **str, none_type** | Specifies the upgrade package url to be used for upgrading the connections in the tenant. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


