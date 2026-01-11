# DowntieringFileAgePolicy

Specifies the file's selection rule by file age for down tiering data tiering task eg. 1. select files older than 10 days. 2. select files last accessed 2 weeks ago. 3. select files last modified 1 month ago.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_msecs** | **int, none_type** | Specifies the number of msecs used for file selection. | [optional] 
**condition** | **str, none_type** | Specifies the condition for the file age. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


