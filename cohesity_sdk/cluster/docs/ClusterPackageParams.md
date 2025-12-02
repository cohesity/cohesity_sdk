# ClusterPackageParams

Cluster software package parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatible_packages** | **[str]** | Array of versionName values, representing compatible packages that are available on system.  | [optional] 
**components** | [**[PackageComponent]**](PackageComponent.md) | List of package componenets. Aplicable for one helios package  | [optional] 
**file_size_bytes** | **int** | Size of file in bytes | [optional] 
**fixed_issues** | [**ClusterPackageFixedIssues**](ClusterPackageFixedIssues.md) |  | [optional] 
**is_downtime_required** | **bool, none_type** | Indicates whether package need downtime during installation | [optional]  if omitted the server will use the default value of False
**md5_checksum** | **str** | MD5 Checksum | [optional] 
**node_ids** | **[int]** | Node IDs where package is available | [optional] 
**node_type** | **str** | Type of node where upgrade has to be performed using the provided package. * &#x60;ClusterNode&#x60; * &#x60;ConnectorNode&#x60;  | [optional] 
**package_sub_type** | **str** | Sub-type of package - Security Patch or Product Patch | [optional] 
**package_type** | **str** | Type of the package - Upgrade or Patch | [optional] 
**release_date** | **datetime, none_type** | Release date of the package. | [optional] 
**release_version** | **str** | Release version of the package. Examples: For upgrade package: &#39;6.6.0d_u6&#39;, &#39;7.0.&#39; For patch package - &#39;6.8.1-p1s1&#39;  | [optional] 
**sha256_checksum** | **str** | SHA256 Checksum | [optional] 
**status** | [**ClusterPackageStatus**](ClusterPackageStatus.md) |  | [optional] 
**version_name** | **str, none_type** | Name of the package version. Example: &#39;6.6.0d_u6_release-20210714_0fad884e&#39;,   &#39;7.0.1_release-20230623_ddbb8c79&#39; for upgrade packages, &#39;6.8.1-p1s1-2023Jun26-221b8a5c&#39; for patch packages  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


