# InfectedFiles

Specifies a list of infected entities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str, none_type** | Specifies the pagination cookie. Cookie is used to  resume the enumeration of infected entities. When the cookie is set the fields viewNameVec, includeQuarantinedFiles and include UnquarantinedFiles are ignored.  | [optional] 
**infected_files** | [**[InfectedFile], none_type**](InfectedFile.md) | Specifies the list of infected entities. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


