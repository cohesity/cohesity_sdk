# ClusterUpradeParams

Specifies the parameters to upgrade the software on the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The operation type. &#39;Upgrade&#39; indicates to upgrade the software on the cluster. &#39;UploadPackageAndUpgrade&#39; indicates to first upload the package using the url where package is hosted and then upgrade the cluster. | 
**version_name** | **str** | Version name of the package. Example: 6.3.1h_release-20210714_0fad884e. This is required when the operation type is &#39;Upgrade&#39; | [optional] 
**url** | **str** | The URL where the package is hosted. This is required when the operation type is &#39;UploadPackageAndUpgrade&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


