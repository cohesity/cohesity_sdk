# ConnectionUpgradeConfig

Specifies the config for upgrading an individual connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Specifies the ID of the connection. | [optional] 
**connection_patch_package_url** | **str** | \&quot;Specifies the patch package url to be used for patching a connection in specific. If this is provided, it will override the defaultPatchPackage and tenantPatchPackageUrl URLs. This URL will be used to download the package by connector. It can be http or https and must be IPv4 address or hostname (must be resolvable by the connector). | [optional] 
**connection_upgrade_package_url** | **str** | Specifies the upgrade package url to be used for upgrading the connection. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connection_upgrade_config import ConnectionUpgradeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionUpgradeConfig from a JSON string
connection_upgrade_config_instance = ConnectionUpgradeConfig.from_json(json)
# print the JSON string representation of the object
print(ConnectionUpgradeConfig.to_json())

# convert the object into a dict
connection_upgrade_config_dict = connection_upgrade_config_instance.to_dict()
# create an instance of ConnectionUpgradeConfig from a dict
connection_upgrade_config_from_dict = ConnectionUpgradeConfig.from_dict(connection_upgrade_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


