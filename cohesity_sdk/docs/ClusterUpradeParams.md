# ClusterUpradeParams

Specifies the parameters to upgrade the software on the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The operation type. &#39;Upgrade&#39; indicates to upgrade the software on the cluster. &#39;UploadPackageAndUpgrade&#39; indicates to first upload the package using the url where package is hosted and then upgrade the cluster. | 
**abort_upgrade_on_checks_failure** | **bool** | Specifies if pre upgrade healthchecks failure will cause upgrade to be aborted. By default we abort upgrade if there are healthchecks failures .Cluster will stop the upgrade.and present the failures which need to be resolved before proceeding with upgrade. If set to false upgrade will not be aborted on healthchecks failure. | [optional]  if omitted the server will use the default value of True
**url** | **str** | The URL where the package is hosted. This is required when the operation type is &#39;UploadPackageAndUpgrade&#39; | [optional] 
**version_name** | **str** | Version name of the package. Example: 6.3.1h_release-20210714_0fad884e. This is required when the operation type is &#39;Upgrade&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


