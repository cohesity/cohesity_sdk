# ClusterSWUpdateParams

Specifies the parameters to update the software on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assess_software_update_params** | [**AssessSoftwareUpdateParams**](AssessSoftwareUpdateParams.md) |  | [optional] 
**node_type** | **str** | Type of node where upgrade has to be performed using the provided package. * &#x60;ClusterNode&#x60; * &#x60;ConnectorNode&#x60; nodeType is only applicable for following operation types. * &#x60;DownloadUpgradePackage&#x60; * &#x60;DownloadPatchPackage&#x60; * &#x60;DownloadUpgradeAndPatchPackages&#x60;  | [optional] 
**operation_type** | **str** | The operation type. * &#x60;DownloadUpgradePackage&#x60; - Operation to download upgrade package. * &#x60;DownloadPatchPackage&#x60; - Operation to download patch package. * &#x60;DownloadUpgradeAndPatchPackages&#x60; - Operation to download upgrade    and patch packages. * &#x60;DownloadAndUpgrade&#x60; - Operation to download package and    and then upgrade the cluster. * &#x60;DownloadAndApplyPatch&#x60; - Operation to download package and    and then apply the patch. * &#x60;DownloadAndUpgradeWithPatch&#x60; - Operation to download upgrade   and patch packages, and then, upgrade the cluster and immediately   patch it * &#x60;Upgrade&#x60; - Operation to upgrade the software on the cluster. * &#x60;ApplyPatch&#x60; - Operation to apply the patch. * &#x60;RevertPatch&#x60; - Operation to revert the patch. * &#x60;UpgradeAndPatch&#x60; - Operation to upgrade the software on the   cluster and apply a patch. * &#x60;AssessSoftwareUpdate&#x60; - Operation to perform checks to assess   the state of cluster pre/post software update (upgrade/patch). * &#x60;AbortApplyPatch&#x60; - Operation to abort the patch. * &#x60;AbortUpgrade&#x60; - Operation to abort the upgrade.  | 
**patch_params** | [**PatchParams**](PatchParams.md) |  | [optional] 
**upgrade_params** | [**UpgradeParams**](UpgradeParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_sw_update_params import ClusterSWUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSWUpdateParams from a JSON string
cluster_sw_update_params_instance = ClusterSWUpdateParams.from_json(json)
# print the JSON string representation of the object
print(ClusterSWUpdateParams.to_json())

# convert the object into a dict
cluster_sw_update_params_dict = cluster_sw_update_params_instance.to_dict()
# create an instance of ClusterSWUpdateParams from a dict
cluster_sw_update_params_from_dict = ClusterSWUpdateParams.from_dict(cluster_sw_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


