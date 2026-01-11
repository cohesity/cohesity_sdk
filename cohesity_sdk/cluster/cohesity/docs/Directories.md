# Directories

Specifies the information of all the directories corresponding to the snapshot ID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str, none_type** | Cookie is used for paginating results. If ReadVMDirResult is returning partial results, this field will be set. Supplying this cookie will resume listing from where this result left off. | [optional] 
**entries** | [**[Directory], none_type**](Directory.md) | Entries is the array of files and folders that are immediate children of the parent directory specified in the request. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


