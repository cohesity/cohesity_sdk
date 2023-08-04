# FlashbladeParams

Specifies the information related to Registered Pure Flashblade.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_params** | [**FlashBladeRegistrationInfo**](FlashBladeRegistrationInfo.md) |  | [optional] 
**uuid** | **str, none_type** | Specifies uuid of the pure flashblade server. | [optional] [readonly] 
**assigned_data_vips** | **[str], none_type** | Specifies list of data vips that are assigned to cohesity cluster to create nfs share mountpoints. | [optional] 
**assigned_capacity_bytes** | **int, none_type** | Specifies the capacity in bytes assigned on pure flashblade for remote storage usage on cohesity cluster. | [optional] 
**is_dedicated_storage** | **bool, none_type** | If true, cohesity cluster uses all available capacity on pure flashblade for remote storage. | [optional] 
**available_data_vips** | **[str, none_type]** | Available data vips configured on pure flashblade. | [optional] [readonly] 
**available_capacity** | **int, none_type** | Available capacity on pure flashblade. | [optional] [readonly] 
**created_file_system_count** | **int, none_type** | Number of new file systems created on pure flashblade when assignedCapacityBytes is updated. | [optional] [readonly] 
**updated_file_system_count** | **int, none_type** | Number of file systems that are updated on pure flashblade when assignedCapacityBytes is updated. | [optional] [readonly] 
**software_os_version** | **str, none_type** | Software OS and version running on pure flashblade | [optional] [readonly] 
**name** | **str, none_type** | Name of the pure flashblade specified on pure storage. | [optional] [readonly] 
**total_capacity** | **int, none_type** | Total capacity of pure flashblade. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


