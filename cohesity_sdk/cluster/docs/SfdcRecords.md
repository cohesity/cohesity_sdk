# SfdcRecords

Specifies the list of salesforce records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_names** | **List[str]** | Specifies the column names for the records. | [optional] 
**records** | **List[List[str]]** | Each record is represented by an array of strings having the same order as the &#39;columnNames&#39;. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sfdc_records import SfdcRecords

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcRecords from a JSON string
sfdc_records_instance = SfdcRecords.from_json(json)
# print the JSON string representation of the object
print(SfdcRecords.to_json())

# convert the object into a dict
sfdc_records_dict = sfdc_records_instance.to_dict()
# create an instance of SfdcRecords from a dict
sfdc_records_from_dict = SfdcRecords.from_dict(sfdc_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


