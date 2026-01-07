# FlashbladeParams

Specifies the information related to Registered Pure Flashblade.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_capacity_bytes** | **int, none_type** | Specifies the capacity in bytes assigned on pure flashblade for remote storage usage on cohesity cluster. | [optional] 
**assigned_data_vips** | **[str], none_type** | Specifies list of data vips that are assigned to cohesity cluster to create nfs share mountpoints. | [optional] 
**available_capacity** | **int, none_type** | Available capacity on pure flashblade. | [optional] [readonly] 
**available_data_vips** | **[str, none_type]** | Available data vips configured on pure flashblade. | [optional] [readonly] 
**created_file_system_count** | **int, none_type** | Number of new file systems created on pure flashblade when assignedCapacityBytes is updated. | [optional] [readonly] 
**is_dedicated_storage** | **bool, none_type** | If true, cohesity cluster uses all available capacity on pure flashblade for remote storage. | [optional] 
**name** | **str, none_type** | Name of the pure flashblade specified on pure storage. | [optional] [readonly] 
**registration_params** | [**FlashBladeRegistrationInfo**](FlashBladeRegistrationInfo.md) |  | [optional] 
**software_os_version** | **str, none_type** | Software OS and version running on pure flashblade | [optional] [readonly] 
**total_capacity** | **int, none_type** | Total capacity of pure flashblade. | [optional] [readonly] 
**updated_file_system_count** | **int, none_type** | Number of file systems that are updated on pure flashblade when assignedCapacityBytes is updated. | [optional] [readonly] 
**uuid** | **str, none_type** | Specifies uuid of the pure flashblade server. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


