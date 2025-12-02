# UpgradeParams

Parameters to upgrade the cluster software One of `packageUrl` or `versionName` must be specified. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_on_pre_checks_failure** | **bool** | Specifies if healthchecks failure will cause upgrade to be aborted. By default we abort upgrade if there are healthchecks failures .Cluster will stop the upgrade.and present the failures which need to be resolved before proceeding with upgrade. If set to false upgrade will not be aborted on healthchecks failure.  | [optional] [default to True]
**auto_agent_upgrade** | **bool** | Upgrade Cohesity agents on servers of registered sources.  | [optional] 
**ignore_sw_incompatibility** | **bool** | If set to true, software incomaptibility checks are ignored. Applicable for operations: * &#x60;DownloadAndUpgradeWithPatch&#x60; * &#x60;DownloadAndUpgrade&#x60; * &#x60;Upgrade&#x60; * &#x60;UpgradeAndPatch&#x60;  | [optional] [default to False]
**md5_sum** | **str** | md5Sum of the upgrade package. Applicable for operations: * &#x60;DownloadAndUpgradeWithPatch&#x60; * &#x60;DownloadAndUpgrade&#x60; * &#x60;Upgrade&#x60; * &#x60;UpgradeAndPatch&#x60;  | [optional] 
**package_url** | [**ArtifactUrl**](ArtifactUrl.md) |  | [optional] 
**run_upgrade_in_parallel** | **bool** | If set to true, upgrade will run in parallel on all nodes. Applicable for operations: * &#x60;DownloadAndUpgradeWithPatch&#x60; * &#x60;DownloadAndUpgrade&#x60; * &#x60;Upgrade&#x60; * &#x60;UpgradeAndPatch&#x60;  | [optional] [default to False]
**version_name** | **str** | Version name of the package if the package is already downloaded. Example: 6.3.1h_release-20210714_0fad884e. Applicable for operations: * &#x60;Upgrade&#x60; * &#x60;UpgradeAndPatch&#x60;  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.upgrade_params import UpgradeParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeParams from a JSON string
upgrade_params_instance = UpgradeParams.from_json(json)
# print the JSON string representation of the object
print(UpgradeParams.to_json())

# convert the object into a dict
upgrade_params_dict = upgrade_params_instance.to_dict()
# create an instance of UpgradeParams from a dict
upgrade_params_from_dict = UpgradeParams.from_dict(upgrade_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


