# GcpDiskExclusionParams

Specifies the paramaters to exclude disks attached to GCP VM instances and exclude VMs without disks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_vm_with_no_disk** | **bool, none_type** | Specifies the paramaters to exclude VM without disks. | [optional] 
**raw_query** | **str, none_type** | Raw boolean query given as input by the user to exclude disk. User can input params in raw query form: (&lt;&gt; AND &lt;&gt; AND &lt;&gt; ..) OR (&lt;&gt; AND &lt;&gt; AND &lt;&gt; ..) OR (..) OR (..) OR .. There cannot be an OR operator inside the bracket. Example query: (K1 &#x3D; V1 AND K2 &#x3D; V2 AND K3 !&#x3D; V3) OR (K4 &#x3D; V4 AND K6 !&#x3D; V6). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


