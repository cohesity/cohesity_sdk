# UpgradeConfig

Specifies the config for upgrading connections.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_upgrade_configs_override** | [**[ConnectionUpgradeConfig], none_type**](ConnectionUpgradeConfig.md) | Specifies the upgrade config of connections to be upgraded. If the tenantUpgradeConfigs is provided, connections in the tenantUpgradeConfigs would be upgraded along with the connections in connectionUpgradeConfigs. If this is provided, it will override upgradePackageUrl and tenantUpgradeConfigsOverride for the connection. | [optional] 
**default_patch_package_url** | **str, none_type** | Specifies the patch package url for the connections. If no overrides are mentioned, this URL will be used. This URL will be used to download the package by connector. It can be http or https and must be IPv4 address or hostname (must be resolvable by the connector). | [optional] 
**default_upgrade_package_url** | **str, none_type** | Specifies the default upgrade package url for the connections unless an override is specified for a tenant or connection. All connections will be upgraded using this URL if specified. | [optional] 
**tenant_upgrade_configs_override** | [**[TenantUpgradeConfig], none_type**](TenantUpgradeConfig.md) | Specifies the upgrade config of tenants for which the connections would be upgraded. If this is provided, it will override defaultUpgradePackageUrl for the tenant. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


