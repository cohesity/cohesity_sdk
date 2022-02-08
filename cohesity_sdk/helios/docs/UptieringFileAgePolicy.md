# UptieringFileAgePolicy

Specifies the file's selection rule by file age for up tiering data   tiering task eg.   1. select files last accessed 2 weeks ago.   2. select files last modified 1 month ago.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str, none_type** | Specifies the condition for the file age. | [optional] 
**age_msecs** | **int, none_type** | Specifies the number of msecs used for file selection. | [optional] 
**num_file_access** | **int, none_type** | Specifies number of file access in last ageMsecs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


