# IpmiSelNonVerboseEntry

Specifies each entry in the sel verbose response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_assertion_type** | **str, none_type** | Specifies whether the event is asserted or not. This is only returned in case of verbose &#x3D; false. | [optional] 
**record_date** | **str, none_type** | Specifies the date on which the record is added to SEL. This is only returned in case of verbose &#x3D; false. | [optional] 
**record_description** | **str, none_type** | Specifies a short description corresponding to the sensor event for which record is added to SEL. | [optional] 
**record_event** | **str, none_type** | Provides a short description related to sensor action. This is only returned in case of verbose &#x3D; false. | [optional] 
**record_id** | **str, none_type** | Specifies the ID corresponding to record in SEL(System Event Log) for given node. | [optional] 
**record_time** | **str, none_type** | Specifies the time at which the record is added to SEL. This is only returned in case of verbose &#x3D; false. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


