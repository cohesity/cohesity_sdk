# SiteRestoreParam

Specifies the parameters to recover a MSGroup site document.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_library_params** | [**[OneDriveParam], none_type**](OneDriveParam.md) | Specifies the list of document library items to recover in the MSGroup site. | 
**target_doc_lib_name** | **str, none_type** | Specifies the name for the target document library. Should be provided iff it is an alternate granular group site restore either to a different document library in the same group site or a document library in a different group site within the same M365 source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


