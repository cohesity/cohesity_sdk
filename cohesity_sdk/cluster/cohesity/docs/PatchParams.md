# PatchParams

One of `packageUrl` or `versionName` must be specified. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_on_pre_checks_failure** | **bool** | Specifies if healthchecks failure will cause apply patch to be aborted. By default we patch if there are healthchecks failures. Cluster will stop the apply patch and present the failures which need to be resolved before proceeding with apply patch. If set to false, apply patchwill not be aborted on healthchecks failure.  | [optional]  if omitted the server will use the default value of True
**apply_patch_in_parallel** | **bool** | If set to true, patch will be applied in parallel on all nodes. Applicable for operations: * &#x60;ApplyPatch&#x60; * &#x60;DownloadAndApplyPatch&#x60;  | [optional]  if omitted the server will use the default value of False
**node_ids** | **[int]** | Node IDs where patch has to be applied.  If unspecified, patch will be applied on all nodes.  | [optional] 
**package_url** | [**ArtifactUrl**](ArtifactUrl.md) |  | [optional] 
**version_name** | **str** | Version name of the package if the package is already downloaded. Example: 7.0.1-p1-2023Jul04-cc6d7c5f Applicable for operations: * &#x60;ApplyPatch&#x60; * &#x60;RevertPatch&#x60; * &#x60;UpgradeAndPatch&#x60;  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


