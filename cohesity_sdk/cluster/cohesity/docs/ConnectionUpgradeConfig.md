# ConnectionUpgradeConfig

Specifies the config for upgrading an individual connection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Specifies the ID of the connection. | [optional] 
**connection_patch_package_url** | **str, none_type** | \&quot;Specifies the patch package url to be used for patching a connection in specific. If this is provided, it will override the defaultPatchPackage and tenantPatchPackageUrl URLs. This URL will be used to download the package by connector. It can be http or https and must be IPv4 address or hostname (must be resolvable by the connector). | [optional] 
**connection_upgrade_package_url** | **str, none_type** | Specifies the upgrade package url to be used for upgrading the connection. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


